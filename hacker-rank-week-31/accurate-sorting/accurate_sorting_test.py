import accurate_sorting
import unittest

class TestAccurateSorting(unittest.TestCase):

  def test_accurate_sorting(self):
    tests = [
        ([0, 1, 2], "Yes"),
        ([0], None),
        ([2, 0, 1], "No"),
        ([0, 2, 3, 1, 4], "No"),
        ([-1, 1, 0], "Yes"),
        ([2, 3, 0, 1], "No")
      ]

    for test in tests:
      self.assertEqual(accurate_sorting.IsSortable(test[0]), test[1])

if __name__ == "__main__":
  unittest.main()