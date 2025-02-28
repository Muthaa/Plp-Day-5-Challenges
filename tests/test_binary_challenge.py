import unittest
from binary_challenge import is_valid_binary, decimal_to_binary, binary_to_decimal

class TestBinaryChallenge(unittest.TestCase):
    def test_is_valid_binary(self):
        self.assertTrue(is_valid_binary("101"))
        self.assertTrue(is_valid_binary("-101"))
        self.assertTrue(is_valid_binary("101.101"))
        self.assertTrue(is_valid_binary("-101.101"))
        self.assertFalse(is_valid_binary("102"))
        self.assertFalse(is_valid_binary("10.2"))
        self.assertFalse(is_valid_binary("abc"))

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(5), "101")
        self.assertEqual(decimal_to_binary(-5), "-101")
        self.assertEqual(decimal_to_binary(0), "0")
        self.assertEqual(decimal_to_binary(2.75), "10.11")
        self.assertEqual(decimal_to_binary(-2.75), "-10.11")

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal("101"), 5)
        self.assertEqual(binary_to_decimal("-101"), -5)
        self.assertEqual(binary_to_decimal("0"), 0)
        self.assertEqual(binary_to_decimal("10.11"), 2.75)
        self.assertEqual(binary_to_decimal("-10.11"), -2.75)
        with self.assertRaises(ValueError):
            binary_to_decimal("102")
        with self.assertRaises(ValueError):
            binary_to_decimal("10.2")

if __name__ == "__main__":
    unittest.main()
