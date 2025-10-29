Setup
=====

We're going to use |zsh| as it is *always* available on any system I use::

    #! /bin/zsh

We'll want stricter defaults out of the box:

=======================  ===================================================
Option                   Description
=======================  ===================================================
``err_exit``             Exit immediately if a command exits with a non-zero
                         status.
``no_clobber``           Don’t allow ``>`` to truncate files
``no_unset``             Treat unset variables as an error.
``warn_create_global``   Warn when a global variable is created.
=======================  ===================================================

::

    setopt err_exit no_clobber no_unset warn_create_global

We'll need zutil_ to allow us to process command line arguments::

    zmodload -F zsh/zutil +b:zparseopts

.. _zutil: https://zsh.sourceforge.io/Doc/Release/Zsh-Modules.html#The-zsh_002fzutil-Module
