class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        for i in range(n - 1):
            m = i
            for j in range(i + 1, n):
                if nums[j] < nums[m]:
                    m = j
            nums[i], nums[m] = nums[m], nums[i]
        return nums
   