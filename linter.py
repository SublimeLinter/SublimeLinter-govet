from SublimeLinter.lint import Linter, util


class Govet(Linter):
    cmd = ('go', 'vet', '${file_path}')

    regex = r'(?P<filename>^.+?):(?P<line>\d+):((?P<col>\d+):)?\s+(?P<message>(.|\n\t)+)'

    tempfile_suffix = '-'
    multiline = True
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'source.go'
    }

    def split_match(self, match):
        if self.filename.find(match.group('filename')) > 0:  # self.filename is an absolute path
            error = super().split_match(match)
            flat_message = ' '.join(line.strip() for line in error.message.split('\n'))
            return error._replace(message=flat_message)
