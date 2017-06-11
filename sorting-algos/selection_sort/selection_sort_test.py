import unittest
import selection_sort

class TestSelectionSort(unittest.TestCase):

  def test_selection_sort(self):
    tests = [
      ([5,24,2,3,4,6,8], [2,3,4,5,6,8,24]),
      ([5,5,5,5,5,5], [5,5,5,5,5,5]),
      ([1,2,3,4,5,6,7], [1,2,3,4,5,6,7])
    ]

    for test in tests:
      self.assertEqual(selection_sort.selection_sort(test[0]), test[1])

if __name__ == '__main__':
  unittest.main()
