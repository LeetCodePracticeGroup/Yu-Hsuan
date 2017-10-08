class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        my_stack = []
        isVisited = []
        count = 1
        max_island = 1
        flag = 0

        for item in grid:
            if 1 in item:
                flag = 1
                break

        if flag == 0:
            return 0


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if [i,j] in isVisited:
                        continue
                    else:
                        isVisited.append([i,j])
                    
                    my_stack.append([i,j])

                    while len(my_stack) != 0:
                        item = my_stack.pop()

                        # go up
                        if item[0]-1 != -1 and grid[item[0]-1][item[1]] == 1 and [item[0]-1, item[1]] not in isVisited:

                            isVisited.append([item[0]-1, item[1]])
                            my_stack.append([item[0]-1, item[1]])

                            count = count + 1
                        
                        # go down
                        if item[0]+1 != len(grid) and grid[item[0]+1][item[1]] == 1 and [item[0]+1, item[1]] not in isVisited:

                            isVisited.append([item[0]+1, item[1]])
                            my_stack.append([item[0]+1, item[1]])

                            count = count + 1

                        # go right
                        if item[1]+1 != len(grid[i]) and grid[item[0]][item[1]+1] == 1 and [item[0], item[1]+1] not in isVisited:

                            isVisited.append([item[0], item[1]+1])
                            my_stack.append([item[0], item[1]+1])

                            count = count + 1
                            
                        # go left
                        if item[1]-1 != -1 and grid[item[0]][item[1]-1] == 1 and [item[0], item[1]-1] not in isVisited:

                            isVisited.append([item[0], item[1]-1])
                            my_stack.append([item[0], item[1]-1])

                            count = count + 1

                    if count > max_island:
                        max_island = count
                    
                    count = 1

        return max_island