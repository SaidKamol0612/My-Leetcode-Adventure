class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        hm = {}

        for i, word in enumerate(words):
            if pattern[i] in hm:
                if hm[pattern[i]] != word:
                    return False
            else:
                if word in hm.values():
                    return False

                hm[pattern[i]] = word
        return True


solution = Solution()


# Testcase 1
res = solution.wordPattern("abba", "dog cat cat dog")
print(res, end=" ")
print(res)

# Testcase 2
res = solution.wordPattern("abba", "dog cat cat fish")
print(res, end=" ")
print(not res)

# Testcase 3
res = solution.wordPattern("aaaa", "dog cat cat dog")
print(res, end=" ")
print(not res)
