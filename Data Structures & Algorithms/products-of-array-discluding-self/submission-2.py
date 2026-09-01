class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Gotta get the product of all other values
        # Plan: iterate through list and add to set and like for each index value add the array of all of values then call values array with prod on it
        result = [1] * len(nums)

        # Product of everything to the LEFT
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Product of everything to the RIGHT
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


