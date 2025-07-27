Common applications
'''''''''''''''''''

Spawn a |foot| client instance::

    riverctl map normal Super Return spawn "footclient --no-wait"

Attempt to pick the most useful *to me* browser that is available::

    riverctl map normal Super Z spawn \
        "exec ${commands[firefox]:-${commands[chromium]:-sensible-browser}}"
