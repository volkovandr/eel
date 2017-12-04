#!/usr/bin/python3
'''
Parser and executor of eel code
'''


def execute_eel_script(filename):
    with open(filename, "r") as eel_file:
        eel_lines = eel_file.readlines()
        tokens = parse_eel_code(eel_lines, filename)
    execute_eel_code(tokens)


def parse_eel_code(lines, filename):
    pass


def execute_eel_code(tokens):
    pass
