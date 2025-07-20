Mouse bindings
--------------

Configure “standard” mouse bindings::

    riverctl map-pointer normal Super BTN_LEFT move-view
    riverctl map-pointer normal Super BTN_RIGHT resize-view

It is nice to have a simple way to flip the float bit on a window::

    riverctl map-pointer normal Super BTN_MIDDLE toggle-float

Using back and forward to manipulate the stack feels really quite natural::

    riverctl map-pointer normal Super BTN_FORWARD swap next
    riverctl map-pointer normal Super BTN_BACK swap previous

… and by extension back and forward to shuffle across outputs works well::

    riverctl map-pointer normal Super+Shift BTN_FORWARD send-to-output next
    riverctl map-pointer normal Super+Shift BTN_BACK send-to-output previous
