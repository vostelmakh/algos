from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0

    dp = [1] * len(nums) 

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


print(lengthOfLIS([10,9,2,5,3,7,101,18]))