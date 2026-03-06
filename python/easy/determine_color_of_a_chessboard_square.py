class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        char_to_num = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
        }

        char, num = coordinates
        return (char_to_num[char] + int(num)) % 2 != 0


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
