class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # get rows and columns
        rows, columns = len(boxGrid), len(boxGrid[0])
        # rotate boxGrid
        rotated = [list(row) for row in zip(*reversed(boxGrid))]

        # loop through each column
        for col in range(rows):
            # create a queue
            position = deque()

            # loop through each row bottom up
            for row in range(columns - 1, -1, -1):
                # check for obstacle
                if rotated[row][col] == "*":
                    # clear the queue
                    position.clear()
                # check for stone
                elif rotated[row][col] == ".":
                    # update postion
                    position.append(row)
                # else empty
                elif rotated[row][col] == "#" and position:
                    # get lowest empty position
                    empty = position.popleft()
                    # move stone to lowest empty position
                    rotated[empty][col] = '#'
                    rotated[row][col] = '.'
                    # current position becomes empty after stone falls
                    position.append(row)

        # return rotated
        return rotated