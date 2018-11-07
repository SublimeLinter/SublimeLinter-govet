from SublimeLinter.lint import Linter, util


class Govet(Linter):
    cmd = ('go', 'vet', '${file_path:file_name}')

    regex = r'(?P<filename>^.+):(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'

    tempfile_suffix = '-'
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'source.go'
    }
