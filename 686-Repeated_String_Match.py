class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        tmp = A
        count = 1
        
        while B not in A:           
            A = A + tmp

            if len(A) > len(B) and B not in A:
                return -1            
            
            count = count + 1
            
        return count