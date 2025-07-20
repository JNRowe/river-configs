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

.. _zsh: https://www.zsh.org/
