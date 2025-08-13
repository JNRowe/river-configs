Configuration overview
======================

.. ifconfig:: not github_actions

    .. tip::

        The `generated HTML`_ will likely be a better reading experience.

My |river| configuration is created by extracting the code blocks from within
this file and its direct dependencies.  It sounds *far* more complex than it
needs to be, but it fits in to an elaborate ninja_ configuration that I use to
generate my home directories.  The advantage *to me* is that I can mix-and-match
software versions on different machines, but it also means that the repository
structure for individual configurations looks overcomplicated from the outside.

.. tip::

    The output from :command:`tools/rst2zsh` includes comment markers that can
    be used to navigate back to the source in this file.  For example, in vim_
    calling :kbd:`gF` will jump to the section under the cursor.

.. _generated HTML: https://jnrowe.github.io/river-configs/init.html
.. _ninja: https://ninja-build.org/
.. _vim: https://www.vim.org/

Contents
--------

.. toctree::

    sections/river/software_versions
    sections/river/general_setup
    sections/river/utility_functions
    sections/river/configure_environment
    sections/river/run_background_services
    sections/river/keybindings
    sections/river/window_management
    sections/river/floating_support
    sections/river/common_applications
    sections/river/mouse_bindings
    sections/river/theming
    sections/river/input_devices
    sections/river/window_rules
    sections/river/layout
    sections/river/finalising

.. spelling:word-list::

    Config
    overcomplicated
