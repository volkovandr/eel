#!/usr/bin/python3

from unittest import TestCase


class TestCanImportModules(TestCase):

    def test_can_import_eveel(self):
        import eel as eel
        self.assertIsNotNone(eel)
