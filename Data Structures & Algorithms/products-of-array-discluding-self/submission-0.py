class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #result --> array of products of numbers excluding one in index

        preProd = [1] * len(nums)
        postProd = [1] * len(nums)

        postProd[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            preProd[i] = preProd[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            postProd[i] = postProd[i + 1] * nums[i + 1]

        result = [1] * len(nums) 
        for i in range(0, len(nums)):
            result[i] = preProd[i] * postProd[i]

        return result

        # [1, 2, 4, 6] -- nums
        # preProd -- [1, 1, 2, 8]
        # postProd -- [, 6]
        