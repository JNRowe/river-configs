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

.. _sandbar: https://github.com/kolunmi/sandbar
.. _example river init file: https://codeberg.org/river/river/src/branch/master/example/init

.. spelling:word-list::

    Exposé
    Keybindings
    Passthrough
