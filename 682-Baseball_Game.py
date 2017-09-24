class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        my_stack = []
        current = 0
        sum = 0
        
        for op in ops:
            if op == "+":
                current = my_stack[-1] + my_stack[-2]
                my_stack.append(current)
                sum = sum + current
                
            elif op == "D":
                last_valid = my_stack[-1]
                current = last_valid * 2
                my_stack.append(current)
                sum  = sum + current
                
            elif op == "C":
                last_valid = my_stack.pop()
                sum = sum - last_valid
              
            else:   
                current = int(op)
                my_stack.append(current)
                sum = sum + current
            
        return sum