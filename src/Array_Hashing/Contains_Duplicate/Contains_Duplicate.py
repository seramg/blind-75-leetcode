class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbersSet = set()

        for num in nums:
            if num in numbersSet:
                return True
            numbersSet.add(num)
        return False

nums = [1,2,3,1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)
