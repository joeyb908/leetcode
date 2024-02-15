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

# My solution - Get length of t, the window for length of t can be len(t) + len(t-1)
# ex. t = 3, max length can be 3 + (3 - 1) = 5 long because one character
# has to match at beginning and at end in worst case.

def minWindowSubstring(s:str, t:str) -> str:
    if len(t) > len(s):
        return ""
    
    l, r = 0, 0
    tCount = {}
    sCount = {}
    curMinString = []
    curMinStringLen = 9999999999999

    i=0
    for i in range(len(t)):
        tCount[s[i]] = 1 + tCount.get(s[i], 0)
    
    for r in range(len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r], 0)
 
    
        if tCount in sCount:
            if min(len(s[l:r])) + 1 < curMinStringLen:
                curMinStringLen = len(s[l:r]) + 1
                curMinString = s[l:r]


print(minWindowSubstring("ADOBECODEBANC", "ABC"))