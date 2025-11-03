"""Mitchell Davis.

Homework 1 - Black Box Testing
10/19/25
"""
import random
import unittest
from credit_card_validator import credit_card_validator


class TestCCValidator(unittest.TestCase):
    """Class for test cases using unit test."""

    def test1(self):
        """Creating one randomized value"""
        max_length = 19
        min_length = 10
        num_tests = 800000

        for i in range(num_tests):

            length = random.randint(0, max_length)
            card_num = ""
            for char in range(length):
                char = str(random.randint(0, 9))
                card_num += char

            print(credit_card_validator(card_num))


if __name__ == '__main__':
    unittest.main(verbosity=2)
