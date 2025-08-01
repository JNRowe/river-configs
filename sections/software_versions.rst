Software versions
-----------------

===================  ===============================
Package              Version
===================  ===============================
|foot|               ``1.21.0``
|river|              ``0.3.0+git76~gbe7c6dc`` [#s1]_
|river-tag-overlay|  ``1.0.0``
|sandbar|            ``0.1+git23~g0e942af`` [#s2]_
|swayidle|           ``1.8.0``
|wideriver|          ``1.2.0+git20~ge4d64c0`` [#s2]_
|wob|                ``0.14.2``
===================  ===============================

.. note::

    These are the base versions from upstream, there may be local additions
    exposed in the installation packages.  However, they will *not* introduce
    breaking changes.

.. rubric:: Footnotes

.. [#s1] I've added some largely uninteresting local changes from
         ``v0.3.0-39-gccd676e``, but mostly it is because there is no timeline
         for wlroots_ ``v0.18`` hitting my installations.

.. [#s2] Beyond packaging changes there are only light hacks to use `Nerd
         Fonts`_ for icons.

.. _wlroots: https://gitlab.freedesktop.org/wlroots/wlroots
.. _nerd fonts: https://www.nerdfonts.com/
