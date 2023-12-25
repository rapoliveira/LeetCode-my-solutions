# (c) Raphael A. P. Oliveira, astronomer
# My solution for the problem 91, given in this link:
# https://leetcode.com/problems/decode-ways/

# This is my only solution (beats 92% in runtime and 6% in memory)
class Solution:

    def numDecodings(self, s: str) -> int:

        # My notes...
        # "12" => 2 !!!
        # "226" => 2+2+6 / 2+26 / 22+6 => 3 !!!
        # "06" => 0 because it has two digits and starts with 0
        # "1234" => 1+2+3+4 / 12+3+4 / 12+34 / 1+2+34 => 4 !!!
        # "12345" => 5 - 34/5 - 3/45

        # letters = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 1-26
        # digits_larger = [l for l in s[:-1] if int(l) >= 3]
        # last_digits = 1 if int(s[-2:]) > 26 else 0
        if len(s) == 0 or s[0] == "0":
            return 0
        # return len(s) - s.count('0') - len(digits_larger) - last_digits

        # based on avetik's solution, change later...
        letters = {str(i) for i in range(1, 27)}
        prev, prev_2 = 1, 1

        for i in range(1, len(s)):
            if s[i] == "0" and s[i-1] == "0":  # two consec. zeroes
                return 0
            if s[i] != "0" and s[i-1:i+1] in letters:
                prev_2, prev = prev, prev_2 + prev
            elif s[i] != "0":
                prev_2, prev = prev, prev
            elif s[i-1:i+1] not in letters:
                return 0
            else:
                prev_2, prev = prev_2, prev_2
        return prev
