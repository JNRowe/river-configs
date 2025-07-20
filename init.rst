Config time
===========

.. ifconfig:: not github_actions

    .. note::

        The `generated HTML`_ will likely be a better reading experience.

My |river| configuration is created by extracting the code blocks from within
this file. It sounds *far* more complex than it needs to be, but it fits in to
an elaborate ninja_ configuration that I use to generate my home directories.
The advantage *to me* is that I can mix-and-match software versions on different
machines, but it also means that the repository structure for individual
configurations looks overcomplicated from the outside.

.. tip::

    The output from ``tools/rst2zsh`` includes comment markers that can be used
    to navigate back to the source in this file.  For example, in vim_ calling
    ``gF`` will jump to the section under the cursor.

Software versions
-----------------

==================  ===========================
Package             Version
==================  ===========================
foot_               1.21.0
|river|             0.3.0+git76~gbe7c6dc [#s1]_
river-tag-overlay_  1.0.0
sandbar_            0.1+git23~g0e942af [#s2]_
swayidle_           1.8.0
wideriver_          1.2.0+git20~ge4d64c0 [#s2]_
wob_                0.14.2
==================  ===========================

.. note::

    These are the base versions from upstream, there may be local additions
    exposed in the installation packages.  However, they will *not* introduce
    breaking changes.

General setup
-------------

We’re going to use zsh_ as it is *always* available on any system I use::

    #! /bin/zsh -x

.. note::

    We set ``-x`` here because it is gives us a lazy logging mechanism to catch
    and report errors at practically zero cost.  In the initial run output will
    end up in river’s log, and in subsequent runs it will be in the executing
    terminal.

We’ll want stricter defaults out of the box::

    setopt err_exit no_unset warn_create_global

.. _extended_glob:

… along with extended globs for better matching support::

    setopt extended_glob

.. _add_zsh_hook:

``autoload`` functions we’ll need later::

    autoload -Uz add-zsh-hook

Utility functions
-----------------

Fetch socket path for systemd_ ``.socket`` units::

    find_socket() {
        systemctl --user show $1@$WAYLAND_DISPLAY.socket --property=Listen |
            sed 's,.*=\(.*\) .*,\1,'
    }

.. _progress bar within this file:

Populate a wob_ progress bar, if possible, as we move through the ``init``
file::

    LINES=${#${(@f)"$(< $0)"}}
    _progress() {
        setopt local_options no_xtrace
        [[ -z ${wob_pipe:-} ]] && return
        float line=${funcfiletrace[1]##*:}
        integer pcnt=$(((line - 1) / LINES * 100))
        echo $pcnt >>$wob_pipe
    }
    add-zsh-hook preexec _progress

While startup is fast enough that a progress marker isn’t necessary, I find it
quite useful as a smoketest that quickly highlights an error in the
configuration if the progress bar doesn’t reach the end.  Also, I’ll be honest,
it felt like a fun hack.

.. note::

    This doesn’t strictly require add_zsh_hook_, but I prefer the interface
    offered by it over simply setting the hook by hand.

Calculate a tag mask given a list of tags::

    tag_mask() {
        integer r n
        for n ($@) {
            r+=$((1 << (n-1)))
        }
        echo $r
    }
    ALL_TAGS=$(tag_mask {1..32})

Configure environment
---------------------

Configure environment variables used by freedesktop.org_ specifications::

    export XDG_SESSION_TYPE=wayland XDG_{CURRENT,SESSION}_DESKTOP=river

.. warning::

    It is important to be aware that ``river`` is not a standard compliant value
    for ``XDG_*_DESKTOP``, but I’m already using it locally to trigger
    behaviour.  I’ll change it if a better option appears later.

Make important environment variables available to dbus_ and ``systemd`` units::

    envvars=(
        PATH
        WAYLAND_DISPLAY
        XDG_SESSION_TYPE
        XDG_{CURRENT,SESSION}_DESKTOP
    )
    if (( $+commands[dbus-update-activation-environment] )) {
        dbus-update-activation-environment --systemd $envvars
    } else {
        systemctl --user import-environment $envvars
    }

Run background services
-----------------------

I manage all my background services with a systemd_ user session.  ``systemd``
handles all the gory details of process supervision, so that — for example — you
don’t need to implement your own hot reloading for your status script.

The interesting thing to notice below is that I use instances keyed off of
``WAYLAND_DISPLAY`` so that it is possible to run multiple sessions, which comes
in handy for testing as you can simply start a new nested session.

Start foot_ server::

    systemctl --user start foot-server@$WAYLAND_DISPLAY.socket

Start sandbar_::

    systemctl --user start sandbar@$WAYLAND_DISPLAY.socket
    sandbar_pipe=$(find_socket sandbar)
    systemctl --user start sandbar_status@$WAYLAND_DISPLAY

.. note::

    We fetch the ``sandbar`` socket location so that we can issue commands to it
    from within this file.

Start swayidle_::

    systemctl --user start swayidle@$WAYLAND_DISPLAY

Start wideriver_::

    systemctl --user start wideriver@$WAYLAND_DISPLAY

Start wob_::

    systemctl --user start wob@$WAYLAND_DISPLAY.socket
    wob_pipe=$(find_socket wob)

.. note::

    We fetch the socket location so that we can use it for a `progress bar
    within this file`_.

Start river-tag-overlay_::

    systemctl --user start river-tag-overlay@$WAYLAND_DISPLAY

Keybindings
-----------

General bindings::

    riverctl map normal Super+Shift Q exit

    riverctl map normal Super Page_Up focus-output next
    riverctl map normal Super Page_Down focus-output previous

    riverctl map normal Super B \
        spawn "echo all toggle-visibility >>$sandbar_pipe"
    riverctl map normal Super+Shift B \
        spawn "echo all toggle-location >>$sandbar_pipe"

Extended keys
'''''''''''''

Configure function keys::

    for mode (normal locked) {
        riverctl map $mode None XF86MonBrightnessUp \
            spawn "brightness_toggle up"
        riverctl map $mode None XF86MonBrightnessDown \
            spawn "brightness_toggle down"

        riverctl map $mode None XF86AudioPlay spawn "dtas-ctl play_pause"
        riverctl map $mode None XF86AudioNext spawn "dtas-ctl skip"

        riverctl map $mode None XF86AudioMute spawn "amixer sset Master toggle"
        riverctl map -repeat $mode None XF86AudioRaiseVolume \
            spawn "amixer sset Master 5%+"
        riverctl map -repeat $mode None XF86AudioLowerVolume \
            spawn "amixer sset Master 5%-"
    }

.. note::

    Media and function keys perform tasks that should work regardless of screen
    lock state.

Passthrough mode for testing configuration
''''''''''''''''''''''''''''''''''''''''''

A really great idea from the `example river init file`_ giving a quick toggle to
make keys a no-op for testing nested compositors::

    riverctl declare-mode passthrough

    riverctl map normal Super F11 enter-mode passthrough
    riverctl map passthrough Super F11 enter-mode normal

Tag management
--------------

Direct key access for manipulation of tags one through nine::

    for tag ({1..9}) {
        tag_id=$(tag_mask $tag)

        riverctl map normal Super $tag set-focused-tags $tag_id
        riverctl map normal Super+Shift $tag set-view-tags $tag_id
        riverctl map normal Super+Control $tag toggle-focused-tags $tag_id
        riverctl map normal Super+Shift+Control $tag toggle-view-tags $tag_id
    }

Show all, which you can treat it like a weak Apple’s Exposé::

    riverctl map normal Super 0 set-focused-tags $ALL_TAGS

Window management
-----------------

State bindings::

    riverctl map normal Super+Shift Return zoom
    riverctl map normal Super+Shift C close
    riverctl map normal Super+Shift 0 set-view-tags $ALL_TAGS

    riverctl map normal Super+Control Space toggle-float
    riverctl map normal Super F toggle-fullscreen

Navigation bindings::

    riverctl map normal Super Tab focus-view next
    riverctl map normal Super+Shift Tab focus-view previous

    riverctl map normal Super+Control Tab swap next
    riverctl map normal Super+Control+Shift Tab swap previous

Output bindings::

    riverctl map normal Super+Shift Page_up send-to-output next
    riverctl map normal Super+Shift Page_down send-to-output previous


Floating support
''''''''''''''''

::

    ARROW_KEYS=(Left Down Up Right)

Declare floating mode::

    riverctl declare-mode float
    riverctl map normal Super R enter-mode float
    riverctl map float None Escape enter-mode normal

.. note::

    We declare a full mode here to make large scale changes to windows easier to
    accomplish.  For quick changes all the modifiers aren’t a problem, but big
    changes are easier in the dedicated mode.

Basic movement bindings::

    for key ($ARROW_KEYS) {
        riverctl map normal Super+Alt $key move $key:l 100
        riverctl map float None $key move $key:l 100
    }

Cardinal movement bindings::

    for key ($ARROW_KEYS) {
        riverctl map normal Super+Alt+Control $key snap $key:l
        riverctl map float Control $key snap $key:l
    }

Basic resizing bindings::

    xs=(horizontal vertical)
    integer i=0 delta
    for key dir (${ARROW_KEYS:^^xs}) {
        delta=$((i++ % 2 ? 1 : -1))00
        riverctl map normal Super+Alt+Shift $key resize $dir $delta
        riverctl map float Shift $key resize $dir $delta
    }

Common applications
'''''''''''''''''''

Spawn a foot_ client instance::

    riverctl map normal Super Return spawn "footclient --no-wait"

Attempt to pick the most useful *to me* browser that is available::

    riverctl map normal Super Z spawn \
        "exec ${commands[firefox]:-${commands[chromium]:-sensible-browser}}"

Mouse bindings
--------------

Configure “standard” mouse bindings::

    riverctl map-pointer normal Super BTN_LEFT move-view
    riverctl map-pointer normal Super BTN_RIGHT resize-view

It is nice to have a simple way to flip the float bit on a window::

    riverctl map-pointer normal Super BTN_MIDDLE toggle-float

Using back and forward to manipulate the stack feels really quite natural::

    riverctl map-pointer normal Super BTN_FORWARD swap next
    riverctl map-pointer normal Super BTN_BACK swap previous

… and by extension back and forward to shuffle across outputs works well::

    riverctl map-pointer normal Super+Shift BTN_FORWARD send-to-output next
    riverctl map-pointer normal Super+Shift BTN_BACK send-to-output previous

Theming
-------

Use monokai_-pro palette::

    riverctl background-color 0x1b1d1e
    riverctl border-color-focused 0xa6e22e
    riverctl border-color-unfocused 0x75715e
    riverctl border-color-urgent 0xf92672

.. note::

    This should *really* be configured more centrally, but for the time being it
    works.

Input devices
-------------

Wait 300 milliseconds and then repeat keys 50 times per second::

    riverctl set-repeat 50 300

Configure non-standard `options for keyboard`_::

    declare -A _xkb_opts=(
        [caps]=escape_shifted_capslock
        [compose]=paus
        [keypad]=future
        [parens]=swap_brackets
    )
    xkb_opts_full=${(kj:,:)_xkb_opts/(#m)*/$MATCH:$_xkb_opts[$MATCH]}

.. note::

    The globbing flags used here require extended_glob_.

Perhaps those `obscure keyboard options`_ deserve an explanation:

===========================  ================================================
Option                       Description
===========================  ================================================
``escape_shifted_capslock``  Make ``Capslock`` an alternative ``Escape`` key,
                             but keep ``Capslock`` available with
                             ``Shift+Capslock``
``paus``                     Use ``Pause`` as `compose key`_
``future``                   Unicode mathematics operators, noting that ASCII
                             operators already exist on the main section
``swap_brackets``            Swap square bracket and parenthesis position
===========================  ================================================

Configure a subset without bracket swaps for editing square bracket heavy code::

    _xkb_opts_toggle=(parens)
    xkb_opts_toggle=${(kj:,:)${(k)_xkb_opts:|_xkb_opts_toggle}/(#m)*/$MATCH:$_xkb_opts[$MATCH]}

Default to ``swap_brackets`` behaviour::

    riverctl keyboard-layout -options $xkb_opts_full gb

Configure host specific touchpad settings::

    if [[ $HOST =~ ^(camille|corale)$ ]] {
        riverctl input pointer-2-14-ETPS/2_Elantech_Touchpad tap enabled
        riverctl input pointer-2-14-ETPS/2_Elantech_Touchpad pointer-accel 0.8
    }

We’ll declare a mode to wrap our input bindings, mainly as their use is uncommon
and we won’t lose a lot of keys this way::

    riverctl declare-mode input
    riverctl map normal Super I enter-mode input
    riverctl map input None Escape enter-mode normal

    if [[ $HOST =~ ^(camille|corale)$ ]] {
        riverctl map input None T input pointer-2-14-ETPS/2_Elantech_Touchpad \
            events disabled
        riverctl map input Shift T input pointer-2-14-ETPS/2_Elantech_Touchpad \
            events enabled
    }
    riverctl map input None K spawn "riverctl keyboard-layout \
        -options $xkb_opts_full gb"
    riverctl map input Shift K spawn "riverctl keyboard-layout \
        -options $xkb_opts_toggle gb"

Window rules
------------

Allow window tearing if requested by the application::

    riverctl allow-tearing enabled

Sloppy focus is the *only* focus model that makes any sense to me::

    riverctl focus-follows-cursor normal

Allow some rules to be stored outside default init to make it easier to share
across different machines.  For example, I *need* conflicting rules for outputs
depending on location.

::

    [[ -f $0:a:h/local_rules ]] && source $0:a:h/local_rules

Decades of use at this point means I always like the “second” tag — or workspace
2 for non-tagging interfaces — to contain a browser by default::

    riverctl rule-add -app-id "chromium" tags $(tag_mask 2)
    riverctl rule-add -app-id "firefox-esr" tags $(tag_mask 2)

I treat the “third” tag as media zone by default::

    riverctl rule-add -app-id "mpv" tags $(tag_mask 3)

.. note::

    It may make more sense to use a custom application identifier for the
    default apps, so that we can push them to their common tags but keep regular
    instances attached to current tag.

Layout
------

wideriver_ is the layout engine that is the closest match to the behaviour I’m
used to with awesomewm_, and makes a great default::

    riverctl default-layout wideriver

We’ll declare a layout mode to make it quicker — and easier on the hands — to
cycle layout controls when trying to pin down a comfortable setup::

    riverctl declare-mode layout
    riverctl map normal Super L enter-mode layout
    riverctl map layout None Escape enter-mode normal

Layout format manipulation bindings::

    riverctl map layout None M send-layout-cmd wideriver "--layout monocle"
    riverctl map layout None T send-layout-cmd wideriver "--layout left"
    riverctl map layout Shift T send-layout-cmd wideriver "--layout wide"
    riverctl map layout Control T send-layout-cmd wideriver "--layout right"
    riverctl map layout None Space send-layout-cmd wideriver "--layout-toggle"

Layout style manipulation bindings::

    riverctl map layout None E send-layout-cmd wideriver "--stack even"
    riverctl map layout None W send-layout-cmd wideriver "--stack dwindle"
    riverctl map layout None I send-layout-cmd wideriver "--stack diminish"

Main window ratio manipulation bindings::

    riverctl map layout None Equal send-layout-cmd wideriver "--ratio 0.52"
    riverctl map layout None H send-layout-cmd wideriver "--ratio +0.05"
    riverctl map layout None L send-layout-cmd wideriver "--ratio -0.05"

Bindings to adjust the number of windows in main stack::

    riverctl map layout Shift Equal send-layout-cmd wideriver "--count 1"
    riverctl map layout Shift H send-layout-cmd wideriver "--count +1"
    riverctl map layout Shift L send-layout-cmd wideriver "--count -1"

Add top level bindings for monocle and tile-left, as they’re my most common
layouts that I want quick access to::

    riverctl map normal Super M send-layout-cmd wideriver "--layout monocle"
    riverctl map normal Super T send-layout-cmd wideriver "--layout left"

Configure initial per-tag layouts::

    for n ({2..32..2}) {
        riverctl set-focused-tags $(tag_mask $n)
        riverctl send-layout-cmd wideriver "--layout monocle"
    }
    riverctl set-focused-tags $(tag_mask 1)

.. note::

    This reflects — what is at this point — my *decades* old tradition of
    defaulting to fullscreen on even tags.  It doesn’t really make sense, but
    I’m quite accustomed to it.

Finalising
----------

Allow a private machine specific configuration to be loaded::

    [[ -f $0:a:h/local_init ]] && source $0:a:h/local_init

Show ``sandbar``::

    echo all show >>$sandbar_pipe

.. note::

    ``sandbar`` is spawned hidden to allow us to issue per-tag layout changes or
    launch default applications without all the bar flashes that would result.

.. rubric:: Footnotes

.. [#s1] I’ve added some largely uninteresting local changes from
         v0.3.0-39-gccd676e, but mostly it is because there is no timeline for
         wlroots_ v0.18 hitting my installations.

.. [#s2] Beyond packaging changes there are only light hacks to use `Nerd
         Fonts`_ for icons.

.. _generated HTML: https://jnrowe.github.io/river-configs/
.. _ninja: https://ninja-build.org/
.. _vim: https://www.vim.org/
.. _foot: https://codeberg.org/dnkl/foot
.. _river-tag-overlay: https://git.sr.ht/~leon_plickat/river-tag-overlay
.. _sandbar: https://github.com/kolunmi/sandbar
.. _swayidle: https://github.com/swaywm/swayidle
.. _wideriver: https://github.com/alex-courtis/wideriver
.. _wob: https://github.com/francma/wob
.. _zsh: https://www.zsh.org/
.. _systemd: https://systemd.io
.. _freedesktop.org: https://freedesktop.org
.. _dbus: https://dbus.freedesktop.org/
.. _example river init file: https://codeberg.org/river/river/src/branch/master/example/init
.. _monokai: https://github.com/tanvirtin/monokai.nvim
.. _options for keyboard: https://www.freedesktop.org/wiki/Software/XKeyboardConfig/
.. _obscure keyboard options: https://xkcd.com/1806/
.. _compose key: https://en.wikipedia.org/wiki/Compose_key
.. _awesomewm: https://awesomewm.org/
.. _wlroots: https://gitlab.freedesktop.org/wlroots/wlroots/
.. _Nerd Fonts: https://www.nerdfonts.com/

.. spelling:word-list::

    Config
    Exposé
    Passthrough
    Theming
    aren
    doesn
    fullscreen
    gaa
    gccd
    globbing
    init
    isn
    overcomplicated
    smoketest
    touchpad
    ve
