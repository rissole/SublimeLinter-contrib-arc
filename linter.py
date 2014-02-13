#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
#
# License: MIT
#

"""This module exports the Arc plugin class."""

from SublimeLinter.lint import Linter, util


class Arc(Linter):

    """Provides an interface to arc."""

    syntax = ('php', 'html')
    cmd = 'arc lint --output compiler --severity warning @'
    executable = 'arc'
    version_args = None
    version_re = None
    version_requirement = None
    regex = r'.+?:(?P<line>\d+):(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
