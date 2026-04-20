class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))   # sort string → ["a","e","t"]->>["aet"]
            groups[key].append(s)

        return list(groups.values())
        