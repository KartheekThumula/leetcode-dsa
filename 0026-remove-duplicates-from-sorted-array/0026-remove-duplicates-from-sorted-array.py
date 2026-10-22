class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the list is empty, there are 0 unique elements
        if not nums:
            return 0
            
        # The first element is always unique, so we start inserting at index 1
        insertIndex = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Place the new unique element at the insertIndex
                nums[insertIndex] = nums[i]
                # Move the insertIndex forward
                insertIndex += 1
                
        # insertIndex now holds the count of unique elements
        return insertIndex