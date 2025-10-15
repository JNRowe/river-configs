Utility functions
-----------------

Fetch socket path for |systemd| `.socket units`_::

    find_socket() {
        local listen
        for _ ({1..10}) {
            listen=$(systemctl --user show $1@$WAYLAND_DISPLAY.socket --property=Listen 2>/dev/null)
            if [[ -n $listen && $listen != Listen= ]] {
                echo ${${listen#*=}%% *}
                return
            }
            zselect -t 10 || :
        }
        print -u2 "Could not find socket for ‘$1’ after 1s"
        return 1
    }

.. _progress_bar:

Populate a |wob| progress bar, if possible, as we move through :file:`init`::

    LINES=${#${(@f)"$(< $0)"}}
    _progress() {
        setopt local_options no_xtrace
        [[ -z ${wob_pipe:-} ]] && return
        float line=${funcfiletrace[1]##*:}
        integer pcnt=$(((line - 1) / LINES * 100))
        echo $pcnt >>$wob_pipe
    }
    add-zsh-hook preexec _progress

Although startup is quick enough that a progress marker isn't strictly
necessary, it serves as a useful smoketest, quickly highlighting configuration
errors if the progress bar fails to reach the end.  Also — and I will be honest
— it felt like a fun hack.

.. note::

    This does not strictly require :ref:`add_zsh_hook <add_zsh_hook>`, but I
    prefer the interface offered by it over simply setting the hook by hand.

Calculate a tag mask given a list of tags::

    tag_mask() {
        integer r n
        for n ($@) {
            r+=$((1 << (n-1)))
        }
        echo $r
    }
    ALL_TAGS=$(tag_mask {1..32})

.. _.socket units: https://www.freedesktop.org/software/systemd/man/latest/systemd.socket.html

.. spelling:word-list::

    smoketest
