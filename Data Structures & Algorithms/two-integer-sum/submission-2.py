class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checkedMap = {} #pair = {value checked, index}

        for i, value in enumerate(nums):
            difference = target - value
            if difference in checkedMap:
                return [checkedMap[difference], i]
            else:
                checkedMap[value] = i

