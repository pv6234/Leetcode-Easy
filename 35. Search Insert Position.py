class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        c=-1
        for i in range(len(nums)):
            if target<=nums[i]:
                c = i
                break
        if c==-1:
            c=len(nums)
        return c
