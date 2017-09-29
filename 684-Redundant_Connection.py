class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        my_dict = dict()    # use to store the root

        def findRoot(node):
            # 如果不是自己一組，看是跟誰一組
            while node != my_dict[node]:
                node = my_dict[node]

            return node


        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            
            if node1 not in my_dict:
                my_dict[node1] = node1
            if node2 not in my_dict:
                my_dict[node2] = node1  # set its root to node1

            else:
                root1 = findRoot(node1)
                root2 = findRoot(node2)

                # check if the two nodes belong to the same root
                if root1 == root2:
                    return edge
                
                # union
                else:
                    if root1 > root2:
                        my_dict[root1] = my_dict[root2]
                    else:
                        my_dict[root2] = my_dict[root1]