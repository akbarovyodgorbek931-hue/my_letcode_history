class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        javob = []

        for i in range(len(words)):
            if x in words[i]:
                javob.append(i)

        return javob