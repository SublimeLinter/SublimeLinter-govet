from SublimeLinter.lint import Linter, util


class Govet(Linter):
    cmd = ('go', 'vet', '${file_path}')

    regex = (
        r'.+?:(?P<line>\d+):((?P<col>\d+):)'  # Parse line and col.
        r'?\s+(?P<message>(.+\s*(?!(.+\/)))+)'  # Parse multiline message.
    )

    multiline = True

    tempfile_suffix = '-'
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'source.go'
    }
