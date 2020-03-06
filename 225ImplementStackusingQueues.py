# 225. Implement Stack using Queues
# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""

Using queue as required
"""

#-------------------------------------------------------------------------------
#    Soluton O(nlogn) O(A)
#-------------------------------------------------------------------------------
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        lens = len(self.q1)
        for i in range(lens - 1):
            temp = self.q1.pop(0)
            self.q1.append(temp)
        return self.q1.pop(0)
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        lens = len(self.q1)
        for i in range(lens):
            temp = self.q1.pop(0)
            self.q1.append(temp)
        return temp
        
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.q1:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


                         

#-------------------------------------------------------------------------------
#    Test
#-------------------------------------------------------------------------------

