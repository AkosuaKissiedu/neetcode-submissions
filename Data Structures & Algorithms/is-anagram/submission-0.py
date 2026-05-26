class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            slist=list(s)
            ssort = sorted(slist)
            tlist=list(t)
            tsort = sorted(tlist)
            return (ssort == tsort)
        return False