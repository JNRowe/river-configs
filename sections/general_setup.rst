General setup
-------------

We're going to use zsh_ as it is *always* available on any system I use::

    #! /bin/zsh -x

.. note::

    The ``-x`` option gives us a low-cost, lazy logging mechanism for error
    reporting.  Output appears in river's log during the initial run and in the
    executing terminal for subsequent runs.

We'll want stricter defaults out of the box::

    setopt err_exit no_unset warn_create_global

.. _extended_glob:

… along with extended globs for better matching support::

    setopt extended_glob

We'll need zselect_ to allow us perform :manpage:`sleep(1)` without forks::

    zmodload -F zsh/zselect b:zselect

.. _add_zsh_hook:

``autoload`` functions we'll need later::

    autoload -Uz add-zsh-hook

.. _exit_trap:

Configure an exit handler to display a notification if this script doesn't
:ref:`exit cleanly <normal_exit>`::

    notify_cmd=${commands[fyi]:-$commands[notify-send]}
    if [[ -n $notify_cmd ]] {
        trap $notify_cmd' --app-name river --urgency critical --icon=error "River: Unexpected exit in init" "Around line $LINENO"' EXIT
    } else {
        print -u2 "Warning: Unable to configure visual error notification"
    }

.. _background_fade:

Attempt to fade_ background from river default to my :doc:`preferred
colourscheme <theming>`::

    () {
        setopt local_options no_xtrace
        if (( $+commands[pastel] )) {
            local steps=($(pastel gradient --number 20 'rgb(0,43,54)' 'rgb(27,29,30)' |
                pastel format hex))
            local colour
            for colour (${steps/\#/0x}) {
                riverctl background-color $colour
                zselect -t 10 || :
            }
        }
    } &

.. _zsh: https://www.zsh.org/
.. _zselect: https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html#The-zsh_002fzselect-Module
.. _fade: https://github.com/sharkdp/pastel
