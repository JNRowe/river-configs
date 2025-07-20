Utility functions
-----------------

Fetch socket path for systemd_ ``.socket`` units::

    find_socket() {
        systemctl --user show $1@$WAYLAND_DISPLAY.socket --property=Listen |
            sed 's,.*=\(.*\) .*,\1,'
    }

.. _progress-bar:

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

    This doesn’t strictly require :ref:`add_zsh_hook <add_zsh_hook>`, but I
    prefer the interface offered by it over simply setting the hook by hand.

Calculate a tag mask given a list of tags::

    tag_mask() {
        integer r n
        for n ($@) {
            r+=$((1 << (n-1)))
        }
        echo $r
    }
    ALL_TAGS=$((2**32 - 1))

.. _systemd: https://systemd.io
.. _wob: https://github.com/francma/wob

.. spelling:word-list::

    smoketest
