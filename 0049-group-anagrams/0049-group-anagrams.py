class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list) # Mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a-z
            for c in s:
                count[ord(c) - ord("a")] += 1 # Mapping from ASCII to 0 - 25

            result[tuple(count)].append(s)
        
        return result.values()