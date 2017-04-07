import numeronym
import unittest

class TestNumeronym(unittest.TestCase):

  def test_is_valid_numeronym(self):
    tests = [
              [
                "k9",
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
                "k8s",
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
              ]
            ]

    for test in tests:
      self.assertEqual(numeronym.is_valid_numeronym(test[0], test[1]), test[2])

if __name__ == "__main__":
  unittest.main()