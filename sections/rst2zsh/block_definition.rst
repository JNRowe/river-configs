Block definition
================

The ``start_block`` variable defines the regular expression used to identify the
start of a code block:

===========================  ============================================
Regular expression           Description
===========================  ============================================
:regexp:`^::$`               Literal block, which for the sake of this
                             repository is always ``zsh``
:regexp:`^\.\. code:: zsh`   :program:`zsh` code block
:regexp:`^[^\. ][^\.].*::$`  Implied code block via ``::`` suffixed line,
                             skipping lines that are :abbr:`reST
                             (reStructuredText)` directives
===========================  ============================================

.. code:: zsh

    start_block='^(::|\.\. code:: zsh|[^\. ][^\.].*::)$'
