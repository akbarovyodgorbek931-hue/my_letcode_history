class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lugat = {}
        
        for indeks, son in enumerate(nums):
            farq = target - son
            
            if farq in lugat:
                return [lugat[farq], indeks]
                
            lugat[son] = indeks