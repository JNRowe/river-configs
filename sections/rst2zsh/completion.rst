Completion
==========

A simple completion to make life a little easier.

.. code:: zsh

    #compdef rst2zsh

    _arguments \
        {-d,--depfile}'[File to write dependencies to]:_files' \
        {-h,--help}'[This message]' \
        '1:input file:_files' \
        '2:output file:_files'
