Config time
===========

.. ifconfig:: not github_actions

    .. note::

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

.. spelling:word-list::

    Config
    ninja
    overcomplicated
