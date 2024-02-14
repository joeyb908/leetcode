# You are given a string s and an integer k. You can choose any character of the string and change it to 
# any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above
# operations.

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

# My strategy - Turn the string into a list of tuples with the character and the number of times it appears
# (e.g. "AABABBA":
# A through index 0 - 1 appears 2 times
# B through index 2 - 2 appears 1 time
# A through index 3 - 3 appears 1 time
# B through index 4 - 5 appears 2 times
# A through index 6 - 6 appears 1 time

# I can take index max - index min to find the length of the substring
# Then I can use K to find acceptable places for the character to be replaced working from the longest substrings first.
# In this case, I will start at A at indexes (0,1)
# I can go one to the right (but not left since it's the first substring) and replace B at index 2 with A
# This returns a substring of length 4 --> AAAABBA

# I will then go to index B at indexes (4,5)
# I can go one to the left OR one to the right
# If I change A to the left, I get a substring of length 4 --> AABBBBA
# If I change A to the right, I get a subtring of length 3 --> AABABBB


def longestRepeatingSubstring(s:str, k:int):
    l, r = 0, 1
    repeatedSubstring = []
    i = 0

    while i < len(s):
        count = 0
        while i < len(s) - 1 and s[i] == s[i+1]:
            count += 1
            i += 1

        repeatedSubstring.append((s[i], count + 1))
        i += 1

    print(repeatedSubstring)

longestRepeatingSubstring("AABABBA", 2)