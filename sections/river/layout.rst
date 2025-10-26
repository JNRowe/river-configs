Layout
------

|rivercarro| is the layout engine that is the closest match to the behaviour I'm
used to with |awesomewm|, and makes a great default::

    riverctl default-layout rivercarro

We'll declare a layout mode to make it quicker — and easier on the hands — to
cycle layout controls when trying to pin down a comfortable setup::

    riverctl declare-mode layout
    riverctl map normal Super L enter-mode layout
    riverctl map layout None Escape enter-mode normal

Layout format manipulation bindings::

    riverctl map layout None M send-layout-cmd rivercarro "main-location monocle"
    riverctl map layout None T send-layout-cmd rivercarro "main-location left"
    riverctl map layout Control T send-layout-cmd rivercarro "main-location right"

Main window ratio manipulation bindings::

    riverctl map layout None Equal send-layout-cmd rivercarro "main-ratio 0.52"
    riverctl map layout None H send-layout-cmd rivercarro "main-ratio +0.05"
    riverctl map layout None L send-layout-cmd rivercarro "main-ratio -0.05"

Bindings to adjust the number of windows in main stack::

    riverctl map layout Shift Equal send-layout-cmd rivercarro "main-count 1"
    riverctl map layout Shift H send-layout-cmd rivercarro "main-count +1"
    riverctl map layout Shift L send-layout-cmd rivercarro "main-count -1"

Add top level bindings for monocle and tile-left, as they're my most common
layouts that I want quick access to::

    riverctl map normal Super M send-layout-cmd rivercarro "main-location monocle"
    riverctl map normal Super T send-layout-cmd rivercarro "main-location left"

Configure initial per-tag layouts::

    for n ({2..32..2}) {
        riverctl set-focused-tags $(tag_mask $n)
        riverctl send-layout-cmd rivercarro "main-location monocle"
    }
    riverctl set-focused-tags $(tag_mask 1)

.. note::

    This reflects — what is at this point — my decades-old tradition of
    defaulting to fullscreen on even tags.  While it may not make sense, it is a
    deeply ingrained habit.

.. spelling:word-list::

    fullscreen
