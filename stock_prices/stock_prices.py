#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = prices[1] - prices[0]
  for buy_price in prices:
    for sell_price in prices[2:]:
      # print('this is the buy_price and this is the sell_price: ', buy_price, sell_price)
      if (sell_price-buy_price) > profit and (prices.index(sell_price) > prices.index(buy_price)):
        profit = sell_price-buy_price
  return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()
# 
  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))