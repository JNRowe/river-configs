Floating support
''''''''''''''''

::

    ARROW_KEYS=(Left Down Up Right)

Declare floating mode::

    riverctl declare-mode float
    riverctl map normal Super R enter-mode float
    riverctl map float None Escape enter-mode normal

.. note::

    We declare a full mode here to make large scale changes to windows easier to
    accomplish.  For quick changes all the modifiers aren’t a problem, but big
    changes are easier in the dedicated mode.

Basic movement bindings::

    for key ($ARROW_KEYS) {
        riverctl map normal Super+Alt $key move $key:l 100
        riverctl map float None $key move $key:l 100
    }

Cardinal movement bindings::

    for key ($ARROW_KEYS) {
        riverctl map normal Super+Alt+Control $key snap $key:l
        riverctl map float Control $key snap $key:l
    }

Basic resizing bindings::

    xs=(horizontal vertical)
    integer i=0 delta
    for key dir (${ARROW_KEYS:^^xs}) {
        delta=$((i++ % 2 ? 1 : -1))00
        riverctl map normal Super+Alt+Shift $key resize $dir $delta
        riverctl map float Shift $key resize $dir $delta
    }

.. spelling:word-list::

    aren
