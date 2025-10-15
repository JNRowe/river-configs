Parsing logic
=============

The ``parse`` function is the core of :command:`rst2zsh`.  It reads the input
file line by line, identifying code blocks, and extracting them to the output
file.  It also handles include_ and toctree_ directives to recursively parse
included files.

.. _parse_function:

.. code:: zsh

    parse() {
        readonly input=$1 output=$2

We need to know whether we are recursing at various points within this function,
this allows us to track it::

        integer _RST2HTML_recursing=${_RST2HTML_recursing:-0}

If this is our first entry into ``parse``, we'll truncate the output file::

        (( $_RST2HTML_recursing )) || : >| $output

Initialise values for our state machine::

        integer in_block=0 in_toctree=0

We keep track of the line number to allow us to create a source map to jump back
to :abbr:`reST (reStructuredText)` content when debugging output::

        integer line_nr=1

::

        local indent_prefix=""
        local line match
        integer mbegin mend
        while IFS='' read -r line; do
            (( line_nr++ ))
            if [[ $line =~ '^.. include:: (.*)' ]] {
                includes+=(${input:h}/$match)
                _RST2HTML_recursing=1 parse ${input:h}/$match $output
            } elif [[ $line =~ '^.. toctree::' ]] {
                in_toctree=1

We'll have indented filenames within toctree_ directive::

            } elif (( $in_toctree )) && [[ $line =~ '^[[:space:]]+([^ :].*)' ]] {
                includes+=(${input:h}/$match[1].rst)
                _RST2HTML_recursing=1 parse ${input:h}/$match[1].rst $output
            } elif [[ $line =~ $start_block ]] {
                (( ++block_count))
                in_block=1
                in_toctree=0

Reset indent for the new block::

                indent_prefix=""

Add source map, but not if we're at the very start of a non-recursive call.
The reason is that this would break the output if first line is a shebang.

::

                if [[ -s $output ]] {
                    echo "# $input:$line_nr" >> $output
                }
            } elif [[ $line =~ '^[^ ]' ]] {

When we leave the code block we need to reset our state::

                in_block=0
                in_toctree=0
            } elif (( $in_block )) && [[ -n $line ]] {
                if [[ -z $indent_prefix ]] {

Capture the indentation of the first line of the block::

                    [[ $line =~ '^([[:space:]]+)' ]] && indent_prefix=$match[1]
                }

Remove the indentation prefix from the line::

                if (( DYNAMIC_INDENT )) {
                    echo -E "${line#$indent_prefix}" >> $output
                } else {
                    echo -E "${line[5,-1]}" >> $output
                }
            }
        done < $input

.. note::

    We default to a strict four space removal unless the ``-i`` option is given
    even though it violates that reST specification, as our code blocks are
    only partial entities and dynamic whitespace removal breaks indentation in
    the final output.

Finally, if we're in the final call of ``parse`` we'll display the status of
this parsing run::

        if ! (( $_RST2HTML_recursing )) {
            if [[ ! -s $output ]] {
                print -u2 "Warning: No Zsh code blocks found in '$input'"
            } else {
                print -u2 "Extracted $block_count Zsh code blocks to '$output'"
            }
        }
    }

.. _include: https://docutils.sourceforge.io/docs/ref/rst/directives.html#include
.. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree

.. spelling:word-list::

    recursing
