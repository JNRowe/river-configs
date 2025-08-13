Main logic
==========

This section handles command-line argument parsing and the main execution flow.

.. code:: zsh

    typeset -A args
    zparseopts -D -K -E -A args d: h

    if [[ -n ${args[(I)-h]} ]] {
        print -P "Usage: %B$0%b [option…] <input> <output>"
        echo "Options:"
        echo "    -d <file>  File to write dependencies to"
        echo "    -h         This message"
        exit 0
    } elif [[ -z ${1:-} ]] {
        echo "Error: No input given"
        exit 2
    } elif [[ -z ${2:-} ]] {
        echo "Error: No output given"
        exit 2
    }

Thanks to :program:`zsh`'s ``-U`` flag we can ignore duplicate includes, and
simply let :command:`zsh` uniquify our array::

    typeset -U includes=()

This is the meat of the user interface; we simply call :ref:`parse
<parse_function>`::

    integer block_count=0
    parse $1 $2

.. note::

    The use of ``block_count`` here is a code smell, but I'm unable to figure
    out a clean way to handle the output effect without a *little* state
    spilling out.

If the user asked for a dependency list we'll write it out.  We use a standard
:program:`make` syntax, as it is widely understood and directly supported with
ninja_

::

    [[ -n ${args[(I)-d]} ]] && echo $2: $0 $1 $includes >| ${args[-d]}

If we've reached this far exit with ``0``.  This mainly exists so we never need
to worry about a dangling conditional causing failures if this script is
extended. 

::

    :

.. _ninja: https://ninja-build.org/

.. spelling:word-list::

    uniquify
