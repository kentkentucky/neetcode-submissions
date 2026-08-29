class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hash map to count numbers
        count = {}
        # loop through nums to count
        for i in nums:
            if (i in count):
                count[i] += 1
            else:
                count[i] = 1
        
        # convert hash map into heap
        heap = []
        for i in count.keys():
            heapq.heappush(heap, (count[i] , i))
            if len(heap) > k:
                heapq.heappop(heap)

        # create array for return
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res