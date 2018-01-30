"""This function assumes that at least one value is larger than 0"""
def buy_sell_stocks(prices):
  if prices == []:
    return 0
  buy_price = prices[0]
  profit = prices[1] - prices[0]
  sell_price = prices[1]

  for price in prices:
    if (price - buy_price) > profit:
      sell_price = price
      profit = price - buy_price
    if price < buy_price:
      buy_price = price

  return [buy_price, sell_price]