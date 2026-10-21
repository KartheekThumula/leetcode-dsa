class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # will store indices
        
        # Iterate twice to simulate circular array
        for i in range(2 * n):
            current_num = nums[i % n]
            
            # Resolve elements in stack that are smaller than current_num
            while stack and nums[stack[-1]] < current_num:
                res[stack.pop()] = current_num
                
            # Only push indices during the first pass
            if i < n:
                stack.append(i % n)
                
        return res