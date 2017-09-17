class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative_number = False
        x_rev = 0
        
        x_str = str(x)
        if x_str[0] == '-':
            is_negative_number = True
            x = abs(x)
        
        while x != 0:
            x_rev = x_rev * 10 + x % 10
            x = x / 10
        
        if x_rev > (1 << 31)-1:
            return 0
        elif is_negative_number:
            return 0-x_rev
        else:
            return x_rev
        