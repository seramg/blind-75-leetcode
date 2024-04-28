# 217. Contains Duplicate
##### Difficulty Level - EASY

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

---


**Example 1:**
Input: nums = [1,2,3,1]
Output: true

**Example 2:**
Input: nums = [1,2,3,4]
Output: false

**Constraints:**
1 <= nums.length <= 105
-109 <= nums[i] <= 109


---


# Intuition
The initial instinct was to directly check adjacent elements for duplicates, but since the array might be unsorted, this approach could be inefficient. Sorting the array first would make duplicates adjacent, but sorting adds a time complexity of O(nlogn).

So, the more efficient approach involves utilizing a set data structure. While iterating through the array, each element is added to the set. If a duplicate is encountered (i.e., if an element already exists in the set), True is returned. If the iteration completes without finding any duplicates, False is returned. This approach has a time complexity of O(n).

# Approach

By sorting
1. Sort the given array.
2. Iterate through the sorted array from the second element onwards.
3. For each element, compare it with the previous element.
4. If the current element is equal to the previous element, return True (indicating a duplicate).
5. If the loop completes without finding any duplicates, return False.

Using set data structure
1. Initialize an empty set to store unique elements encountered so far
2. Iterate through the given array and for each element, check if it exists in the set. If it does, return True (indicating a duplicate)
3. If the element is not in the set, add it to the set.
4. If the loop completes without finding any duplicates, return False.

# Complexity

By sorting
- Time complexity:
O(nlogn) for sorting the array and then iterating through the sorted array takes O(n).

- Space complexity:
O(1) Sorting operation is done in-place and no additional space required.

Using set data structure
- Time complexity:
O(n) The loop iterates through each element once, and set operations like checking membership and adding elements are typically O(1) on average.

- Space complexity:
O(n) The set will store at most n unique elements.


# Code

By sorting
```
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(1,len(nums)):
            prev = nums[i-1]
            curr = nums[i]
            if curr == prev:
                return True
        return False
```


Using set data structure
```
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
# ```
