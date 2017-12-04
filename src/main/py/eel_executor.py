#!/usr/bin/python3
'''
Parser and executor of eel code
'''


from eel_parser import parse_eel_code


def execute_eel_script(filename):
    with open(filename, "r") as eel_file:
        eel_lines = eel_file.readlines()
        tokens = parse_eel_code(eel_lines, filename)
    execute_eel_code(tokens)


def execute_eel_code(tokens):
    pass
