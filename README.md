# river-configs

> So, imagine your workmate has created a new tool that *requires* Wayland…

This is my personal [river] configuration that is shared among hosts.  Maybe
they’re useful to you too, or — better yet — you’ll spot *and* fix a bug!

---

*Note*: I’m writing this for myself as a work in progress notebook.  Expect
foolish — or even downright ignorant — errors and omissions.  Feel free to
[drop me a note] for clarifications or to fix my invalid assumptions.

---

This is in a very early state; basically the result of needing to get up and
running quickly, without breaking my workflow too much.  I haven’t decided on a
lot of things yet, so don’t expect this to work for you *or* remain as-is for
long.

## Software

### river (replacing `awesomewm`/`dwm`)

[river] is definitely the only choice I’m comfortable with right now.  The other
tiling managers are either a little raw([dwl]) or very weak([sway]).  If the
setup changes it will be toward `dwl` or something that more closely resembles
[awesomewm].

What I want:

|Feature|Reason                                                               |
|-------|---------------------------------------------------------------------|
|tags   |Workspaces are an anaemic stub of a feature when you’re used to tags |
|dynamic|If I wanted to manage windows by hand I wouldn’t use a tiling manager|
|layouts|Some tags should be tiled in fancy directions, some should be monocle|
|…      |\<things I depend on but haven’t noticed yet>                        |

[wideriver] is a great layout engine, providing the main layouts I rely on.
I may well end up changing to one of the scriptable replacements at some point
though, both [river-luatile] and [riverguile] look enticing.

The main thing I’m missing right now is per-tag default layouts, but you can
work around that by issuing a heap of commands at startup(before any views are
created to prevent flicker).

### foot (replacing `alacritty`)

[foot] is amazing.  If I’d known it was available before it may have been the
catalyst for me to move to Wayland before now.  Something *unknowingly amazing*
would have to arrive for this not to be the choice going forward.

### sandbar (replacing built-in `awesomewm`/`dwm` functionality)

[sandbar] does pretty much exactly what I want from a bar.  I’m going to miss
how integrated the `wibox` is in `awesomewm`, but I’m comfortable enough making
the widgets I *really* care about work with `sandbar`.

### wob (replacing `dzen2`)

[wob] is simple little progress bar tool, that can replace a fair chunk of my
[dzen2] usage.  It isn’t featureful enough *by design* to be a full replacement,
but it remains to be seen how much I’ll miss the hover popups or context hints
that come with accompanying text.

[river]: https://codeberg.org/river/river
[dwl]: https://codeberg.org/dwl/dwl.git
[sway]: https://github.com/swaywm/sway/
[wideriver]: https://github.com/alex-courtis/wideriver
[river-luatile]: https://github.com/MaxVerevkin/river-luatile
[riverguile]: https://git.sr.ht/~leon_plickat/riverguile
[awesomewm]: https://awesomewm.org/
[foot]: https://codeberg.org/dnkl/foot
[sandbar]: https://github.com/kolunmi/sandbar
[wob]: https://github.com/francma/wob
[drop me a note]: mailto:jnrowe@gmail.com
[dzen2]: https://github.com/robm/dzen

