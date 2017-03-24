import unittest
import main

class TestBuySellStocks(unittest.TestCase):

  def test_sums(self):

    tests = [
        [[10, 20, -12, 75, 10], [-12, 75]],
        [[1, 4, -12, 75, 10], [-12, 75]],
        [[10, -10, 10, -10], [-10, 10]],
        [[],  0]
      ]

    for test in tests:
      self.assertEqual(main.buy_sell_stocks(test[0]), test[1])

if __name__ == "__main__":
  unittest.main()