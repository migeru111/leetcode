class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        solution1
        arrayをループ
        0が来たらそれ以降の数字を一つずつ前にコピー。末尾に０を挿入
        これを繰り返す。
        ループに対して、0の個数分毎回他の数字を移動する必要がある。
        sol2
        ループして0が来たらカウントする。
        0以外の数字の時にカウントの数分左におく。
        末尾からカウントした分だけ0で置換する
        """
        len_nums=len(nums)
        if len_nums==1:
            return
        
        zero_cnt=0

        for i in range(len_nums):
            if nums[i] ==0:
                zero_cnt+=1
            else:
                if zero_cnt!=0:
                    nums[i-zero_cnt]=nums[i]
        if zero_cnt!=0:
            for i in range(zero_cnt):
                nums[-(i+1)]=0

        print(nums)

nums1 = [0,1,0,3,12]

sol=Solution()
sol.moveZeroes(nums1)
