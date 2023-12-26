# (c) LeetCode, Raphael A. P. Oliveira
# My solution for the problem 1496, given in this link:
# https://leetcode.com/problems/path-crossing/

# This is my 1st solution (beats 41% in runtime and 6% in memory)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coords = [(0, 0)]
        for i in range(1, len(path)+1):
            if path[i-1] == 'N':
                coords.append((coords[i-1][0], coords[i-1][1]+1))
            elif path[i-1] == 'S':
                coords.append((coords[i-1][0], coords[i-1][1]-1))
            elif path[i-1] == 'E':
                coords.append((coords[i-1][0]+1, coords[i-1][1]))
            else:
                coords.append((coords[i-1][0]-1, coords[i-1][1]))
            if len(set(coords)) != len(coords):
                return True
        return False
