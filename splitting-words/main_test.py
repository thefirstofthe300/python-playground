import unittest
import main

class TestWordSplitting(unittest.TestCase):

    def test_splitting_words(self):
        tests = [
            ["helloworld", ["hello", "world", "what", "is", "up"], True],
            ["helloWorld", ["hello", "world", "what", "is", "up"], False],
            ["helloworld", ["helloworld", "what", "is", "up"], False],
            ["helloworldis", ["hello", "world", "what", "is", "up"], True],
            ["helloworldiswhat", ["hello", "world", "what", "is", "up"], True],
            ["", ["hello", "world", "what", "is", "up"], False],
            ["helloworld", [], False]
        ]

        for x in tests:
            self.assertEqual(main.splitting_words(x[0], x[1]), x[2])

if __name__ == '__main__':
    unittest.main()