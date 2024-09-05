#
"""conf - Sphinx configuration information."""

import os
from contextlib import suppress
from subprocess import CalledProcessError, PIPE, run

import sphinx_rtd_theme

on_github = "GITHUB_ACTIONS" in os.environ

# General configuration {{{
extensions: [str] = [
    "sphinx.ext.ifconfig",
]

rst_epilog = """
.. |river| replace:: `river <https://codeberg.org/river/river>`__
"""

needs_sphinx = "4.3"

exclude_patterns: [str] = [
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
# }}}

# Options for HTML output {{{
html_theme = "sphinx_rtd_theme"
html_theme_path: [str] = [
    sphinx_rtd_theme.get_html_theme_path(),
]

highlight_language = "zsh"

html_copy_source = False
# }}}


def setup(app):
    # Make on_github available for ifconfig directive
    app.add_config_value("github_actions", on_github, "env")
