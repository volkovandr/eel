#!/usr/bin/python3

from unittest import TestCase
import eel_parser
import textwrap


class TestToken(TestCase):
    '''Tests for the class Token'''

    def test_token_can_represent_itself(self):
        toc = eel_parser.token("some_file.eel", ["line one", "line two"], 9)
        str_repr = str(toc)
        expected = textwrap.dedent('''\
            Code from some_file.eel:
             9: line one
            10: line two
            ''')
        self.assertEqual(str_repr, expected)

    def test_can_add_line_to_token(self):
        toc = eel_parser.token("some_file.eel", ["line one"], 9)
        toc.add_line("line two")
        str_repr = str(toc)
        expected = textwrap.dedent('''\
            Code from some_file.eel:
             9: line one
            10: line two
            ''')
        self.assertEqual(str_repr, expected)


class TestParser(TestCase):
    '''Tests for the parser'''

    def test_returns_empty_list_on_no_code(self):
        tokens = eel_parser.parse_eel_code([], "some_file.eel")
        self.assertEqual(tokens, [])
