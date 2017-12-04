#!/usr/bin/python3
'''
Interpreter of the language Eel
Usage: python3 eel.py <eel module name>
'''

import sys
import os.path
from eel_executor import execute_eel_script


def parse_command_line_arguments_exit_on_error(args):
    if len(args) != 2:
        print("Expected exactly one command line argument: the name"
              "of the .eel file")
        sys.exit(1)
    eel_script_name = args[1]
    if not os.path.exists(eel_script_name):
        print("The file {} not found".format(eel_script_name))
        sys.exit(2)
    if not os.path.isfile(eel_script_name):
        print("The given name {} is not a file".format(eel_script_name))
        sys.exit(2)
    return eel_script_name


def main():
    eel_script_name = parse_command_line_arguments_exit_on_error(sys.argv)
    execute_eel_script(eel_script_name)


if __name__ == "__main__":
    main()
