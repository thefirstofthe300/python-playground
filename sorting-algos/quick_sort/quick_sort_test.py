import unittest
from ddt import ddt, data, file_data, unpack
import quick_sort

@ddt
class TestQuickSort(unittest.TestCase):

  @file_data('data_to_sort.json')
  def test_quick_sort(self, tests):
    self.assertEqual(quick_sort.quick_sort(tests[0]), tests[1])

if __name__ == '__main__':
  unittest.main()
