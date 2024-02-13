#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class containing tests for the max_integer function"""

    def test_normal_list(self):
        """Tests a typical list of integers"""
        test_list = [1, 5, 3, 8, 2]
        self.assertEqual(max_integer(test_list), 8)  

    def test_empty_list(self):
        """Tests when an empty list is provided"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Tests a list with a single element"""
        self.assertEqual(max_integer([99]), 99)

    def test_negative_numbers(self):
        """Tests with a list of only negative integers"""
        test_list = [-5, -1, -8]
        self.assertEqual(max_integer(test_list), -1)

    # Add more test cases as needed ... (floats, mixed types, non-list input, etc.)


if __name__ == '__main__':
    unittest.main()
