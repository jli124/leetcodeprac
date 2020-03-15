# 735. Asteroid Collision
"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves 
at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.


"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""
stack 
"""

#-------------------------------------------------------------------------------
#    Soluton1 
#-------------------------------------------------------------------------------
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = [] #Used to track the first num of the pair
        for asteroid in asteroids:
            while len(res) and asteroid < 0 and res[-1] > 0:
                # example: 5 and -5
                if res[-1] == -asteroid:
                    res.pop()
                    break
                # example 2 and -5, 2 get destroyed, -5 still needs to be append 
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                # example 5 and -2, -2 get destroyed    
                elif res[-1] > -asteroid:
                    break
            else:
                res.append(asteroid)
        return res
                    
        
                    
        
#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

