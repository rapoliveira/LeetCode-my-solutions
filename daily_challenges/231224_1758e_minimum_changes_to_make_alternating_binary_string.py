# (c) LeetCode, Raphael A. P. Oliveira
# My solution for the problem 1758, given in this link:
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

# This is my 1st solution (beats 66% in runtime and 6% in memory)
class Solution:
    def minOperations(self, s: str) -> int:
        length = len(s)
        opt_1 = "01" * ((length+1) // 2)
        opt_2 = "10" * ((length+1) // 2)
        opt_1, opt_2 = opt_1[:length], opt_2[:length]

        diff_1 = sum(s[i] != opt_1[i] for i in range(length))
        diff_2 = sum(s[i] != opt_2[i] for i in range(length))

        return min(diff_1, diff_2)