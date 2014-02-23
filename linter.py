#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jon Surrell
# Copyright (c) 2014 Jon Surrell
#
# License: MIT
#

"""This module exports the Govet plugin class."""

from SublimeLinter.lint import Linter, util


class Govet(Linter):

    """Provides an interface to go vet."""

    syntax = ('go', 'gosublime-go')
    cmd = ('go', 'tool', 'vet')
    regex = r'^.+:(?P<line>\d+):\s+(?P<message>.+)'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDERR
