import unittest
import merge_sort
from ddt import ddt, data, file_data, unpack

@ddt
class TestMergeSort(unittest.TestCase):

  @file_data('data_to_sort.json')
  def test_merge_sort(self, test):
    self.assertEqual(merge_sort.merge_sort(test[0]), test[1])

if __name__ == '__main__':
  unittest.main()
