Finalising
----------

Allow a private machine specific configuration to be loaded::

    [[ -f $0:a:h/local_init ]] && source $0:a:h/local_init

Show |sandbar|::

    echo all show >>$sandbar_pipe

.. note::

    ``sandbar`` is spawned hidden to prevent bar flashes when issuing per-tag
    layout changes or launching default applications.

Wait for any background jobs to complete::

    wait

.. _normal_exit:

Exit without triggering :ref`error exit notification <exit_trap>`::

    exec :
