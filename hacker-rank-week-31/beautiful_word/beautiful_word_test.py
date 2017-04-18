import unittest
import beautiful_word

class TestBeautifulWord(unittest.TestCase):

  def test_beautiful_word(self):

    words = [
      ("abacaba", "Yes"),
      ("abba", "No"),
      ("yes", "No"),
      ("Hello", "No"),
      ("Yyes", "No")
    ]

    for word in words:
      self.assertTrue(beautiful_word.is_beautiful_word(word[0]), word[1])

if __name__ == "__main__":
  unittest.main()