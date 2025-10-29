:program:`rst2zsh` script
=========================

.. ifconfig:: not github_actions

    .. tip::

        The `generated HTML`_ will likely be a better reading experience.

This script generates a :abbr:`CSV (Comma-Separated Values)` file with software
versions to be used with the `csv-table directive`_ in :abbr:`reST
(reStructuredText)`.  The generated output is incorporated in to the
:doc:`software <sections/river/software_versions>` section of my river
configuration.

The script is built from the sections below.

Contents
--------

.. toctree::

    sections/generate_versions/setup
    sections/generate_versions/packages
    sections/generate_versions/main_logic

.. _generated HTML: https://jnrowe.github.io/river-configs/generated_versions.html
.. _csv-table directive: https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table
