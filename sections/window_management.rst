Window management
-----------------

State bindings::

    riverctl map normal Super+Shift Return zoom
    riverctl map normal Super+Shift C close
    riverctl map normal Super+Shift 0 set-view-tags $ALL_TAGS

    riverctl map normal Super+Control Space toggle-float
    riverctl map normal Super F toggle-fullscreen

Navigation bindings::

    riverctl map normal Super Tab focus-view next
    riverctl map normal Super+Shift Tab focus-view previous

    riverctl map normal Super+Control Tab swap next
    riverctl map normal Super+Control+Shift Tab swap previous

Output bindings::

    riverctl map normal Super+Shift Page_up send-to-output next
    riverctl map normal Super+Shift Page_down send-to-output previous

.. spelling:word-list::

    fullscreen
