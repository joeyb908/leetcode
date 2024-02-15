# leetcode URL - https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# Use sliding window to get an initial acceptable value. If one match is found,
# increase left pointer once and continuously move left pointer until match isn't found
# anymore. Then move right pointer until new match is found and repeat the process.

def minWindowSubstring(s:str, t:str) -> str:
    if len(t) > len(s):
        return ""
    



print(minWindowSubstring("ADOBECODEBANC", "ABC"))