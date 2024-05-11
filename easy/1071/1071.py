# Example 1:
# # Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# # Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def control(s1: str, s2: str):
            while s1.startswith(s2):
                s1 = s1[len(s2):]
            return s1

        if len(str2) > len(str1):
            return self.gcdOfStrings(str2, str1)
        if not str1.startswith(str2):
            return ""
        if not str2:
            return str1
        return self.gcdOfStrings(str2, control(str1, str2))

# sol = Solution()
# print(sol.gcdOfStrings("ABCABCABC", "ABC"))
