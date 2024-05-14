class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        mylist = [i for i in s if i in vowels]
        mylist.reverse()
        count = 0
        r = ""
        for i in s:
            if i in vowels:
                i = mylist[count]
                count += 1
            r += i
        return r


solution = Solution()
print(solution.reverseVowels("hello"))
print(solution.reverseVowels("leetcode"))
