# 121. Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell 
# one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""


"""

#-------------------------------------------------------------------------------
#    Soluton - O(n) & O(1)
#-------------------------------------------------------------------------------
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

