#!/usr/bin/python3

import unittest


class TestClassName(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_test_name(self):
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()