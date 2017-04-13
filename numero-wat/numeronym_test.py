import numeronym
import unittest

class TestNumeronym(unittest.TestCase):

  def test_parse_numeronym(self):
    tests = [
        ['k8s', [('k', 0), ('s', 10)]],
        ['k8', [('k', 0)]],
        ['k9', [('k', 0)]],
        ['ka8', [('k', 0), ('a', 1)]],
        ['h1', [('h', 0)]]
      ]

    for test in tests:
      self.assertSequenceEqual(numeronym.parse_numeronym(test[0]), test[1])

  def test_get_numeronym_length(self):
    tests = [
      ("k8s", 10),
      ("t9", 10),
      ("k10", 11),
      ("wa3s", 6)
    ]

    for test in tests:
      self.assertEqual(numeronym.get_numeronym_length(test[0]), test[1])

  def test_compare_word_to_numeronym(self):
    tests = [
        ['kubernetes', [('k', 0), ('s', 9)], True],
        ['kats', [('k', 0)], True],
        ['hello', [('k', 0)], False],
        ['k', [('k', 0), ('a', 1)], False],
        ['h1', [('h', 0)], True],
        ['k8s', [('k', 0), ('s', 10)], False],
        ['k1', [('h', 0)], False],
      ]

    for test in tests:
      self.assertEqual(numeronym.compare_word_to_numeronym(test[0], test[1]), test[2])

  def test_is_valid_numeronym(self):
    tests = [
              [
                "k10",
                [
                  'kettledrums', 'keyboarders', 'keyboarding', 'keypunching',
                  "keystroke's", "kickstand's", "kidnapper's", 'kidnappings',
                  "kilocycle's", "kilohertz's", 'kilohertzes', "kilometer's",
                  'kindhearted', 'kingfishers', "kinswoman's", 'kitchenette',
                  'kitchenware', 'kleptomania', 'knackwursts', 'kneecapping',
                  'knickknacks', 'knighthoods', 'knockwursts', "knowledge's",
                  'knucklehead', 'kookaburras', "kookiness's"
                ],
                False
              ],
              [
                "k8ed",
                [
                  'kettledrums', 'keyboarders', 'keyboarding', 'keypunching',
                  "keystroke's", "kickstand's", "kidnapper's", 'kidnappings',
                  "kilocycle's", "kilohertz's", 'kilohertzes', "kilometer's",
                  'kindhearted', 'kingfishers', "kinswoman's", 'kitchenette',
                  'kitchenware', 'kleptomania', 'knackwursts', 'kneecapping',
                  'knickknacks', 'knighthoods', 'knockwursts', "knowledge's",
                  'knucklehead', 'kookaburras', "kookiness's"
                ],
                True
              ]
            ]

    for test in tests:
      self.assertEqual(numeronym.is_valid_numeronym(test[0], test[1]), test[2])

if __name__ == "__main__":
  unittest.main()