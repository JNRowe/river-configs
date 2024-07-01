river-configs
=============

.. epigraph::

   So, imagine your workmate has created a new tool that *requires* Wayland…

This is my personal river_ configuration that is shared among hosts.  Maybe
they’re useful to you too, or — better yet — you’ll spot *and* fix a bug!

.. note::

    I’m writing this for myself as a |WIP| notebook.  Expect foolish — or even
    downright ignorant — errors and omissions.  Feel free to `drop me a note`_
    for clarifications or to fix my invalid assumptions.

This is in a very early state; basically the result of needing to get up and
running quickly, without breaking my workflow too much.  I haven’t decided on a
lot of things yet, so don’t expect this to work for you *or* remain as-is for
long.

Software
--------

``river`` (replacing ``awesomewm``/``dwm``)
'''''''''''''''''''''''''''''''''''''''''''

``river`` is definitely the only choice I’m comfortable with right now.  The
other tiling managers are either a little raw(dwl_) or very weak(sway_).  If the
setup changes it will be toward ``dwl`` or something that more closely resembles
awesomewm_.

What I want:

=======  =====================================================================
Feature  Reason
=======  =====================================================================
tags     Workspaces are an anaemic stub of a feature when you’re used to tags
dynamic  If I wanted to manage windows by hand I wouldn’t use a tiling manager
layouts  Some tags should be tiled in fancy directions, some should be monocle
…        <things I depend on but haven’t noticed yet>
=======  =====================================================================

wideriver_ is a great layout engine, providing the main layouts I rely on.
I may well end up changing to one of the scriptable replacements at some point
though, both river-luatile_ and riverguile_ look enticing.

The main thing I’m missing right now is per-tag default layouts, but you can
work around that by issuing a heap of commands at startup(before any views are
created to prevent flicker).

Other candidates
^^^^^^^^^^^^^^^^

``dwl`` is close to perfect as a dwm_ replacement, but there a few rough edges
that need ironing out.  I’d recommend it to others who want a ``dwm``
experience.

``sway`` is popular with lots of support, but fails on every count.  Its
workspace implementation is ferociously under-featured.  Its layout splitting
feels like a chore.  Custom layouts require endless scripting after making
everything float.  Even seemingly simple things like window switching across
branches become a chore requiring heaps of code, even including implementing
locks to make sure keys aren’t swallowed when you execute commands quickly.


vivarium_ feels very promising.  It features most of the layouts I’ve become
accustomed to, but its stability wasn’t great for me.

``foot`` (replacing ``alacritty``)
''''''''''''''''''''''''''''''''''

foot_ is amazing.  If I’d known it was available before it may have been the
catalyst for me to move to Wayland before now.  Something *unknowingly amazing*
would have to arrive for this not to be the choice going forward.

``sandbar`` (replacing built-in ``awesomewm``/``dwm`` functionality)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

sandbar_ does pretty much exactly what I want from a bar.  I’m going to miss how
integrated the ``wibox`` is in ``awesomewm``, but I’m comfortable enough making
the widgets I *really* care about work with ``sandbar``.

``wob`` (replacing ``dzen2``)
'''''''''''''''''''''''''''''

wob_ is simple little progress bar tool, that can replace a fair chunk of my
dzen2_ usage.  It isn’t featureful enough *by design* to be a full replacement,
but it remains to be seen how much I’ll miss the hover popups or context hints
that come with accompanying text.

.. _river: https://codeberg.org/river/river
.. _dwl: https://codeberg.org/dwl/dwl.git
.. _sway: https://github.com/swaywm/sway/
.. _wideriver: https://github.com/alex-courtis/wideriver
.. _river-luatile: https://github.com/MaxVerevkin/river-luatile
.. _riverguile: https://git.sr.ht/~leon_plickat/riverguile
.. _awesomewm: https://awesomewm.org/
.. _foot: https://codeberg.org/dnkl/foot
.. _sandbar: https://github.com/kolunmi/sandbar
.. _wob: https://github.com/francma/wob
.. _drop me a note: mailto:jnrowe@gmail.com
.. _dzen2: https://github.com/robm/dzen
.. _dwm: http://dwm.suckless.org/
.. _vivarium: https://github.com/inclement/vivarium

.. |WIP| raw:: html

    <abbr title="Work In Progress">WIP</abbr>
