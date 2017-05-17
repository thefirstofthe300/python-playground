import listify_word_file
import unittest
import mock

class TestListifyWordFile(unittest.TestCase):
  def test_listify_word_file(self):
    with mock.patch("__builtin__.open", mock.mock_open(read_data="Hello\nworld")) as mock_open:
      mocked_list = listify_word_file.listify_word_file("hello")
      self.assertEqual(mocked_list, ["Hello", "world"])

if __name__ == "__main__":
  unittest.main()