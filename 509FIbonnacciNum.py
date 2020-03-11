# 509. Fibonacci Number
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
"""
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
"""

#-------------------------------------------------------------------------------
#    Soluton1 - Recursion
#-------------------------------------------------------------------------------
class Solution():
    def fib_rec(self, n):
        """
        :type N: int
        :rtype: int
        """
        if n == 0 or n == 1: return n
        return self.fib_rec(n - 1) + self.fib_rec(n - 2)
                    
#-------------------------------------------------------------------------------
#    Soluton2  - DP
#-------------------------------------------------------------------------------
class Solution():
# cache = 
	n = 10
	cache = [None] * (n + 1)

	def fib_dyn(self, n):
		# Base case
		if n == 0 or n == 1:
			return n
		# Check Cache
		if cache[n] != None:
			return cache[n]
		# Keep setting cache
		cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

		return cache[n]



#-------------------------------------------------------------------------------
#    Soluton3  - Iterative
#-------------------------------------------------------------------------------
class Solution():	
	def fib_iter(self, n):
		a, b = 0, 1
		for i in range(n):
			a, b = b, a + b
		return a 
#-------------------------------------------------------------------------------
#    Test
#------------------------------------------------------------------------------

soln = Solution()
print(soln.fib_iter(10))