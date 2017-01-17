import unittest
from GeneratePrimes import genPrimes

class PrimesTestCases(unittest.TestCase):
  def test_it_calculates_primes_for_positive_int(self):
      result = genPrimes(10)
      self.assertEqual(result, [2,3,5,7], msg="Should return [2,3,5,7] for the input 10")

  def test_no_calculation_for_negative_int(self):
      result = genPrimes(-6)
      self.assertEqual(result, "Invalid Input", msg="Should return 'Invalid Input' for negative input")

  def test_no_calculation_for_zero(self):
      result = genPrimes(0)
      self.assertEqual(result, "Invalid Input", msg="Should return 'Invalid Input' for input 0")

  def test_no_calculation_for_dictionary(self):
      result = genPrimes({"k":10})
      self.assertEqual(result, "Invalid Input", msg="Should return 'Invalid Input' for dict input")

  def test_no_calculation_for_string(self):
      result = genPrimes("a string")
      self.assertEqual(result, "Invalid Input", msg="Should return 'Invalid Input' for string input")

  def test_no_calculation_for_list_input(self):
      result = genPrimes([12,10,13])
      self.assertEqual(result, "Invalid Input", msg="Should return 'Invalid Input' for list input")

  def test_no_calculation_for_large_positive_input(self):
      result = genPrimes(300)
      self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293], msg="Should return all primes for large input")

  def test_no_calculation_for_float(self):
      result = genPrimes(20.23)
      self.assertEqual(result, "Invalid Input", msg="Should return 'Invalid Input' for string input")

  def test_no_calculation_for_one(self):
      result = genPrimes(1)
      self.assertEqual(result, "Invalid Input", msg="Should return 'Invalid Input' for string input")

  def test_no_calculation_for_tuple(self):
      result = genPrimes((2,13,30))
      self.assertEqual(result, "Invalid Input", msg="Should return 'Invalid Input' for string input")

  def test_no_calculation_for_large_negative_int(self):
      result = genPrimes(-562166)
      self.assertEqual(result, "Invalid Input", msg="Should return 'Invalid Input' for string input")

if __name__ == '__main__':
    unittest.main()