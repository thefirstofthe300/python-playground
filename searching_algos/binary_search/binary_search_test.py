import unittest
from ddt import ddt, file_data
import binary_search

@ddt
class TestBinarySearch(unittest.TestCase):

  @file_data('data_binary_search.json')
  def test_binary_search(self, test):
    self.assertEqual(binary_search.binary_search(test[0], test[1]), test[2])

if __name__ == '__main__':
  unittest.main()
