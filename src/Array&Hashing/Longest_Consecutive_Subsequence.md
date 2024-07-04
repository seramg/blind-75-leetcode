# 128. Longest Consecutive Subsequence
##### Difficulty Level - MEDIUM

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

---

**Example 1:**
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

**Example 2:**
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

**Constraints:**
0 <= nums.length <= 105
-109 <= nums[i] <= 109


---


# Intuition
This approach involves the traversing through each number in the input list. To avoid the duplicates, rather than taking a copy of the array, taking the set of the array is preferred. After iterating through each number in the set, it checks if the number before it exists in order to determine whether this is the start of the sequence. Once we find out the start of the sequence we go on to finding the adjacent elements in the set and then update the length. If the current length is greater, it updates longest with the new length. Finally, it returns the longest length found after iterating through all numbers in the set.

# Approach

1. Initialise a set using the nums array.
2. Iterate through each element in the input array and for each element, check if its previous element is absent in the set in order to confirm whether this element is the start of the sequence.
3. Once we encounter the start element, traverse adjacent elements in the set to extend the sequence. 
4. Increase the sequence length for each consecutive element found.
5. After processing all elements, return the longest consecutive sequence length found.

# Complexity

- Time complexity:
O(n) due to iterating through the set.

- Space complexity:
O(n) due to storing elements in the set.

# Code

```
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
```