Glossary
========

.. glossary::

.. envvar:: WAYLAND_DISPLAY

    Identifies the compositor to connect to, making it possible to interact
    with more than one at a time.

.. envvar:: XDG_CURRENT_DESKTOP

    Identifies the current desktop environment, used by the `desktop entry
    specification`_ for example.

.. envvar:: XDG_SESSION_DESKTOP

    Similar to :envvar:`XDG_CURRENT_DESKTOP`, but some software that relies on
    |systemd| requires this setting_.

.. _desktop entry specification: https://specifications.freedesktop.org/desktop-entry-spec/
.. _setting: https://www.freedesktop.org/software/systemd/man/latest/pam_systemd.html#%24XDG_SESSION_DESKTOP
