#
"""conf - Sphinx configuration information."""

import os
import importlib.util
from subprocess import check_output

on_github = "GITHUB_ACTIONS" in os.environ

# General configuration {{{
extensions: list[str] = [
    f"sphinx.ext.{ext}"
    for ext in [
        "duration",
        "ifconfig",
        "todo",
    ]
] + [
    "sphinx_rtd_theme",
]
if importlib.util.find_spec("sphinxcontrib.spelling"):
    extensions.append("sphinxcontrib.spelling")

# Including a central list of common URLs here a far cleaner way to handle
# duplication.
rst_epilog = """
.. |awesomewm| replace:: `awesomewm <https://awesomewm.org/>`__
.. |foot| replace:: `foot <https://codeberg.org/dnkl/foot>`__
.. |river-tag-overlay| replace:: `river-tag-overlay <https://git.sr.ht/~leon_plickat/river-tag-overlay>`__
.. |river| replace:: `river <https://codeberg.org/river/river-classic>`__
.. |sandbar| replace:: `sandbar <https://github.com/kolunmi/sandbar>`__
.. |swayidle| replace:: `swayidle <https://github.com/swaywm/swayidle>`__
.. |systemd| replace:: `systemd <https://systemd.io>`__
.. |wideriver| replace:: `wideriver <https://github.com/alex-courtis/wideriver>`__
.. |wob| replace:: `wob <https://github.com/francma/wob>`__
.. |zsh| replace:: `zsh <https://www.zsh.org/>`__
"""

needs_sphinx = "8.2"

# While upstream uses this purely to enable reference warnings, we’ll use it as
# trigger for all configurable QA messages.
nitpicky = True

exclude_patterns: list[str] = [
    ".build",
    ".github",
    ".venv",
    "maybe",
    "README.rst",
]
# }}}

# Project information {{{
project = "river-configs"
author = "James Rowe"
copyright = f"2024-%Y  {author}"

if on_github:
    html_last_updated_fmt = (
        check_output([
            "git",
            "-C",
            os.path.dirname(__file__),
            "log",
            "--pretty=format:%ad [%h]",
            "--date=short",
            "-n1",
        ])
        .decode()
        .strip()
    )
else:
    # Use a static updated time to limit rebuilds for faster commit hooks
    html_last_updated_fmt = "[local build]"

release = html_last_updated_fmt
version = ""

trim_footnote_reference_space = True

manpages_url = "https://manpages.debian.org/{path}"
# }}}

# Options for HTML output {{{
html_theme = "sphinx_rtd_theme"
html_logo = ".images/logo.svg"

highlight_language = "zsh"

html_copy_source = False
# }}}

# Options for link check builder {{{
linkcheck_exclude_documents = ["todo.rst"]
# }}}

# spelling extension settings {{{
spelling_exclude_patterns = ["todo.rst"]
spelling_ignore_acronyms = False
spelling_lang = "en_GB"
spelling_ignore_python_builtins = False
spelling_ignore_importable_modules = False
spelling_warning = nitpicky
# Sadly, we can't use en_GB.UTF-8 to correct for Unicode quotes, because that is
# a site-local improvement
tokenizer_lang = "en_GB"
# }}}

# todo extension settings {{{
todo_include_todos = True
# }}}


def setup(app):
    # Make on_github available for ifconfig directive
    app.add_config_value("github_actions", on_github, "env")
