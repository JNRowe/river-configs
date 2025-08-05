Config time
===========

.. ifconfig:: not github_actions

    .. tip::

        The `generated HTML`_ will likely be a better reading experience.

My |river| configuration is created by extracting the code blocks from within
this file. It sounds *far* more complex than it needs to be, but it fits in to
an elaborate ninja_ configuration that I use to generate my home directories.
The advantage *to me* is that I can mix-and-match software versions on different
machines, but it also means that the repository structure for individual
configurations looks overcomplicated from the outside.

.. tip::

    The output from ``tools/rst2zsh`` includes comment markers that can be used
    to navigate back to the source in this file.  For example, in vim_ calling
    ``gF`` will jump to the section under the cursor.

.. _generated HTML: https://jnrowe.github.io/river-configs/
.. _ninja: https://ninja-build.org/
.. _vim: https://www.vim.org/

Contents
--------

.. toctree::

    sections/software_versions
    sections/general_setup
    sections/utility_functions
    sections/configure_environment
    sections/run_background_services
    sections/keybindings
    sections/window_management
    sections/floating_support
    sections/common_applications
    sections/mouse_bindings
    sections/theming
    sections/input_devices
    sections/window_rules
    sections/layout
    sections/finalising

.. spelling:word-list::

    Config
    overcomplicated
