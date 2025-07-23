Layout
------

wideriver_ is the layout engine that is the closest match to the behaviour I’m
used to with awesomewm_, and makes a great default::

    riverctl default-layout wideriver

We’ll declare a layout mode to make it quicker — and easier on the hands — to
cycle layout controls when trying to pin down a comfortable setup::

    riverctl declare-mode layout
    riverctl map normal Super L enter-mode layout
    riverctl map layout None Escape enter-mode normal

Layout format manipulation bindings::

    riverctl map layout None M send-layout-cmd wideriver "--layout monocle"
    riverctl map layout None T send-layout-cmd wideriver "--layout left"
    riverctl map layout Shift T send-layout-cmd wideriver "--layout wide"
    riverctl map layout Control T send-layout-cmd wideriver "--layout right"
    riverctl map layout None Space send-layout-cmd wideriver "--layout-toggle"

Layout style manipulation bindings::

    riverctl map layout None E send-layout-cmd wideriver "--stack even"
    riverctl map layout None W send-layout-cmd wideriver "--stack dwindle"
    riverctl map layout None I send-layout-cmd wideriver "--stack diminish"

Main window ratio manipulation bindings::

    riverctl map layout None Equal send-layout-cmd wideriver "--ratio 0.52"
    riverctl map layout None H send-layout-cmd wideriver "--ratio +0.05"
    riverctl map layout None L send-layout-cmd wideriver "--ratio -0.05"

Bindings to adjust the number of windows in main stack::

    riverctl map layout Shift Equal send-layout-cmd wideriver "--count 1"
    riverctl map layout Shift H send-layout-cmd wideriver "--count +1"
    riverctl map layout Shift L send-layout-cmd wideriver "--count -1"

Add top level bindings for monocle and tile-left, as they’re my most common
layouts that I want quick access to::

    riverctl map normal Super M send-layout-cmd wideriver "--layout monocle"
    riverctl map normal Super T send-layout-cmd wideriver "--layout left"

Configure initial per-tag layouts::

    for n ({2..32..2}) {
        riverctl set-focused-tags $(tag_mask $n)
        riverctl send-layout-cmd wideriver "--layout monocle"
    }
    riverctl set-focused-tags $(tag_mask 1)

.. note::

    This reflects — what is at this point — my *decades* old tradition of
    defaulting to fullscreen on even tags.  It doesn’t really make sense, but
    I’m quite accustomed to it.

.. _wideriver: https://github.com/alex-courtis/wideriver
.. _awesomewm: https://awesomewm.org/

.. spelling:word-list::

    doesn
    fullscreen
