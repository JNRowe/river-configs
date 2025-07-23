#
"""conf - Sphinx configuration information."""

import os
from contextlib import suppress
from subprocess import CalledProcessError, PIPE, run

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
    "sphinxcontrib.spelling",
]

rst_epilog = """
.. |river| replace:: `river <https://codeberg.org/river/river>`__
"""

needs_sphinx = "4.3"

# While upstream uses this purely to enable reference warnings, we’ll use it as
# trigger for all configurable QA messages.
nitpicky = True

exclude_patterns: list[str] = [
    ".build",
    ".github",
    "maybe",
    "README.rst",
]
# }}}

# Project information {{{
project = "river-configs"
copyright = "2024  James Rowe"  # NOQA: A001

if on_github:
    with suppress(CalledProcessError):
        proc = run(
            [
                "git",
                "-C",
                os.path.dirname(__file__),
                "log",
                "--pretty=format:%ad [%h]",
                "--date=short",
                "-n1",
            ],
            stdout=PIPE,
        )
        html_last_updated_fmt = proc.stdout.decode()
else:
    # Use a static updated time to limit rebuilds for faster commit hooks
    html_last_updated_fmt = "[local build]"

release = html_last_updated_fmt
version = ""

trim_footnote_reference_space = True
# }}}

# Options for HTML output {{{
html_theme = "sphinx_rtd_theme"

highlight_language = "zsh"

html_copy_source = False
# }}}

# spelling extension settings {{{
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
