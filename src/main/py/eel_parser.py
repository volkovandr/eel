#!/usr/bin/python3
'''
Parser of eel code
'''


import math


class token:

    def __init__(self, filename, lines, start_from):
        self.filename = filename
        self.lines = lines
        self.start_from = start_from

    def add_line(self, line):
        self.lines.append(line)

    def __repr__(self):
        line_numbers = list(
            range(self.start_from, self.start_from + len(self.lines)))
        pad = int(math.log10(line_numbers[-1])) + 1
        pattern = "{:>" + str(pad) + "}: {}"
        return "Code from {}:\n{}\n".format(
            self.filename, "\n".join(
                [pattern.format(a[0], a[1])
                 for a in zip(line_numbers, self.lines)]))


def parse_eel_code(lines, filename):
    pass
