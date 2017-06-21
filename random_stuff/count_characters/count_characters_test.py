import unittest
from ddt import ddt, data, unpack
import count_characters

@ddt
class TestCountCharacters(unittest.TestCase):

  @data(['Hello world', {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}],
        ['What is up?', {'w': 1, 'h': 1, 'a': 1, 't': 1, 'i': 1, 's': 1, 'u': 1, 'p': 1}],
        ['On my way', {'o': 1, 'n': 1, 'm': 1, 'y': 2, 'w': 1, 'a': 1}])
  @unpack
  def test_count_characters(self, string, counted):
    self.assertDictEqual(count_characters.count_characters(string), counted)

if __name__ == '__main__':
  unittest.main()
