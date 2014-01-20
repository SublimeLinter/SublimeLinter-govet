#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jon Surrell,,,
# Copyright (c) 2014 Jon Surrell,,,
#
# License: MIT
#

"""This module exports the Vet plugin class."""

from SublimeLinter.lint import Linter, util


class Vet(Linter):

    """Provides an interface to go vet."""

    syntax = 'go'
    cmd = ('go', 'tool', 'vet')
    regex = r'^vet:\s+.+:\s+.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)$'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDERR