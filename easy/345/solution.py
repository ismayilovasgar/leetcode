class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        mylist = [i for i in s if i.lower() in vowels]
        mylist.reverse()
        count = 0
        r = ""
        for i in s:
            if i.lower() in vowels:
                i = mylist[count]
                count += 1
            r += i
        return r


solution = Solution()
print(solution.reverseVowels("hello"))
print(solution.reverseVowels("leetcode"))


# 1-)
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         v='aeiouAEIOU'
#         a=[]
#         str=""
#         for i in s:
#             if(i in v):
#                 a.append(i)
#         b=a[::-1]
#         j=0
#         for i in s:
#             if(i not in v):
#                 str=str+i
#             else:
#                 str=str+b[j]
#                 j+=1
#         return str


#2-)
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         test = list(s)
#         leftHasVowel = False
#         rightHasVowel = False
#         changedVowels = False
#         leftPointer = 0
#         rightPointer = len(test)-1
#         while(leftPointer < rightPointer):
#             if test[leftPointer].lower() in ('a', 'e', 'i', 'o', 'u'):
#                 leftHasVowel = True
#             else:
#                 leftPointer = leftPointer + 1
#             if s[rightPointer].lower() in ('a', 'e', 'i', 'o', 'u'):
#                 rightHasVowel = True
#             else:
#                 rightPointer = rightPointer - 1
#             if  leftHasVowel and rightHasVowel:
#                 help = s[leftPointer]
#                 test[leftPointer] = test[rightPointer]
#                 test[rightPointer] = help
#                 leftHasVowel = False
#                 rightHasVowel = False
#                 rightPointer = rightPointer - 1
#                 leftPointer = leftPointer + 1
#         return "".join(test)


#3-)
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels = set('aeiouAEIOU')
#         s = list(s)
#         m = len(s)
#         start = 0
#         end = m-1

#         while start < end:

#             while start < end and s[start] not in vowels:
#                 start += 1
#             while start < end and s[end] not in vowels:
#                 end -= 1    

#             s[start], s[end] = s[end], s[start]
#             start,end = start+1, end-1

#         return ''.join(s)    