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

.. _freedesktop.org: https://freedesktop.org
.. _dbus: https://dbus.freedesktop.org/
.. _systemd: https://systemd.io
