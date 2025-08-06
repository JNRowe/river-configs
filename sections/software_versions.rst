Software versions
-----------------

===================  ===============================
Package              Version
===================  ===============================
|foot|               ``1.21.0``
|river|              ``0.3.0+git91~g82cbe78`` [#s1]_
|river-tag-overlay|  ``1.0.0+git16~g11d2dc4``
|sandbar|            ``0.1+git36~gf080371`` [#s2]_
|swayidle|           ``1.8.0``
|wideriver|          ``1.2.0+git35~g8c25ebf`` [#s2]_
|wob|                ``0.16+git14~g0a6ba9b``
===================  ===============================

.. note::

    These are the base versions from upstream, there may be local additions
    exposed in the installation packages.  However, they will *not* introduce
    breaking changes.

.. rubric:: Footnotes

.. [#s1] I've added some largely uninteresting local changes from upstream, I'm
         purposely not changing anything in the hope I can smoothly transition
         to an official Debian package at some point.

.. [#s2] Beyond packaging changes there are only light hacks to use `Nerd
         Fonts`_ for icons.

.. _wlroots: https://gitlab.freedesktop.org/wlroots/wlroots
.. _nerd fonts: https://www.nerdfonts.com/
