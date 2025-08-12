:program:`rst2zsh` script
=========================

.. ifconfig:: not github_actions

    .. tip::

        The `generated HTML`_ will likely be a better reading experience.

This script is used to extract :program:`zsh` code from the ``.rst`` files in
this repository.  It is the key part of the ninja_ build process that assembles
the configuration from the documentation in this repository.

The script is built from the sections below.

.. _generated HTML: https://jnrowe.github.io/river-configs/rst2zsh.html
.. _ninja: https://ninja-build.org/

Contents
--------

.. toctree::

    sections/rst2zsh/setup
    sections/rst2zsh/block_definition
    sections/rst2zsh/parse_function
    sections/rst2zsh/main_logic
