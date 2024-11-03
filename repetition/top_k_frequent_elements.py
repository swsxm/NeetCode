from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_ind_list = [[] for _ in range(len(nums))] 
        hashmap = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for key in hashmap:
            freq_ind_list[hashmap[key]-1].append(key)
        ret_vals = []
        print(freq_ind_list)
        for i in range(len(freq_ind_list)-1, -1, -1):
            if len(freq_ind_list[i]) > 0:
                ret_vals.extend(freq_ind_list[i])
            if len(ret_vals) == k:
                return ret_vals
        return []

Test = Solution()
print(Test.topKFrequent(nums=[1,2,2,3,3,3], k=2))

