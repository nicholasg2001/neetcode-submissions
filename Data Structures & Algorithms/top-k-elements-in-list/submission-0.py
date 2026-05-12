class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        res = []
        i = 0
        for num, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
            
            if i >= k:
                break
            res.append(num)
            i+=1
        
        return res
