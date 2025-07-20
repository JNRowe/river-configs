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
    within this file <progress_bar>`_.

Start river-tag-overlay_::

    systemctl --user start river-tag-overlay@$WAYLAND_DISPLAY

.. _systemd: https://systemd.io
.. _foot: https://codeberg.org/dnkl/foot
.. _sandbar: https://github.com/kolunmi/sandbar
.. _swayidle: https://github.com/swaywm/swayidle
.. _wideriver: https://github.com/alex-courtis/wideriver
.. _wob: https://github.com/francma/wob
.. _river-tag-overlay: https://git.sr.ht/~leon_plickat/river-tag-overlay
