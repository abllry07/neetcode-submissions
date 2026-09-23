class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checkedMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in checkedMap:
                return [checkedMap[diff], i]
            checkedMap[n] = i
    
        return 

