class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==k==1:
            return nums[0]
        search_range_max=len(nums)-k
        max_sum=sum(nums[0:k])
        
        for i in range(search_range_max+1):
            sum_temp=sum(nums[i:i+k])
            if max_sum < sum_temp:
                max_sum=sum_temp
            
        return max_sum/k
            
            
