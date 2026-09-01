class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # initialise fast and slow pointer to 0
        slow1 = fast = 0
        # detect cycle
        # loop till slow1 and fast pointer meet
        while True:
            # increment by 1
            slow1 = nums[slow1]
            # increment by 2
            fast = nums[nums[fast]]
            # check for same index
            if slow1 == fast:
                # break out of loop
                break
        # initialise slow2 to 0
        slow2 = 0
        # loop till slow1 and slow2 pointer meet
        while True:
            # increment both slow1 and slow2 pointer by 1 step
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            # check for same index
            if slow1 == slow2:
                # return slow1
                return slow1