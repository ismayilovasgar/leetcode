# * Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
#
# * Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"


from itertools import zip_longest

# zip_longest( iterable1, iterable2, fillval)
# "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
word1 = "abc"
word2 = "def"
