class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        a = 0
        b = n - 1
        while a <= b:
            mid = ((b - a) // 2) + a
            if nums[mid] < target:
                a = mid + 1
            else:
                b = mid - 1
        if a == n or nums[a] != target:
            return [-1, -1]
        c = a
        d = n - 1
        while c <= d:
            mid = ((d - c) // 2) + c
            if nums[mid] <= target:
                c = mid + 1
            else:
                d = mid - 1
        return [a, d]