from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        result: list[str] = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])

        return result


solution = Solution()


# Testcase 1
res = solution.findOcurrences("alice is a good girl she is a good student", "a", "good")
print(res, end=" ")
print(res == ["girl", "student"])

# Testcase 2
res = solution.findOcurrences("we will we will rock you", "we", "will")
print(res, end=" ")
print(res == ["we", "rock"])
