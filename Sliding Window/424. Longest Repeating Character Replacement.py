# leetcode URL - https://leetcode.com/problems/longest-repeating-character-replacement/

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

# More efficient to use a hashmap to store the character and the number of times it appears
# Then use a sliding window and update the hashamp as we go along
# Calculate the max length by taking the max length of all the characters
# while subtracting the highest frequency character from the hashmap
# ex. A - 7, B - 3 would be 10 - 7 = 3. If k = 3, 3 >= 3 so that would work
# allowing us to have a total length of 6
# if k = 2, then 10 - 7 = 3. 3 > 2 so that doesn't work in this case.
# We would then slide the left pointer over one and recalculate.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0 # both left and pointers start at 0 because 1st character will the longest default substring for k=0
        maxSubStringLength = 0
        charCount = {}
        maxFreq = 0 

        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0) # increase count for each character, if it doesn't exist yet, set it to 0
            maxFreq = max(charCount[s[r]], maxFreq) # get the max frequency of whatever character is repeated the most

            # make sure current window for current character is valid (don't need to subtract the current count of whatever letter
            # we're on because it's irrelevant. We only care about the maxFreq throughout the entire operation, we never have to
            # recalculate for a lower value since it would always return a smaller subString length)
            while (r - l + 1) - maxFreq > k: 
                charCount[s[l]] -= 1
                l += 1

            # return max substring length so far from either current max or current window size
            maxSubStringLength = max(maxSubStringLength, r - l + 1)
        return maxSubStringLength