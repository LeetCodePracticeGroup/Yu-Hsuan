class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x_rev = 0
        
        x_str = str(x)
        if x_str[0] == '-':
            return False
        
        x_copy = x
        while x_copy != 0:
            x_rev = x_rev * 10 + x_copy % 10
            x_copy = x_copy / 10
        
        if x_rev == x:
            return True
        else:
            return False