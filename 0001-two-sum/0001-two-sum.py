class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # i=0
        # while(i<len(nums)):
        #     j=i+1
        #     print(i,j)
        #     i+=1
        #     while(j<len(nums)):
        #         j+=1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                # print(i,j)
                if nums[i]+nums[j]==target:
                    return [i,j]