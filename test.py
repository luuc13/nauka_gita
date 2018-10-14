import unittest

from calculator import calculate

class TestCalcurator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1, 10, '+')
        self.assertEqual(r, 3)
