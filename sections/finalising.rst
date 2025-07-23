Finalising
----------

Allow a private machine specific configuration to be loaded::

    [[ -f $0:a:h/local_init ]] && source $0:a:h/local_init

Show ``sandbar``::

    echo all show >>$sandbar_pipe

.. note::

    ``sandbar`` is spawned hidden to allow us to issue per-tag layout changes or
    launch default applications without all the bar flashes that would result.

.. _normal_exit:

Exit without triggering :ref`error exit notification <exit_trap>`::

    exec :

.. _sandbar: https://github.com/kolunmi/sandbar
