"""Mitchell Davis.

Homework 1 - Black Box Testing
10/19/25
"""

import unittest
from credit_card_validator import credit_card_validator


class TestCCValidator(unittest.TestCase):
    """Class for test cases using unit test."""

    def test1(self):
        """Setup test just to try gradescope."""
        card_num = "0123456789"
        credit_card_validator(card_num)


if __name__ == '__main__':
    unittest.main(verbosity=2)
