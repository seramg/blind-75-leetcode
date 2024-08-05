# 49. Group Anagrams
##### Difficulty Level - MEDIUM

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

**Example 1:**
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

**Example 2:**
Input: strs = [""]
Output: [[""]]

**Constraints:**
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


---


# Intuition
This approach involves traverses through each string in the input list, storing the string in sorted form as the keys of a dictionary. Each key is associated with the original strings that, when sorted, will match the key. Grouping the values based on these keys produces an array of arrays, which can then be returned.

# Approach

1. Initialise a dictionary.
2. Iterate through each string strVal in the input list.
3. Sort the characters of strVal to form a new string val.
4. Check if val already exists as a key in the anagrams dictionary:
    a. If it exists, append the current string strVal to the list associated with the key val in the anagrams dictionary.
    b. If it does not exist, create a new entry in the anagrams dictionary with key val and value as a list containing strVal.
5. Append the list of anagrams associated with each key to the totalAnagramList and return it.


# Complexity

- Time complexity:
O(n * m * log(m)) due to iterating through each string in 'strs', sorting each string which has a time complexity of O(m * log(m)), and then checking if the sorted string exists in the dictionary.

- Space complexity:
O(n * m) due to storing of sorted strings as keys and lists of strings as values.

where 'n' is the number of strings in the input list 'strs' and 'm' is the maximum length of any string in 'strs' 


# Code

```
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for i in range(len(strs)):
            strVal = strs[i]
            val = "".join(sorted(strVal))
            if val in anagrams: 
                anagrams[val].append(strVal)
            else:
                anagrams[val] = [strVal]
        
        totalAnagramList = []
        for anagram in anagrams:
            totalAnagramList.append(anagrams[anagram])
        return totalAnagramList
```