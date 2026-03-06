class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        char, num = coordinates
        return ((ord(char) - 96) + int(num)) % 2 != 0


solution = Solution()

# Testcase 1
res = solution.squareIsWhite("a1")
print(res, end=" ")
print(not res)

# Testcase 2
res = solution.squareIsWhite("h3")
print(res, end=" ")
print(res)

# Testcase 3
res = solution.squareIsWhite("c7")
print(res, end=" ")
print(not res)
