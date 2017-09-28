class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        len_h = len(haystack)
        len_n = len(needle)
        
        if needle not in haystack:
            return -1
        if len_h == 0 or len_n == 0:
            return 0
        
        index = 0
        for i in range(len_h):
            if haystack[i] == needle[0]:
                if haystack[i:i+len_n] == needle:
                    index = i
                    break

                    
        return index