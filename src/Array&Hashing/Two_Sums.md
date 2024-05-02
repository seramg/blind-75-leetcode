# 1. Two Sums
##### Difficulty Level - EASY

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---

**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**
Input: nums = [3,2,4], target = 6
Output: [1,2]

**Constraints:**
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


---


# Intuition
This approach involves the traversing through each number in the input list, storing each number's index in a dictionary. As it traverses, it calculates the complement required to achieve the target sum by subtracting the current number from the target. If the complement is found in the dictionary, it indicates that a pair of numbers exists in the list whose sum equals the target. In this case, the algorithm returns the indices of both the current number and its complement from the dictionary, providing the positions of the two numbers that sum up to the target. 

# Approach

1. Initialise a dictionary to store the elements of the input as keys and their corresponding indices as values.
2. Run a loop through the input and for each element value at index i, we find the complement of the current element value with respect to the target by subtracting value from target.
3. If complement is found in dictionary, it means that we have found two elements whose sum equals the target. In this case, return a list containing the indices of the current element i and the index of the element stored in seen[complement].
4. If complement is not found in seen, add the current element value as a key to the seen dictionary with its index i as the value.

# Complexity

- Time complexity:
O(n) due to iterating through the list once.

- Space complexity:
O(n) due to storing elements in the dictionary, which can have at most 'n' elements.

# Code

```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i,value in enumerate(nums):
            complement = target - value

            if complement in seen:
                return [i, seen[complement]]
            
            seen[value] = i
```