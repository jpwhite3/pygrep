from unittest import TestCase
import os
import pygrep

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(BASE_DIR, "TestFixture")


class TestGrep(TestCase):
    def test_honorcase(self):
        results = pygrep.grep("test", FIXTURE)
        expected = 1
        actual = len(results)
        self.assertEqual(expected, actual)

    def test_honorcase_invertion(self):
        results = pygrep.grep("test", FIXTURE, invert=True)
        expected = 4
        actual = len(results)
        self.assertEqual(expected, actual)

    def test_ignorecase(self):
        results = pygrep.grep("test", FIXTURE, ignorecase=True)
        expected = 4
        actual = len(results)
        self.assertEqual(expected, actual)

    def test_ignorecase_invertion(self):
        results = pygrep.grep("test", FIXTURE, ignorecase=True, invert=True)
        expected = 1
        actual = len(results)
        self.assertEqual(expected, actual)
