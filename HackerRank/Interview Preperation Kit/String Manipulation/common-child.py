
import math
import os
import random
import re
import sys

# def commonChildHelper(s1, s2, total):
#     if not s1 or not s2:
#         return total
#     if s1[0] == s2[0]:
#         return commonChildHelper(s1[1:], s2[1:], total + 1)
#     else:
#         return max(commonChildHelper(s1[1:], s2, total), commonChildHelper(s1, s2[1:], total))

# Complete the commonChild function below. - instance of the longest common subsequence problem
def commonChild(s1, s2):
    solution = [[None]*(len(s1) + 1) for _ in xrange(len(s1) + 1)]
    for x in xrange(len(s1) + 1):
        for y in xrange(len(s1) + 1):
            if x == 0 or y == 0:
                solution[x][y] = 0
            elif s1[x - 1] == s2[y - 1]:
                solution[x][y] = solution[x - 1][y - 1] + 1
            else:
                solution[x][y] = max(solution[x][y-1], solution[x-1][y])
    return solution[-1][-1]

if __name__ == '__main__':

    s1 = "SHINCHAN"
    s2 = "NOHARAAA"
    print commonChild(s1, s2), s1, s2
