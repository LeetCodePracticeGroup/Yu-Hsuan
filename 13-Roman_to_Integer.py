class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # I=1, X=10, L=50, C=100, D=500, M=1000
        converter = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        sum = converter[s[0]]
        for i in range(len(s)-1):
            if converter[s[i]] - converter[s[i+1]] < 0:
                ## e,g. XIV = 10 + (5-1) = 9
                sum = sum - converter[s[i]] + (converter[s[i+1]] - converter[s[i]])
            elif converter[s[i]] - converter[s[i+1]] >= 0:
                sum = sum + converter[s[i+1]]
        
        return sum