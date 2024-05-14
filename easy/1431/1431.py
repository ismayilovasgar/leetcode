# 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int):
        max_candies = max(candies)
        return [i + extraCandies >= max_candies for i in candies]


candies = [2, 3, 5, 1, 3]
extraCandies = 3
solution = Solution()
result = solution.kidsWithCandies(candies, extraCandies)
print(result)
# [True, True, True, False, True]
