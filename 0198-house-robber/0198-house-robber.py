class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 keeps track of the max money up to two houses ago (i-2)
        # rob2 keeps track of the max money up to the previous house (i-1)
        rob1, rob2 = 0, 0
        
        for n in nums:
            # Calculate the max if we rob the current house (n + rob1)
            # vs if we skip it and keep the previous max (rob2)
            current_max = max(rob1 + n, rob2)
            
            # Shift our pointers forward for the next iteration
            rob1 = rob2
            rob2 = current_max
            
        return rob2