# 15. 3 Sum
##### Difficulty Level - MEDIUM

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets. 
---

**Example 1:**
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

**Example 2:**
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

**Constraints:**
3 <= nums.length <= 3000
-105 <= nums[i] <= 105


---

# Complexity

- Time complexity:
O(nlogn) due to sorting of the nums array and then.

- Space complexity:
O(1). The result list stores the triplets, but its size is bounded by the number of valid triplets, not the size of the input list nums.

# Code

```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for i,num in enumerate(nums):

            target = num *-1
            left = i+1
            right = len(nums)-1

            while left < right:

                current_sum = nums[left] + nums[right]

                if i>0 and current_sum == target:
                    result.append(num, nums[left], nums[right])
                
                    while left < right and nums[left] ==  nums[left + 1]:
                        left += 1
                    while left < right and nums[right] ==  nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
```