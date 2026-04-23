"""Test module"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(10, 5)
        self.assertEqual(res, 15)

    def test_subtract_numbers(self):
        """Test subtracting numbers together"""
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)
