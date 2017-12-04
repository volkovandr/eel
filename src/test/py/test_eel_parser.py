#!/usr/bin/python3

from unittest import TestCase
import eel_parser
import textwrap


class TestEelParser(TestCase):

    def test_token_can_represent_itself(self):
        toc = eel_parser.token("some_file.eel", ["line one", "line two"], 9)
        str_repr = str(toc)
        expected = textwrap.dedent('''\
            Code from some_file.eel:
             9: line one
            10: line two
            ''')
        self.assertEqual(str_repr, expected)