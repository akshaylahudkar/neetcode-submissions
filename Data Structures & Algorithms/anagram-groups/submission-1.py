class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            cntr = Counter(s)
            f_cntr = frozenset(cntr.items())

            if f_cntr in hm:
                hm[f_cntr].append(s)
            else:
                hm[f_cntr] = [s]

        return list(hm.values())
        