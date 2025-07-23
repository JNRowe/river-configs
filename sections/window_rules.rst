Window rules
------------

Allow window tearing if requested by the application::

    riverctl allow-tearing enabled

Sloppy focus is the *only* focus model that makes any sense to me::

    riverctl focus-follows-cursor normal

Allow some rules to be stored outside default init to make it easier to share
across different machines.  For example, I *need* conflicting rules for outputs
depending on location.

::

    [[ -f $0:a:h/local_rules ]] && source $0:a:h/local_rules

Decades of use at this point means I always like the “second” tag — or workspace
2 for non-tagging interfaces — to contain a browser by default::

    riverctl rule-add -app-id "chromium" tags $(tag_mask 2)
    riverctl rule-add -app-id "firefox" tags $(tag_mask 2)

I treat the “third” tag as media zone by default::

    riverctl rule-add -app-id "mpv" tags $(tag_mask 3)

.. todo::

    It may make more sense to use a custom application identifier for the
    default apps, so that we can push them to their common tags but keep regular
    instances attached to current tag.

.. spelling:word-list::

   Todo
   init
   todo
