class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums) #takes out all the duplicates
        longest = 0 #starting with the min value

        for num in numSet:
            if (num-1) not in numSet: #to just check if num is the starting point
                length = 1 # start the sequence
                while (num+length) in numSet: # if all elements from num to the longest sequence is there
                    length = length+1 # increase length as we go
                longest = max(longest,length) #find the maximum length
        return longest

nums = [0,3,7,2,5,8,4,6,0,1]
solution = Solution()
result = solution.longestConsecutive(nums)
print(result)