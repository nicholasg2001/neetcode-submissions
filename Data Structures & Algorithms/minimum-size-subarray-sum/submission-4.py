class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        currSum = 0
        l = 0 
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                res = min(r-l+1, res)
                currSum -= nums[l]
                l+=1

        return 0 if res == float("inf") else res