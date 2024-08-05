class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {} # keys = numbers, value= corresponding index
        for i,num in enumerate(nums):
            complement = target - num # opposite of the num
            if complement in seen:# if complement is also present in the object
                return [i, seen[complement]] # [index of num, index of complement]
            seen[num] = i # add the index of num

nums = [2,7,11,15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)