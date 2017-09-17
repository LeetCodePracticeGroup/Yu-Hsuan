class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) != 0:
            common_prefix = strs[0]
        else:
            common_prefix = ""
            
        for i in range(len(strs)-1):
            tmp_str = ""
            j = 0
            while j < len(strs[i]) and j < len(strs[i+1]):
                if strs[i][j] == strs[i+1][j]:
                    tmp_str = tmp_str + strs[i][j]
                    j = j + 1
                else:
                    break
            if len(common_prefix) > len(tmp_str):
                common_prefix = tmp_str
        
        return common_prefix