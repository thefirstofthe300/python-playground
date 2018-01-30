import unittest
import selection_sort
from ddt import ddt, unpack, data_file, data

@ddt
class TestSelectionSort(unittest.TestCase):

  @data_file('data_to_sort.json')
  def test_selection_sort(self, tests):
    self.assertEqual(selection_sort.selection_sort(test[0]), test[1])

if __name__ == '__main__':
  unittest.main()
