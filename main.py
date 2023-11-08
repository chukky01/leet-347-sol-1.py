#THIS IS THE FIRST SOLUTION
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counter = collections.Counter(nums)
    heap = [(v,k) for (k,v) in counter.items()]
    heapq.heapify(heap)
    while len(heap) > k:
      heapq.heappop(heap)
    return[num for(freq, num) in heap]
