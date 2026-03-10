class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        first_height = 0

        r = red
        b = blue

        while r > first_height or b > first_height:
            first_height += 1
            r -= first_height
            if r < 0:
                first_height -= 1
                break

            first_height += 1
            b -= first_height
            if b < 0:
                first_height -= 1
                break

        second_height = 0

        while red > second_height or blue > second_height:
            second_height += 1
            blue -= second_height
            if blue < 0:
                second_height -= 1
                break

            second_height += 1
            red -= second_height
            if red < 0:
                second_height -= 1
                break

        return max(first_height, second_height)


solution = Solution()


# Testcase 1
res = solution.maxHeightOfTriangle(2, 4)
print(res, end=" ")
print(res == 3)

# Testcase 2
res = solution.maxHeightOfTriangle(2, 1)
print(res, end=" ")
print(res == 2)

# Testcase 3
res = solution.maxHeightOfTriangle(1, 1)
print(res, end=" ")
print(res == 1)

# Testcase 4
res = solution.maxHeightOfTriangle(10, 1)
print(res, end=" ")
print(res == 2)
