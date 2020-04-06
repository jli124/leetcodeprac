# 309. Best Time to Buy and Sell Stock with Cooldown
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions 
as you like (ie, buy one and sell one share of the stock multiple times) with the 
following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the 
stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
3 states and 5 edges
hold -----do nothing----->hold

hold -----sell----->notHold_cooldown

notHold -----do nothing -----> notHold

notHold -----buy-----> hold

notHold_cooldown -----do nothing----->notHold

"""

#-------------------------------------------------------------------------------
#    Soluton 1 
#-------------------------------------------------------------------------------
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        not_hold, nothold_cool, hold = 0, float('-inf'), float('-inf')
        for price in prices:
            hold, nothold_cool, not_hold = max(hold, not_hold-price), hold + price, max(not_hold, nothold_cool)
        return max(not_hold, nothold_cool)
        
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
