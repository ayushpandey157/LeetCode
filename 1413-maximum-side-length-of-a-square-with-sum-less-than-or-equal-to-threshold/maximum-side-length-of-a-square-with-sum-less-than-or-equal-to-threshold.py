from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        px = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                px[i][j] = mat[i][j]
        
        # px[i][j] represent the sum from 0,0 to i,j
        for i in range(n):
            for j in range(m):
                px[i][j] = mat[i][j]
                if i > 0:
                    px[i][j] += px[i-1][j]
                if j > 0:
                    px[i][j] += px[i][j-1]
                if i > 0 and j > 0:
                    px[i][j] -= px[i-1][j-1]

        maxi = 0
        
        # l point (i, j)
        for i in range(n):
            for j in range(m):
                # r point (x, y)
                x = i + maxi
                y = j + maxi  # + maxi bcoz if we found our maxi as 1 then we only start looking for sq with greater then maxi side
                while x < n and y < m:
                    # check if sq is valid;
                    sum = px[x][y]
                    if i-1 >= 0:
                        sum -= px[i-1][y]
                    if j-1 >= 0:
                        sum -= px[x][j-1]
                    if i-1 >= 0 and j-1 >= 0:
                        sum += px[i-1][j-1]
                    if sum <= threshold:
                        maxi = x - i + 1
                    x += 1
                    y += 1

        return maxi
