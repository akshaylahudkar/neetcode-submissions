class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for i in s:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        for i in t:
            if i not in hm:
                return False
            else:
                hm[i] -= 1
                if hm[i] < 0:
                    return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    

            