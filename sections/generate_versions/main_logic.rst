Main logic
==========

This section handles command-line argument parsing and the main execution flow::

    typeset -A args
    zparseopts -D -K -E -A args -M -- -help=h

    if [[ -n ${args[(I)-h]} ]] {
        print -P "Usage: %B$0%b [option…] <output>"
        echo "Options:"
        echo "    -h, --help                    This message"
        exit 0
    } elif [[ -z ${1:-} ]] {
        echo "Error: No output given"
        exit 2
    }

We wrap the main body in an `anonymous function`_ so that :program:`zsh` has a
scope with which to handle the temporary file we generate::

    () {
        readonly output=$1 tmp=$2

::

        local package version footnote

The generated :abbr:`CSV (Comma-Separated Values)` has two columns: package
name, and package version.

::

        print '"Package","Version"' >> $tmp

Loop over the defined packages and extract the installed version::

        for package ($packages) {
            version=$(dpkg-query -W -f='${Version}' $package)

.. note::

    At some point this won't be enough, but for now relying on
    :command:`dpkg-query` Works For Me™.

Append footnote references to version string, if required::

            footnote=${footnotes[$package]:-}
            if [[ $footnote ]] {
                footnote=" [#s$footnote]_"
            }

Write out the row::

            printf '"|%s|","``%s``%s"\n' $package $version $footnote >> $tmp
        }

Atomically replace output file::

        mv $tmp $output

Pass the output name and a temporary file to the function::

    } $1 =(:)

.. _anonymous function: https://zsh.sourceforge.io/Doc/Release/Functions.html#Anonymous-Functions
