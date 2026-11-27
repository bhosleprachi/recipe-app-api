
"""
sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test Calc module ."""

    def test_add_numbers(self):
        """Tests adding numbers together"""
        res =calc.add(5,6)

        self.assertEqual(res,11)