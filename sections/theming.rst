Theming
-------

Use monokai_-pro palette while honouring :ref:`fade-in <background_fade>` if in
effect::

    (( $+commands[pastel] )) || riverctl background-color 0x1b1d1e
    riverctl border-color-focused 0xa6e22e
    riverctl border-color-unfocused 0x75715e
    riverctl border-color-urgent 0xf92672

.. todo::

    Theme definitions should *really* be configured more centrally, but for the
    time being it works.

.. _monokai: https://github.com/tanvirtin/monokai.nvim

.. spelling:word-list::

    Theming
    monokai
