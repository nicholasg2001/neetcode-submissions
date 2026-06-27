class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            ans[tuple(count)].append(s)
        
        return list(ans.values())
    
        #O(m * n) runtime M = num of S in strs, N = avg len of S in Strs


        