class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cout={}
        for i in nums:
            cout[i]=cout.get(i,0)+1
        frequent_list=[[]for i in range(nums)]
        for key in cout:
            frequent_list[cout[key]-1].append(key)
        
        for 