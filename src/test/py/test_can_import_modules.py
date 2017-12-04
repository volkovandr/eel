#!/usr/bin/python3

from unittest import TestCase


class TestCanImportModules(TestCase):

    def test_can_import_eel(self):
        import eel as eel
        self.assertIsNotNone(eel)

    def test_can_import_eel_executor(self):
        import eel_executor as eel_executor
        self.assertIsNotNone(eel_executor)

    def test_can_import_eel_parser(self):
        import eel_parser as eel_parser
        self.assertIsNotNone(eel_parser)
