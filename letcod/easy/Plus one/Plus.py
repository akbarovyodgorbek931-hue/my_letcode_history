class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        son=int("".join(map(str,digits)))
        son+=1
        return list(map(int,str(son)))