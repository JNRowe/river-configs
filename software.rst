Software
========

``river`` (replacing ``awesomewm``/``dwm``)
-------------------------------------------

river_ is definitely the only choice I’m comfortable with right now.  The other
tiling managers are either a little raw(dwl_) or very weak(sway_).  If the setup
changes it will be toward ``dwl`` or something that more closely resembles
awesomewm_.

What I want:

=======  =====================================================================
Feature  Reason
=======  =====================================================================
tags     Workspaces are an anaemic stub of a feature when you’re used to tags
dynamic  If I wanted to manage windows by hand I wouldn’t use a tiling manager
layouts  Some tags should be tiled in fancy patterns, some should be monocle
…        <things I depend on but haven’t noticed yet>
=======  =====================================================================

wideriver_ is a great layout engine, providing the main layouts I rely on.
I may well end up changing to one of the scriptable replacements at some point
though, both river-luatile_ and riverguile_ look enticing.

The main thing I’m missing right now is per-tag default layouts, but you can
work around that by issuing a heap of commands at startup(before any views are
created to prevent flicker).

Other candidates
''''''''''''''''

``dwl`` is close to perfect as a dwm_ replacement, but there a few rough edges
that need ironing out.  I’d recommend it to others who want a ``dwm``
experience.

``sway`` is popular with lots of support, but fails on every count for me.  Its
workspace implementation is ferociously under-featured.  Its layout splitting
feels like a chore.  Custom layouts require endless scripting after making
everything float.  Even seemingly simple things like window switching across
branches tends toward drudgery requiring heaps of code, you’ll even need to
implement locking to make sure keys aren’t swallowed if you execute commands
quickly.

wayfire_ is very visually attractive and offers some basic tiling support.  If
you’re comfortable with ``sway`` then it is probably an excellent choice for a
more visually appealing desktop.  I do plan to keep an eye on it to see whether
tiling extension becomes more featureful.

vivarium_ feels very promising.  It features most of the layouts I’ve become
accustomed to, but its stability wasn’t great for me.

``foot`` (replacing ``alacritty``)
----------------------------------

foot_ is amazing.  If I’d known it was available before it may have been the
catalyst for me to move to Wayland before now.  Something *unimaginably amazing*
would have to arrive for this not to be the choice going forward.

I do miss ligatures, but not as much as I miss the clever prompt navigation or
output control when using other terminals.  Using a ligature supporting neovim_
frontend *might* be a reasonable compromise, as I only make significant use of
ligatures in editing sessions.

``sandbar`` (replacing built-in ``awesomewm``/``dwm`` functionality)
--------------------------------------------------------------------

sandbar_ does pretty much exactly what I want from a bar.  I’m going to miss how
integrated the ``wibox`` is in ``awesomewm``, but I’m comfortable enough making
the widgets I *really* care about work with ``sandbar``.

``wob`` (replacing ``dzen2``)
-----------------------------

wob_ is simple little progress bar tool, that can replace a fair chunk of my
dzen2_ usage.  It isn’t featureful enough *by design* to be a full replacement,
but it remains to be seen how much I’ll miss the hover popups or context hints
that come with accompanying text.

.. _river: https://codeberg.org/river/river
.. _dwl: https://codeberg.org/dwl/dwl.git
.. _sway: https://github.com/swaywm/sway/
.. _awesomewm: https://awesomewm.org/
.. _wideriver: https://github.com/alex-courtis/wideriver
.. _river-luatile: https://github.com/MaxVerevkin/river-luatile
.. _riverguile: https://git.sr.ht/~leon_plickat/riverguile
.. _dwm: http://dwm.suckless.org/
.. _wayfire: https://wayfire.org/
.. _vivarium: https://github.com/inclement/vivarium
.. _foot: https://codeberg.org/dnkl/foot
.. _neovim: https://neovim.io/
.. _sandbar: https://github.com/kolunmi/sandbar
.. _wob: https://github.com/francma/wob
.. _dzen2: https://github.com/robm/dzen
