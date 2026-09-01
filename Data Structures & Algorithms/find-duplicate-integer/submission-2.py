class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # initialise fast and slow pointer to 0
        slow1 = fast = 0
        # detect cycle
        # loop till slow1 and fast pointer meet
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1 == fast:
                break
        # initialise slow2 to 0
        slow2 = 0
        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            if slow1 == slow2:
                return slow1