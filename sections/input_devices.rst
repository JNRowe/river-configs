Input devices
-------------

Wait 300 milliseconds and then repeat keys 50 times per second::

    riverctl set-repeat 50 300

Configure non-standard `options for keyboard`_::

    declare -A _xkb_opts=(
        [caps]=escape_shifted_capslock
        [compose]=paus
        [keypad]=future
        [parens]=swap_brackets
    )
    xkb_opts_full=${(kj:,:)_xkb_opts/(#m)*/$MATCH:$_xkb_opts[$MATCH]}

.. note::

    The globbing flags used here require :ref:`extended globbing
    <extended_glob>`.

Perhaps those `obscure keyboard options`_ deserve an explanation:

===========================  ==================================================
Option                       Description
===========================  ==================================================
``escape_shifted_capslock``  Make :kbd:`Capslock`` an alternative :kbd:`Escape`
                             key, but keep :kbd:`Capslock` available with
                             :kbd:`Shift+Capslock`
``paus``                     Use :kbd:`Pause` as `compose key`_
``future``                   Unicode mathematics operators, noting that ASCII
                             operators already exist on the main section
``swap_brackets``            Swap square bracket and parenthesis position
===========================  ==================================================

Configure a subset without bracket swaps for editing square bracket heavy code::

    _xkb_opts_toggle=(parens)
    xkb_opts_toggle=${(kj:,:)${(k)_xkb_opts:|_xkb_opts_toggle}/(#m)*/$MATCH:$_xkb_opts[$MATCH]}

Default to ``swap_brackets`` behaviour::

    riverctl keyboard-layout -options $xkb_opts_full gb

Configure host specific touchpad settings::

    if [[ $HOST =~ ^(camille|corale)$ ]] {
        riverctl input pointer-2-14-ETPS/2_Elantech_Touchpad tap enabled
        riverctl input pointer-2-14-ETPS/2_Elantech_Touchpad pointer-accel 0.8
    }

We'll declare a mode to wrap our input bindings, mainly as their use is uncommon
and we won't lose a lot of keys this way::

    riverctl declare-mode input
    riverctl map normal Super I enter-mode input
    riverctl map input None Escape enter-mode normal

    if [[ $HOST =~ ^(camille|corale)$ ]] {
        riverctl map input None T input pointer-2-14-ETPS/2_Elantech_Touchpad \
            events disabled
        riverctl map input Shift T input pointer-2-14-ETPS/2_Elantech_Touchpad \
            events enabled
    }
    riverctl map input None K spawn "riverctl keyboard-layout \
        -options $xkb_opts_full gb"
    riverctl map input Shift K spawn "riverctl keyboard-layout \
        -options $xkb_opts_toggle gb"

.. _options for keyboard: https://www.freedesktop.org/wiki/Software/XKeyboardConfig/
.. _obscure keyboard options: https://xkcd.com/1806/
.. _compose key: https://en.wikipedia.org/wiki/Compose_key

.. spelling:word-list::

    globbing
    touchpad
