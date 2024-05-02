# 242. Valid Anagram
##### Difficulty Level - EASY

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


---


**Example 1:**
Input: s = "anagram", t = "nagaram"
Output: true

**Example 2:**
Input: s = "rat", t = "car"
Output: false

**Constraints:**
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


---


# Intuition
The initial instinct was to directly sort both strings and check for mismatches in characters based on their index values. So, the initial steps involved checking the lengths of both strings, sorting them, and then comparing them character by character, resulting in a time complexity of O(nlogn).

However, to avoid the unnecessary sorting of the two strings, a more efficient approach was devised. This approach involves counting the frequency of each character in one string and then decrementing the count based on the corresponding character frequency in the other string. In a valid anagram, this process will yield counts of zero for all characters. Any non-zero count indicates the presence of an invalid character, thus identifying an invalid anagram. This optimized method operates in linear time, O(n).

So, instead of sorting, we utilize character frequency counts to efficiently determine if two strings are anagrams of each other.

# Approach

By sorting
1. Compare the lengths of the two input strings, s and t. If they have different lengths, return False immediately, indicating that they cannot be anagrams.
2. Sort both strings s and t.
3. Compare each character in the sorted strings. If any character at the same position in both strings does not match, return False, indicating that they are not anagrams.
4. If all characters match at their respective positions in both strings, return True, indicating that they are anagrams.

By finding frequency of each character
1. Compare the lengths of the two input strings, s and t. If they have different lengths, return False immediately, indicating that they cannot be anagrams.
2. Initialise a dictionary to keep track of the frequency of each character in the first string, s.
3. Run a loop through the second string and decreement the frequency of each character.
4. Iterate through each character in the second string, t, and decrement the corresponding character frequency in the dictionary.
5. After iterating through all characters in t, if the frequency of all characters in the dictionary becomes zero, it indicates that t contains exactly the same characters as s, albeit possibly in a different order, making them anagrams. In this case, return True.
6. If during the iteration, the frequency of any character becomes zero, it means t contains a character that is not present in s or contains the character more times than in s, which breaks the anagram condition. In such a scenario, return False.

# Complexity

By sorting
- Time complexity:
O(nlogn) for sorting the strings and then iterating through the sorted array takes O(n).

- Space complexity:
O(n) for storing the sorted versions of the input strings.

By finding frequency of each character
- Time complexity:
O(n) The loop iterates through each element in both the strings, and set operations like checking membership and adding elements are typically O(1) on average.

- Space complexity:
O(1) the space is utilised for dictionary.


# Code

By sorting
```
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sLen = len(s)
        tLen = len(t)

        if sLen != tLen:
            return False
        else:
            sortedS = ''.join(sorted(s))
            sortedT = ''.join(sorted(t))

            indexOfT = 0
            for characterInS in sortedS:
                if characterInS != sortedT[indexOfT]:
                    return False
                indexOfT = indexOfT + 1
            return True

```


By finding frequency of each character
```
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        characterFreqDict = {}
        sLen = len(s)
        tLen = len(t)

        if sLen != tLen:
            return False
        else:
            for characterInS in s:
                if characterInS in characterFreqDict:
                    characterFreqDict[characterInS] = characterFreqDict[characterInS] + 1
                else:
                    characterFreqDict[characterInS] = 1
            
            for characterInT in t:
                if characterInT in characterFreqDict:
                    characterFreqDict[characterInT] = characterFreqDict[characterInT] - 1

            for value in characterFreqDict.values():
                if value != 0:
                    return False
            return True

```