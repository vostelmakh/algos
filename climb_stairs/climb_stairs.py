# https://leetcode.com/problems/climbing-stairs/description/

# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        previous, current = 1, 2
        for _ in range(3, n + 1):
            previous, current = current, previous + current

        return current
