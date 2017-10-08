class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        mod = []

        if n == 0 or n == 1:
            return True

        while n > 0:
            q = n % 2
            mod.append(q)
            
            n = n / 2

        for i in range(len(mod) - 1):
            if mod[i] == mod[i+1]:
                return False

        return True      