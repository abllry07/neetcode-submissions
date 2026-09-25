class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # recommended time + space = O(n)

        checkedMap = {} # key = index, value = num @ index

        for i, value in enumerate(nums):
            difference = target - value
            if difference in checkedMap:
                return [checkedMap[difference], i]
            checkedMap[value] = i
