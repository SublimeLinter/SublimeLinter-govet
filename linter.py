from SublimeLinter.lint import Linter, util


class Govet(Linter):
    cmd = ('go', 'tool', 'vet')
    regex = r'.+?:(?P<line>\d+):((?P<col>\d+):)?\s+(?P<message>.+)'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'source.go'
    }
