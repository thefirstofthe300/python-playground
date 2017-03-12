import unittest
import main

class TestWordSplitting(unittest.TestCase):

    def test_splitting_words(self):
        self.assertEqual(main.splitting_words("helloworld", ["hello", "world", "what", "is", "up"]), True)
        self.assertEqual(main.splitting_words("helloWorld", ["hello", "world", "what", "is", "up"]), False)
        self.assertEqual(main.splitting_words("helloworld", ["helloworld", "what", "is", "up"]), False)
        self.assertEqual(main.splitting_words("helloworldis", ["hello", "world", "what", "is", "up"]), True)
        self.assertEqual(main.splitting_words("helloworldiswhat", ["hello", "world", "what", "is", "up"]), True)

if __name__ == '__main__':
    unittest.main()