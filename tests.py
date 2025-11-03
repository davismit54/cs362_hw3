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
        num_tests = 700000

        for i in range(num_tests):

            length = random.randint(min_length, max_length)
            card_num = ""

            match random.randint(0, 6):
                case 0:
                    # visa
                    card_num += "4"

                case 1:
                    # asterCard 1
                    card_num += str(random.randint(51, 55))

                case 2:
                    # MasterCard 2
                    card_num += str(random.randint(2221, 2720))

                case 3:
                    # Amex 1
                    card_num += "34"

                case 4:
                    # Amex 2
                    card_num += "37"

            for char in range(length - len(card_num)):
                char = str(random.randint(0, 9))
                card_num += char

            print(credit_card_validator(card_num))


if __name__ == '__main__':
    unittest.main(verbosity=0)
