import unittest
import main

class TestSmallestEvenlyDivisible(unittest.TestCase):
    
    def test_prime_factors(self):
        self.assertEqual(main.prime_factors(20), {2: 2, 5: 1})
        self.assertEqual(main.prime_factors(1), {})
        self.assertEqual(main.prime_factors(0), {})
        self.assertEqual(main.prime_factors(4), {2: 2})
        self.assertEqual(main.prime_factors(30), {2: 1, 3: 1, 5: 1})
        
    def test_most_factors(self):
        self.assertEqual(main.most_factors({2: 2}, 4), {2: 2})
        self.assertEqual(main.most_factors({2: 1, 3: 1}, 4), {2: 2, 3: 1})
        
    def test_smallest_evenly_divisible(self):
        self.assertEqual(main.smallest_evenly_divisible(0, 10), 2520)
        self.assertEqual(main.smallest_evenly_divisible(0, 20), 232792560)
        
        
if __name__ == '__main__':
    unittest.main()