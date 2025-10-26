Software
========

``river`` (replacing ``awesomewm``/``dwm``)
-------------------------------------------

|river| is definitely the only choice I'm comfortable with right now.  The other
tiling managers are either a little raw(dwl_) or very weak(sway_).  If the setup
changes it will be toward :program:`dwl` or something that more closely
resembles |awesomewm|.

.. tip::

    |river| is in a state of flux right now.  The `main repository`_ on Codeberg
    is to become a staging area for the ``river`` rewrite, with the original
    river code continuing development in ``river-classic``.  This configuration
    targets ``river-classic`` now, you can check :doc:`specific versions
    <sections/river/software_versions>` to see what is supported.

What I want:

=======  =====================================================================
Feature  Reason
=======  =====================================================================
tags     Workspaces are an anaemic stub of a feature when you're used to tags
dynamic  If I wanted to manage windows by hand I wouldn't use a tiling manager
layouts  Some tags should be tiled in fancy patterns, some should be monocle
…        <things I depend on but haven't noticed yet>
=======  =====================================================================

|rivercarro| is a great layout engine, providing the main layouts I rely on.
I may well end up changing to one of the scriptable replacements at some point
though, both river-luatile_ and riverguile_ look enticing.

While per-tag default layouts are currently absent, this can be mitigated by
executing commands at startup before any views are created to prevent flicker.

Other candidates
''''''''''''''''

:program:`dwl` is a near-perfect dwm_ replacement, though it still has some
rough edges.  I'd recommend it to others who want a :program:`dwm` experience.

:program:`sway`, despite its popularity and extensive user support, falls short
on every count for me.  Its workspace implementation is ferociously
under-featured, and its layout splitting is cumbersome.  Custom layouts require
extensive scripting after making everything float.  Even seemingly simple tasks,
such as window switching across branches, become tedious, often requiring
significant code.  You'll even find yourself having to implement locking
mechanisms to prevent key swallowing during rapid command execution.

wayfire_ is visually appealing and offers basic tiling.  It is a good choice for
users comfortable with :program:`sway` who desire a more visually engaging
desktop. I do plan to keep an eye on it to see whether tiling extension becomes
more featureful.

vivarium_ shows promise, featuring most of my accustomed layouts, but its
stability has been an issue for me in testing.

``foot`` (replacing ``alacritty``)
----------------------------------

|foot| is amazing.  If I'd known it was available before it may have been the
catalyst for me to move to Wayland before now.  Something *unimaginably amazing*
would have to arrive for this not to be the choice going forward.

I do miss ligatures, but not as much as I miss the clever prompt navigation or
output control when using other terminals.  Using a ligature supporting neovim_
frontend *might* be a reasonable compromise, as I only make significant use of
ligatures in editing sessions.

``sandbar`` (replacing built-in ``awesomewm``/``dwm`` functionality)
--------------------------------------------------------------------

|sandbar| does pretty much exactly what I want from a bar.  I'm going to miss
how integrated the wibox_ is in :program:`awesomewm`, but I'm comfortable enough
making the widgets I *really* care about work with, or alongside,
:program:`sandbar`.

``wob`` (replacing ``dzen2``)
-----------------------------

|wob| is a simple progress bar tool that can replace much of my dzen2_ usage.
By design, it is not feature-rich enough to be a complete replacement, but it
remains to be seen how much I will miss the hover popups or context hints that
accompany text.

.. _dwl: https://codeberg.org/dwl/dwl
.. _main repository: https://codeberg.org/river/river
.. _sway: https://github.com/swaywm/sway/
.. _river-luatile: https://github.com/MaxVerevkin/river-luatile
.. _riverguile: https://git.sr.ht/~leon_plickat/riverguile
.. _dwm: http://dwm.suckless.org/
.. _wayfire: https://wayfire.org/
.. _vivarium: https://github.com/inclement/vivarium
.. _neovim: https://neovim.io/
.. _wibox: https://awesomewm.org/doc/api/classes/wibox.html
.. _dzen2: https://github.com/robm/dzen

.. spelling:word-list::

    Codeberg
    Wayland
    Workspaces
    featureful
    frontend
    popups
    scriptable
