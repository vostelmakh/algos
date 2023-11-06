def longestPalindrome(s: str) -> str:
    if not s:
        return ''

    dp = [1] * len(s)

    for i in range(len(s)):
        for j in range(len(s)):
            if isPalindrome(s[i:j]):
                dp[i] = [i, j]

    p_l = 0

    for i in range(len(dp)):
        p_l_c = dp[i][1] - dp[i][0]
        if (p_l_c > p_l):
            p_l = i

    i = dp[p_l][0]
    j = dp[p_l][1]

    return s[i:j]


def isPalindrome(s):
    return s == s[::-1]


longestPalindrome("a")
