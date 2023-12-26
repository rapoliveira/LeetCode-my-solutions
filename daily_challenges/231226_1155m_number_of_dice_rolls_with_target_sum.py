# (c) LeetCode, Raphael A. P. Oliveira
# My solution for the problem 1155 (medium), given in this link:
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
from functools import lru_cache  # erase it in LeetCode


# This is my only solution (beats 98% in runtime and 40% in memory)
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        # Got some ideas from dereky4 solution...
        modulo = 10**9 + 7
        one_dice = [num+1 for num in range(k)]

        @lru_cache(None)
        def recursive_dices(n, target):
            if target < n or target > n*k:
                return 0
            if n == 1 or target == n*k:
                return 1

            ans = 0
            for num in one_dice:
                ans += recursive_dices(n-1, target-num)
            return ans % modulo

        return recursive_dices(n, target) % modulo


# if __name__ == "__main__":  # local tests
#     obj_solution = Solution()
#     test_1 = obj_solution.numRollsToTarget(n=1, k=6, target=3)
#     test_2 = obj_solution.numRollsToTarget(n=2, k=6, target=7)
#     test_3 = obj_solution.numRollsToTarget(n=30, k=30, target=500)
#     print('Answers to the three tests:', test_1, test_2, test_3)
