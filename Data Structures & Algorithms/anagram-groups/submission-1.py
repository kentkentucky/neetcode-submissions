class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialise hash map
        res = defaultdict(list)
        # loop through strs
        for i in strs:
            # initialise count array
            count = [0] * 26
            for j in i:
                # count character
                count[ord(j) - ord('a')] += 1
            # append word into hash map using count array as key
            res[tuple(count)].append(i)
        return list(res.values())


            
        