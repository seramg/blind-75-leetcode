class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sLen = len(s)
        tLen = len(t)

        if sLen != tLen: # not a valid anagram
            return False
        else:
            sortedS = ''.join(sorted(s))
            sortedT = ''.join(sorted(t))

            for indexOfT,characterInS in enumerate(sortedS):
                if characterInS != sortedT[indexOfT]:
                    return False
            return True


s = "anagram"
t = "nagaram"
solution = Solution()
result = solution.isAnagram(s, t)
print(result)
