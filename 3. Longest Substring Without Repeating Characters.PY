# Task - Given a string s, find the length of the longest substring without repeating characters

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


input = "dvdf"

def longestSubstring(input):
    '''find length of longest substring without repeating characters'''
    maxLength = 0  # default max length of 1 since a single character is 1 long
    l, r = 0, 1    # left = start of string, right = left + 1
    strLength = len(input)
    seenCharacters = {}

    if len(input) == 1:
        return 1
    while r < strLength:
        lAscVal = ord(input[l])
        rAscVal = ord(input[r])
        # check to see if l and right pointers are same
        if ord(input[l]) == ord(input[l+1]):
            maxLength = max(1, maxLength)
            l = r
            r += 1
            seenCharacters = {}

        elif ord(input[r]) in seenCharacters.values():
            maxLength = max(maxLength, len(seenCharacters))
            l += 1
            r = l + 1
            seenCharacters = {}
            
        else:
            seenCharacters[l] = ord(input[l])
            seenCharacters[r] = ord(input[r])
            maxLength = max(maxLength, len(seenCharacters))
            r += 1

        

    return maxLength

print(longestSubstring(input))