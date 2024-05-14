class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i, flower in enumerate(flowerbed):
            if flower == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True

        return False


solution = Solution()
result = solution.canPlaceFlowers([0, 0, 1, 0, 0, 1, 0], 1)
print(result)
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
