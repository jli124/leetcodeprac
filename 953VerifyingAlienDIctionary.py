# 953. Verifying an Alien Dictionary
# In an alien language, surprisingly they also use english lowercase letters, 
# but possibly in a different order. The order of the alphabet is some permutation of 
# lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, 
# return true if and only if the given words are sorted lexicographicaly in this alien language.
# Example1: Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Using Dictionary

"""

#-------------------------------------------------------------------------------
#    Soluton O(nlogn) O(A)
#-------------------------------------------------------------------------------
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # change the order into char:index dictionary
        order_index = {char:index for index, char in enumerate(order)}
        
        # compare neighbours and according to transitive property, it could all work out
        for i in xrange(len(words) - 1):
            word1 = words[i]
            word2= words[i + 1]
            
            ## for char in each adjacent words at same order, if they are reverse in order return False
            for k in xrange(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break 
                ## Corresponding to example 3, if len of word1 > len of word2, return False
                else:
                    if len(word1) > len(word2):
                        return False
        return True
                                   

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

