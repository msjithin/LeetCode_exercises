"""
123. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 105

"""
from typing import List


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <2 :
            return 0
        
        """
        USING STATES METHOD
        1 transaction = 1 buy + 1 sell ==> profit = sell_price - buy_price
        allowed cases buy->sell->buy->sell
        3 choices - buy, sell or skip
        
        0 ---> state1 ---> state2 ---> state3 ---> state4
           BUY   SELL   BUY    SELL

        """
        state1 = -prices[0] #first element. Negavtive sign since we only need profit. buying = money from pocket
        state2 = float('-inf')
        state3 = float('-inf')
        state4 = float('-inf')
        
        for price in prices:
            # change states A,B, C, D depending on price
            state1 = max(state1, -price)         #buy stock or keep A, we choose maximum
            state2 = max(state2, state1 + price)      #waiting to sell, or sell (A->B)
            state3 = max(state3, state2 - price)      #B->C
            state4 = max(state4, state3 + price)      #C->D
            print(state1, state2, state3, state4)
        return state4
            
            
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0 
        dp = [0 for _ in range(len(prices))]
        print(dp)
        # when we buy a stock = we paid moey = profit is -ve
        n=2    # this defines how many transactions we can have
        for t in range(1, n+1):
            profit = 0
            pos = -prices[0]
            for i in range(1, len(prices)):
                pos = max(pos, dp[i]-prices[i])    #maximum position we can we be in
                                              # we want to buy it at lower price, -ve sign helps choose minimum price
                profit = max(profit, pos+prices[i]) # if we sell the stock now, we get the price tag at i -> pos+price[i]
                dp[i] = profit
                print('dp=', dp)

        return dp[-1]  # or return profit , they are same

            
