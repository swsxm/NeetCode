class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        count = {}
        ret = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num in count:
            freqs[count[num]].append(num)
        while len(ret) != k:
            elements = freqs.pop()
            for element in elements:
                if len(ret) == k:
                    return ret
                ret.append(element)
        return ret
