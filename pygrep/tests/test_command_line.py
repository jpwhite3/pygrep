from unittest import TestCase
from pygrep.command_line import main

class TestConsole(TestCase):
    def test_basic(self):
        main()