# 28. Implement strStr()
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 Input: haystack = "hello", needle = "ll"
Output: 2
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
1. Subtring
2. Two pointer
3. Rabin-Karp
"""

#-------------------------------------------------------------------------------
#    Soluton 1 - Substring Linear Time Slice O((N-m)m)
#-------------------------------------------------------------------------------
# class Solution():
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         n, m = len(haystack), len(needle)

#         for i in range(n- m+ 1):
#             if haystack[i:i+m] == needle:
#                 return i
#         return -1
#-------------------------------------------------------------------------------
#    Soluton 2 - Two pointer O((N-m)m)
#-------------------------------------------------------------------------------
# class Solution():
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         n, m = len(haystack), len(needle)

#         if m == 0:
#             return 0

#         pn = 0
#         while pn < n - m + 1:
#             # if the current character not equal to the first on in target
#             while pn < n - m + 1 and haystack[pn] != needle[0]:
#                 pn += 1

#             # if the current character equal to the first on in target
#             curr_len = pm = 0
#             while pn < n and pm < m and haystack[pn] == needle[pm]:
#                 pm += 1
#                 pn += 1
#                 curr_len += 1
#             if curr_len == m:
#                 return pn - m

#             # backtracking
#             pn = pn - curr_len + 1

#         return -1
#-------------------------------------------------------------------------------
#    Soluton 3 - Rabin Karp O(N)
#-------------------------------------------------------------------------------
class Solution():
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)

        if m > n:
            return -1

        # set the base value for the rolling hash function
        a = 26
        modulus = 2**31

        # func convert character to int
        h_to_int = lambda i: ord(haystack[i]) - ord('a')
        needle_to_int = lambda i: ord(needle[i]) - ord('a')

        # compute the hash for haystack[:m] and needle
        h = ref_h = 0
        for i in range(m):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h: return 0

        # const value of a ** m % modulus
        am = pow(a, m, modulus)
        for j in range(1, n - m + 1):
            h = (h * a - h_to_int(j-1)*am + h_to_int(j + m -1)) % modulus
            if h == ref_h:
                return j
        return -1

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------
haystack = "hello"
needle = 'll'
soln = Solution()
print(soln.strStr(haystack, needle))
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
