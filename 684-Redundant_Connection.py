class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        node_num = len(edges)
        
        # initialize
        my_set = [0]
        for i in range(node_num):
            my_set.append(i+1)
        
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            
            # check if thw two noeds belong to the same group
            if my_set[node1] == my_set[node2]:
                return edge
            
            # union
            else:
                group1 = my_set[node1]
                group2 = my_set[node2]
                
                if group1 > group2:
                    for i in range(1,node_num+1):
                        if my_set[i] == group1:
                            my_set[i] = group2
                else:
                    for i in range(1,node_num+1):
                        if my_set[i] == group2:
                            my_set[i] = group1                               