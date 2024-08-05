class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for strVal in strs:
            strValSorted = "".join(sorted(strVal))
            
            if strValSorted in anagrams:
                anagrams[strValSorted].append(strVal)
            else:
                anagrams[strValSorted] = [strVal]
            
        totalAnagramList = [anagrams[anagram] for anagram in anagrams]
        return totalAnagramList




strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
result = solution.groupAnagrams(strs)
print(result)
