class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            consecutive = result = 0
            for n in nums:
                consecutive = consecutive*n+n
                result = max(result, consecutive)
            return result
        