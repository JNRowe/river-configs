river-configs
=============

.. epigraph::

   So, imagine your workmate has created a new tool that *requires* Wayland…

This is my personal river_ configuration that is shared among hosts.  Maybe
they’re useful to you too, or — better yet — you’ll spot *and* fix a bug!

.. note::

    I’m writing this for myself as a |WIP| notebook.  Expect foolish — or even
    downright ignorant — errors and omissions.  Feel free to `drop me a note`_
    for clarifications or to fix my invalid assumptions.

This is in a very early state; basically the result of needing to get up and
running quickly, without breaking my workflow too much.  I haven’t decided on a
lot of things yet, so don’t expect this to work for you *or* remain as-is for
long.

Software
--------

``river`` (replacing ``awesomewm``/``dwm``)
'''''''''''''''''''''''''''''''''''''''''''

``river`` is definitely the only choice I’m comfortable with right now.  The
other tiling managers are either a little raw(dwl_) or very weak(sway_).  If the
setup changes it will be toward ``dwl`` or something that more closely resembles
awesomewm_.

What I want:

=======  =====================================================================
Feature  Reason
=======  =====================================================================
tags     Workspaces are an anaemic stub of a feature when you’re used to tags
dynamic  If I wanted to manage windows by hand I wouldn’t use a tiling manager
layouts  Some tags should be tiled in fancy patterns, some should be monocle
…        <things I depend on but haven’t noticed yet>
=======  =====================================================================

wideriver_ is a great layout engine, providing the main layouts I rely on.
I may well end up changing to one of the scriptable replacements at some point
though, both river-luatile_ and riverguile_ look enticing.

The main thing I’m missing right now is per-tag default layouts, but you can
work around that by issuing a heap of commands at startup(before any views are
created to prevent flicker).

Other candidates
^^^^^^^^^^^^^^^^

``dwl`` is close to perfect as a dwm_ replacement, but there a few rough edges
that need ironing out.  I’d recommend it to others who want a ``dwm``
experience.

``sway`` is popular with lots of support, but fails on every count for me.  Its
workspace implementation is ferociously under-featured.  Its layout splitting
feels like a chore.  Custom layouts require endless scripting after making
everything float.  Even seemingly simple things like window switching across
branches tends toward drudgery requiring heaps of code, you’ll even need to
implement locking to make sure keys aren’t swallowed if you execute commands
quickly.


vivarium_ feels very promising.  It features most of the layouts I’ve become
accustomed to, but its stability wasn’t great for me.

``foot`` (replacing ``alacritty``)
''''''''''''''''''''''''''''''''''

foot_ is amazing.  If I’d known it was available before it may have been the
catalyst for me to move to Wayland before now.  Something *unimaginably amazing*
would have to arrive for this not to be the choice going forward.

``sandbar`` (replacing built-in ``awesomewm``/``dwm`` functionality)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

sandbar_ does pretty much exactly what I want from a bar.  I’m going to miss how
integrated the ``wibox`` is in ``awesomewm``, but I’m comfortable enough making
the widgets I *really* care about work with ``sandbar``.

``wob`` (replacing ``dzen2``)
'''''''''''''''''''''''''''''

wob_ is simple little progress bar tool, that can replace a fair chunk of my
dzen2_ usage.  It isn’t featureful enough *by design* to be a full replacement,
but it remains to be seen how much I’ll miss the hover popups or context hints
that come with accompanying text.

Config time
-----------

.. note::

    If you’re viewing this on GitHub, then the `generated HTML`_ will be a
    better experience.

My configuration is created by extracting the code blocks from within this file.
It sounds *far* more complex than it needs to be, but it fits in to an elaborate
ninja_ configuration that I use to generate my home directories. The advantage
*to me* is that I can mix-and-match software versions on different machines, but
it also means that the repository structure for individual configurations looks
overcomplicated from the outside.

.. tip::

    The output from ``tools/rst2zsh`` includes comment markers that can be used
    to navigate back to the source in this file.  For example, in vim_ calling
    ``gF`` will jump to the section under the cursor.

General setup
'''''''''''''

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
'''''''''''''''''

Fetch socket path for systemd_ ``.socket`` units::

    find_socket() {
        systemctl --user show $1@$WAYLAND_DISPLAY.socket --property=Listen |
            sed 's,.*=\(.*\) .*,\1,'
    }

.. _progress bar within this file:

Populate a wob_ progress bar, if possible, as we move through the ``init``
file::

    LINES=$(awk 'END {print NR}' $0)
    _progress() {
        setopt local_options no_xtrace
        [[ -z ${wob_pipe:-} ]] && return
        float line=${funcfiletrace[1]##*:}
        integer pcnt=$(((line - 1) / LINES * 100))
        echo $pcnt >>$wob_pipe
    }
    add-zsh-hook preexec _progress

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
'''''''''''''''''''''

Configure environment variables used by freedesktop.org_ specifications::

    systemctl --user set-environment \
        XDG_SESSION_TYPE=wayland \
        XDG_{CURRENT,SESSION}_DESKTOP=river

.. warning::

    It is important to be aware that ``river`` is not a standard compliant value
    for ``XDG_*_DESKTOP``, but I’m already using it locally to trigger
    behaviour.  I’ll change it if a better option appears later.

