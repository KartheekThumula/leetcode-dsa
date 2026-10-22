class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        lo=0
        hi=n-1

        while(lo<=hi):
            mid=int(lo+(hi-lo)/2)

            if nums[mid]==target:
                return mid
            
            if(nums[mid]>= nums[lo]):
                if(nums[lo]<= target and target <= nums[mid]):
                    hi=mid-1
                else:
                    lo=mid+1
                
            if(nums[mid]<=nums[hi]):
                if(nums[mid]<=target and target<=nums[hi]):
                    lo=mid+1
                else:
                    hi=mid-1
            
        return -1

            
