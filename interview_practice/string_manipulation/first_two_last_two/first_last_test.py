import unittest
import first_last
from ddt import ddt, data, unpack

@ddt
class TestFirstLast(unittest.TestCase):
  @data(['hello world', 'held'],
        [',, who,', ''],
        ['waup?', 'waup'])
  @unpack
  def test_first_last(self, string, sliced):
    self.assertEqual(first_last.first_last(string), sliced)

if __name__ == '__main__':
  unittest.main()