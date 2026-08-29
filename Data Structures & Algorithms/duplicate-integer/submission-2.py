class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # pointer to first no.
        # check for duplicate
        # point pointer to next no.
        # check for duplicate 
        # repeat
        # time complexity = O(n^2)
        # space complexity = 1
        a = 0;
        while(a <= len(nums)):
            for i in range(a + 1, len(nums)):
                print(nums[a], nums[i])
                if (nums[a] == nums[i]):
                    return True;
            a = a + 1;
        return False;
            
            
        
        