# 125. Valid Palindrome
##### Difficulty Level - EASY

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

---

**Example 1:**
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

**Example 2:**
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

**Constraints:**
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


---

# Complexity

- Time complexity:
O(n) due to iterating through the string.

- Space complexity:
O(n) due to storing alphabets and numbers in the string.

# Code

```
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphaNumericStr = ""
        for str in s:
            if (str >= 'a' and str <= 'z') or 
            (str >= 'A' and str <= 'Z' ) or 
            (str >= '0' and str <= '9'):
                alphaNumericStr += str.lower()
        return alphaNumericStr == alphaNumericStr[::-1]
```