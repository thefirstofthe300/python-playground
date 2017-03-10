import unittest
import main

class TestWordSplitting(unittest.TestCase):
    
    def test_splitting_words(self):
        self.assertEqual(main.splitting_words("helloworld", ["hello", "world", "what", "is", "up"]), True)
        self.assertEqual(main.splitting_words("helloWorld", ["hello", "world", "what", "is", "up"]), False)
        
if __name__ == '__main__':
    unittest.main()