Make important environment variables available to ``systemd`` units::

    systemctl --user import-environment \
        PATH \
        WAYLAND_DISPLAY

Run background services
'''''''''''''''''''''''

Start swaybg_::

    systemctl --user start swaybg@$WAYLAND_DISPLAY

Start foot_ server::

    systemctl --user start foot-server@$WAYLAND_DISPLAY.socket

Start sandbar_::

    systemctl --user start sandbar@$WAYLAND_DISPLAY.socket
    sandbar_pipe=$(find_socket sandbar)
    systemctl --user start sandbar_status@$WAYLAND_DISPLAY

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

Keybindings
'''''''''''

General bindings::

    riverctl map normal Super+Shift Q exit

    riverctl map normal Super Page_Up focus-output next
    riverctl map normal Super Page_Down focus-output previous

    riverctl map normal Super B \
        spawn "echo all toggle-visibility >>$sandbar_pipe"

Extended keys
^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A really great idea from the example river init file giving a quick toggle to
make keys a no-op for testing nested compositors::

    riverctl declare-mode passthrough

    riverctl map normal Super F11 enter-mode passthrough
    riverctl map passthrough Super F11 enter-mode normal

Tag management
''''''''''''''

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
'''''''''''''''''

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
^^^^^^^^^^^^^^^^

.. code:: zsh

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
^^^^^^^^^^^^^^^^^^^

Spawn a foot_ client instance::

    riverctl map normal Super Return spawn "footclient --no-wait"

Attempt to pick the most useful *to me* browser that is available::

    riverctl map normal Super Z spawn \
        "exec ${commands[firefox]:-${commands[chromium]:-sensible-browser}}"

Mouse bindings
''''''''''''''

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
'''''''

Use monokai_-pro palette::

    riverctl background-color 0x1b1d1e
    riverctl border-color-focused 0xa6e22e
    riverctl border-color-unfocused 0x75715e
    riverctl border-color-urgent 0xf92672

.. note::

    This should *really* be configured more centrally, but for the time being it
    works.

Input devices
'''''''''''''

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


Configure a subset without bracket swaps for editing square bracket heavy code::

    _xkb_opts_toggle=(parens)
    xkb_opts_toggle=${(kj:,:)${(k)_xkb_opts:|_xkb_opts_toggle}/(#m)*/$MATCH:$_xkb_opts[$MATCH]}

Default to ``swap_brackets`` behaviour::

    riverctl keyboard-layout -options $xkb_opts_full gb

Configure host specific touchpad settings::

    if [[ $HOST == corale ]] {
        riverctl input pointer-2-14-ETPS/2_Elantech_Touchpad tap enabled
        riverctl input pointer-2-14-ETPS/2_Elantech_Touchpad pointer-accel 0.8
    }

We’ll declare a mode to wrap our input bindings, mainly as their use is uncommon
and we won’t lose a lot of keys this way::

    riverctl declare-mode input
    riverctl map normal Super I enter-mode input
    riverctl map input None Escape enter-mode normal

    if [[ $HOST == corale ]] {
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
''''''''''''

Sloppy focus is the *only* focus model that makes any sense to me::

    riverctl focus-follows-cursor normal

Allow some rules to be stored outside default init to make it easier to share
across different machines.  For example, I *need* conflicting rules for outputs
depending on location.

.. code:: zsh

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
''''''

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
''''''''''

Allow a private machine specific configuration to be loaded::

    [[ -f $0:a:h/local_init ]] && source $0:a:h/local_init

Show ``sandbar``::

    echo all show >>$sandbar_pipe

.. note::

    ``sandbar`` is spawned hidden to allow us to issue per-tag layout changes or
    launch default applications without all the bar flashes that would result.

.. _river: https://codeberg.org/river/river
.. _dwl: https://codeberg.org/dwl/dwl.git
.. _sway: https://github.com/swaywm/sway/
.. _wideriver: https://github.com/alex-courtis/wideriver
.. _river-luatile: https://github.com/MaxVerevkin/river-luatile
.. _riverguile: https://git.sr.ht/~leon_plickat/riverguile
.. _awesomewm: https://awesomewm.org/
.. _foot: https://codeberg.org/dnkl/foot
.. _sandbar: https://github.com/kolunmi/sandbar
.. _wob: https://github.com/francma/wob
.. _drop me a note: mailto:jnrowe@gmail.com
.. _dzen2: https://github.com/robm/dzen
.. _ninja: https://ninja-build.org/
.. _dwm: http://dwm.suckless.org/
.. _vivarium: https://github.com/inclement/vivarium
.. _generated HTML: https://jnrowe.github.io/river-configs/
.. _vim: https://www.vim.org/
.. _zsh: https://www.zsh.org/
.. _systemd: https://systemd.io
.. _freedesktop.org: https://freedesktop.org
.. _swaybg: https://github.com/swaywm/swaybg
.. _swayidle: https://github.com/swaywm/swayidle
.. _monokai: https://github.com/tanvirtin/monokai.nvim
.. _options for keyboard: https://www.freedesktop.org/wiki/Software/XKeyboardConfig/

.. |WIP| raw:: html

    <abbr title="Work In Progress">WIP</abbr>
