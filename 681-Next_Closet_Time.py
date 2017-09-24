class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        
        digits = []
        for digit in time:
            if digit == ':':    
                continue
            else:
                digits.append(digit)
        
        h = time.split(":")[0]
        m = time.split(":")[1]
        
        while True:
            if m == "59":
                h = str(int(h)+1)
                m = "00"
            else:
                m = str(int(m)+1)
            
            if int(h) > 23:
                h = "00"
            
            if len(h) == 1:
                h = '0' + h
            
            if len(m) == 1:
                m = '0' + m

            if all(digit in digits for digit in h+m):
                return h + ':' + m