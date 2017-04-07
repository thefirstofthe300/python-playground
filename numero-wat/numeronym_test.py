import numeronym
import unittest

class TestNumeronym(unittest.TestCase):

  def test_is_valid_numeronym(self):
    word_list = ['kettledrums', 'keyboarders', 'keyboarding', 'keypunching',
                 "keystroke's", "kickstand's", "kidnapper's", 'kidnappings',
                 "kilocycle's", "kilohertz's", 'kilohertzes', "kilometer's",
                 'kindhearted', 'kingfishers', "kinswoman's", 'kitchenette',
                 'kitchenware', 'kleptomania', 'knackwursts', 'kneecapping',
                 'knickknacks', 'knighthoods', 'knockwursts', "knowledge's",
                 'knucklehead', 'kookaburras', "kookiness's"]

    invalid_numeronyms = ["k9", "k8s", "k8g", "k8d"]
    valid_numeronyms = ["k7ds", "k7ks"]

    for numeronym in invalid_numeronyms:
      assertFalse(is_valid_numeronym(numeronym, word_list))
    for numeronym in valid_numeronyms:
      assertTrue(is_valid_numeronym(numeronym, word_list))
