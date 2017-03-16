import unittest
import main

class TestLargestIntSubstrSum(unittest.TestCase):

  def test_sums(self):

    tests = [
        [[10, 20, -12, 75, 10], 85],
        [[10, -10, 10, -10], 10],
        [[-10, -10, -1], -1],
        [[],  0]
      ]

    for test in tests:
      self.assertEqual(main.largest_int_substr_sum(test[0]), test[1])

if __name__ == "__main__":
  unittest.main()