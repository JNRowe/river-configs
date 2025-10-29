Setup
=====

We're going to use |zsh| as it is *always* available on any system I use::

    #! /bin/zsh -f

.. note::

    The ``-f`` option protects us from adverse interactions in the user's
    :program:`zsh` configuration files.  They *shouldn't* cause problems, but
    this build is part of an installation process that occurs *before*
    :program:`zsh` configuration is necessarily complete.

We'll want stricter defaults out of the box:

=======================  ===================================================
Option                   Description
=======================  ===================================================
``err_exit``             Exit immediately if a command exits with a non-zero
                         status.
``no_unset``             Treat unset variables as an error.
``warn_create_global``   Warn when a global variable is created.
=======================  ===================================================

::

    setopt err_exit no_unset warn_create_global

We'll need zutil_ to allow us to process command line arguments::

    zmodload -F zsh/zutil +b:zparseopts

.. _zutil: https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html#The-zsh_002fzutil-Module
