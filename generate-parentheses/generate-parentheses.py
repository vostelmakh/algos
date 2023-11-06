from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(opened, closed, current):
            if opened + closed == 2 * n:
                result.append(current)
                return

            if opened < n:
                generate(opened + 1, closed, current + "(")

            if closed < opened:
                generate(opened, closed + 1, current + ")")

        generate(0, 0, "")

        return result
