River Configurations
====================

.. epigraph::

   So, imagine your workmate has created a new tool that *requires* Wayland…

This is my personal |river| configuration that is shared among hosts.  Maybe
they’re useful to you too, or — better yet — you’ll spot *and* fix a bug!

.. note::

    I’m writing this for myself as a |WIP| notebook.  Expect foolish — or even
    downright ignorant — errors and omissions.  Feel free to `drop me a note`_
    for clarifications or to fix my invalid assumptions.

This is in a very early state; basically the result of needing to get up and
running quickly, without breaking my workflow too much.  I haven’t decided on a
lot of things yet, so don’t expect this to work for you *or* remain as-is for
long.

*Update from 2024-11-26*: I’ve been using ``river`` in this configuration since
July as my main environment, and it has been great!  There are few changes I
need to merge back in to this *public* repository, and a few things I need to
flesh out so that they’ll make sense when I come back to them.

Contents
--------

.. toctree::
    :maxdepth: 2

    software
    init
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
    todo

.. _drop me a note: mailto:jnrowe@gmail.com

.. |WIP| raw:: html

    <abbr title="Work In Progress">WIP</abbr>

.. spelling:word-list::

    Wayland

.. _river: https://codeberg.org/river/river
