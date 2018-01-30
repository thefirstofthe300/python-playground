import unittest
import is_anagram

class TestIsAnagram(unittest.TestCase):

  def test_is_anagram(self):
    tests = [
      (("helloworld", "hola"), False),
      (("hello", "lleho"), True),
    ]

    for test in tests:
      self.assertEqual(is_anagram.is_anagram(test[0][0], test[0][1]), test[1])

if __name__ == '__main__':
  unittest.main()
