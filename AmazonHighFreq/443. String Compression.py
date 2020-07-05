# 443. String Compression
"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

# Two pointer

#-------------------------------------------------------------------------------
#    Soluton  - XOR and hashmap
#-------------------------------------------------------------------------------
class Solution:
    def compress(self, chars: List[str]) -> int:
        left = i = 0
        while i < len(chars):
            length, char = 1, chars[i]
            # when the char does not change, just update length and i
            while i + 1 < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
                
            # in-place change the char for chars_list
            chars[left] = char
            
            # update only when the length is > 1 and use string format
            if length > 1:
                len_char = str(length)
                chars[left + 1:left + 1 + len(len_char)] = len_char
                left += len(len_char)
            left, i = left + 1, i + 1
        
        return left
#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
# soln = Solution()
# print(soln.)