#!/usr/bin/python3
"""Unit tests for max_integer in list function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class contains unit tests for max_integer"""

    def test_positive(self):
        """Tests a list with no duplicates"""
        listy = [1, 2, 5, 0, 3]
        self.assertEqual(max_integer(listy), 5)

    def test_negative(self):
        """Tests a list with negative number largest magnitude"""
        listy = [1, 2, 5, -6, 3]
        self.assertEqual(max_integer(listy), 5)

    def test_negative_result(self):
        """Tests a list with negative number largest number"""
        listy = [-1, -2, -5, -6, -3]
        self.assertEqual(max_integer(listy), -1)

    def test_zero_result(self):
        """Tests a list with 0 as max"""
        listy = [-1, 0, -5, -6, -3]
        self.assertEqual(max_integer(listy), 0)

    def test_first(self):
        """Tests a list with first element max"""
        listy = [10, 2, 5, -6, 3]
        self.assertEqual(max_integer(listy), 10)

    def test_negative(self):
        """Tests a list with last element max"""
        listy = [-10, -2, -5, -6, -1]
        self.assertEqual(max_integer(listy), -1)

    def test_duplicate(self):
        """Tests a list with duplicate non-max values"""
        listy = [1, -5, 3, 1, -5]
        self.assertEqual(max_integer(listy), 1)

    def test_duplicate_max(self):
        """Tests a list with duplicate max and non-max values"""
        listy = [1, -5, 3, 3, -5]
        self.assertEqual(max_integer(listy), 3)

    def test_all_5000(self):
        """Tests a list with all values 5000"""
        listy = [5000, 5000, 5000, 5000]
        self.assertEqual(max_integer(listy), 5000)

    def test_all_0(self):
        """Tests a list with all values 0"""
        listy = [0, 0, 0, 0, 0]
        self.assertEqual(max_integer(listy), 0)

    def test_all_neg5000(self):
        """Tests a list with all values -5000"""
        listy = [-5000, -5000, -5000, -5000]
        self.assertEqual(max_integer(listy), -5000)

    def test_empty(self):
        """Tests an empty list"""
        listy = []
        self.assertIs(max_integer(listy), None)

    def test_type(self):
        badtypelist = ["hi", None, {1: 2, 2: 3}, {1, 2}, (1, 2), 3.4, 3,
                       range(5), b"hi"]
        for x in range(len(badtypelist)):
            listy = badtypelist[x]
            with self.subTest(item=badtypelist[x]):
                with self.assertRaises(TypeError):
                    max_integer(listy)

    def test_type_element_first(self):
        badtypelist = ["hi", None, {1: 2, 2: 3}, {1, 2}, (1, 2), 3.4,
                       range(5), b"hi"]
        for x in range(len(badtypelist)):
            listy = [badtypelist[x], 1, -2]
            with self.subTest(item=badtypelist[x]):
                with self.assertRaises(TypeError):
                    max_integer(listy)

    def test_type_element_last(self):
        badtypelist = ["hi", None, {1: 2, 2: 3}, {1, 2}, (1, 2), 3.4,
                       range(5), b"hi"]
        for x in range(len(badtypelist)):
            listy = [1, -2, badtypelist[x]]
            with self.subTest(item=badtypelist[x]):
                with self.assertRaises(TypeError):
                    max_integer(listy)

if __name__ == "__main__":
    unittest.main()
