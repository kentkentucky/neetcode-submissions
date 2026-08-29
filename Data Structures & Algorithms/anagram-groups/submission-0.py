class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through strs
        res = defaultdict(list)
        for i in strs:
            # initialise hash map
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
            res[tuple(count)].append(i)
        return list(res.values())


            
        