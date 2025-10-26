Run background services
-----------------------

I manage all my background services with a |systemd| user session.
:program:`systemd` handles all the gory details of process supervision, so that
— for example — you don't need to implement your own hot reloading for your
status script.

The interesting thing to notice below is that I use instances keyed off of
:envvar:`WAYLAND_DISPLAY` so that it is possible to run multiple sessions, which
comes in handy for testing as you can simply start a new nested session.

Start |foot| server::

    systemctl --user start foot-server@$WAYLAND_DISPLAY.socket

Start |sandbar|::

    systemctl --user start sandbar@$WAYLAND_DISPLAY.socket
    sandbar_pipe=$(find_socket sandbar)
    systemctl --user start sandbar_status@$WAYLAND_DISPLAY

.. note::

    We fetch the :program:`sandbar` socket location so that we can issue
    commands to it from within the startup file.

Start |swayidle|::

    systemctl --user start swayidle@$WAYLAND_DISPLAY

Start |river-ultitile|::

    systemctl --user start river-ultitile@$WAYLAND_DISPLAY

Start |wob|::

    systemctl --user start wob@$WAYLAND_DISPLAY.socket
    wob_pipe=$(find_socket wob)

.. note::

    We fetch the socket location so that we can use it for a :ref:`progress bar
    within this file <progress_bar>`.

Start |river-tag-overlay|::

    systemctl --user start river-tag-overlay@$WAYLAND_DISPLAY
