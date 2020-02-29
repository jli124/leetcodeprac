#3. Longest Substring Without Repeating Characters
#Given a string, find the length of the longest substring without repeating characters.
#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Two pointers
start: keep track the the last time the current character shows up
res: keep track of the current maximum length

"""

#-------------------------------------------------------------------------------
#    Soluton1 ---Using dictionary
#-------------------------------------------------------------------------------
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                # update the res
                res = max(res, i-start)
                # here should be careful, like "abba"
                start = max(start, dic[ch]+1)
            dic[ch] = i
        # return should consider the last 
        # non-repeated substring
        return max(res, len(s)-start)
