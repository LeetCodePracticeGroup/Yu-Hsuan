class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        """
        Input:
        haystack = "mississippi"
        needle = "issip"
        """
        len_h = len(haystack)
        len_n = len(needle)
        
        if needle not in haystack:
            return -1
        if len_h == 0 or len_n == 0:
            return 0
        
        index = 0
        found = True
        for i in range(len_h):
            if haystack[i] == needle[0]:
                k = 0
                for j in range(i, i + len_n):
                    if haystack[j] != needle[k]:    # Line 23: IndexError: string index out of range
                        found = False
                        break;
                    k = k + 1
                
                if found == True:
                    index = i
                    break
                    
        return index