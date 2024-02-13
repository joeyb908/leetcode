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
    maxLength = 0  # default max length
    l, r = 0, 1    # left = start of string, 2nd character in string
    strLength = len(input)
    seenCharacters = set()

    if len(input) == 1:
        return 1
    elif len(input) == 0:
        return 0
    

    while r < strLength:
        # initialize seenCharacters with first character
        if len(seenCharacters) == 0:
            seenCharacters.add(ord(input[l]))

        # check to see if r character has already been seen
        if ord(input[r]) in seenCharacters:
            seenCharacters.remove(ord(input[l]))
            l += 1

            # if we reach end of string
            if l == strLength:
                return max(maxLength, len(seenCharacters))
            
            # if left pointer reaches right pointer and there's more characters
            if l == r:
                r += 1

            seenCharacters.add(ord(input[l]))
            
        # if r character has not been seen, add it to seenCharacters
        else:
            seenCharacters.add(ord(input[r]))
            r += 1

        maxLength = max(maxLength, r - l)

    return maxLength

print(longestSubstring(input))