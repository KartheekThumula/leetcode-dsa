class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        if n==0:
            return
        k=k%n

        nums[n-k:]=reversed(nums[n-k:])
        nums[:n-k]=reversed(nums[:n-k])
        nums[:]=reversed(nums)

        return nums

    

        
        