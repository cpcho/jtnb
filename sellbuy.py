"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell 
one share of the stock), design an algorithm to find the maximum profit. Note that you cannot sell a stock before you buy one.

Example 1:
	Input: [7, 1, 5, 3, 6, 4]
	Output: 5
	Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
	Input: [7, 6, 4, 3, 1]
	Output: 0
	In this case, no transaction is done, i.e. max profit = 0.
Example 3:
	Input: [2, 4, 1]
	Output: 2
Example 4:
	Input: [2,1,2,1,0,1,2]
	Output: 2
Example 5:
	Input: [3,2,6,5,0,3]
	Output: 4
"""
def maxProfit(prices):
	if prices == []:
		return 0
	min_price = prices[0]
	min_price_idx = prices.index(min_price)
	for i in prices[1:(len(prices)-1)]:
		if i >= min_price:
			continue
		else:
			min_price = i
			min_price_idx = prices.index(i)
	max_price = min_price
	for j in prices[min_price_idx:]:
		if j > max_price:
			max_price = j
		elif j <= max_price or j == 0:
			continue
	return (max_price - min_price)

arr = [7, 1, 5, 3, 6, 4]

print(maxProfit(arr))

def max_profit(prices):

	buy_price = sell_price = prices[0]

	#buy_price should be the lowest
	buy_price = min(prices)
	sell_price = max(prices)

	if prices.index(sell_price) < prices.index(buy_price):
		return 0
	return sell_price - buy_price

print(max_profit(arr))