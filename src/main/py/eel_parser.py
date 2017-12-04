#!/usr/bin/python3
'''
Parser of eel code
'''


class token:

    def __init__(self, filename, lines):
        self.filename = filename
        self.lines = lines

    def __repr__(self):
        return "Code from {}:\n{}\n".format(
            self.filename, "\n".join(self.lines))


def parse_eel_code(lines, filename):
    pass
