# custom error


class MySimpleError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return repr(str(self.code) + ":" + self.message)

    