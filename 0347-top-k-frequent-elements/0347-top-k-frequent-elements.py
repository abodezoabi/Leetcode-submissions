from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for num, freq in count.items():
            heappush(heap, (-freq, num)) 

        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])

        return res