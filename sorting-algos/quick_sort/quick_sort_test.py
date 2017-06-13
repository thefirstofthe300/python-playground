import unittest
from ddt import ddt, data, file_data, unpack
import quick_sort

@ddt
class TestQuickSort(unittest.TestCase):

  @data(([5, 24, 2, 3, 4, 6, 8], [2, 3, 4, 5, 6, 8, 24]),
      ([5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5]),
      ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
      ([2, 1, 4, 5, 6, 3, 4, 6, 7, 8, 10, 396, 193, 594, 29, 485, 29, 19, 1, 59, 94, 39102, 59, 289],
       [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 10, 19, 29, 29, 59, 59, 94, 193, 289, 396, 485, 594, 39102])
    )
  @unpack
  def test_quick_sort(self, unsorted_list, sorted_list):
    self.assertEqual(quick_sort.quick_sort(unsorted_list), sorted_list)

if __name__ == '__main__':
  unittest.main()
