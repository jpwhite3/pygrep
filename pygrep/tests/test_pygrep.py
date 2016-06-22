from unittest import TestCase

import pygrep

class TestGrep(TestCase):
    def test_this_works(self):
        results = pygrep.grep('test', __file__)
        self.assertEqual(len(results), 2)