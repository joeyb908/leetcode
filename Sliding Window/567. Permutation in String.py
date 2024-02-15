# leetcode URL - https://leetcode.com/problems/permutation-in-string

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

#In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").


# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Use a hashmap, keep a count of each of the characters. Use a sliding window to progress through string and update hashmap

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        s1Count = {}
        s2Count = {}
        s1Len = len(s1)

        # Create hashmap of s1
        i = 0
        for i in range(len(s1)):
            s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)

        # Create hashmap of s2 within acceptable window
        for r in range(len(s2)):
            s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)


            # If the window is not valid, subtract 1 from
            # left value and increment left value
            if (r - l + 1) > s1Len:
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    del s2Count[s2[l]]
                l += 1

            if s1Count == s2Count:
                return True

        return False