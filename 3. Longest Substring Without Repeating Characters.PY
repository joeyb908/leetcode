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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = 0  # default max length of 1 since a single character is 1 long
        l, r = 0, 1    # left = start of string, right = left + 1
        strLen = len(s)
        seenCharacters = set()

        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        
        while r < strLen:
            # initialize seenCharacters
            if len(seenCharacters) == 0:
                seenCharacters.add(ord(s[l]))
                
            # check to see if r character has already been seen
            if ord(s[r]) in seenCharacters:
                seenCharacters.remove(ord(s[l]))
                l += 1
                
                # reach end of string
                if l == strLen:
                    return max(maxLength, len(seenCharacters))
                
                # if left pointer meets right pointer but we're not at end of string
                if l == r:
                    r+=1
                    
                seenCharacters.add(ord(s[l]))

            # right character not seen yet, add it to set
            else:
                seenCharacters.add(ord(s[r]))
                r += 1
                
            # gets max length at end if last character is not repeated
            maxLength = max(maxLength, r - l)

        return maxLength