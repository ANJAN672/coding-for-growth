from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anag_dict=defaultdict(list)
        for s in strs:
            count=[0]*26
            for char in s:
                count[ord(char)-ord("a")]+=1
            key=tuple(count)
            anag_dict[key].append(s)
        return anag_dict.values()