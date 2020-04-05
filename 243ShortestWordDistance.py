# 243. Shortest Word Distance
"""
Given a list of words and two words word1 and word2, return the shortest distance 
between these two words in the list.
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""

"""

#-------------------------------------------------------------------------------
#    Soluton 1 
#-------------------------------------------------------------------------------
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_diff = ind1 =  ind2 = len(words)
        for ind, word in enumerate(words):
            if word == word1: 
                ind1 = ind
                min_diff = min(min_diff, abs(ind1-ind2))
            if word == word2: 
                ind2 = ind
                min_diff = min(min_diff, abs(ind1-ind2))
        return min_diff

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
