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
    if len(t) > len(s) or t == "":
        return ""
    
    countT, window = {}, {}
    res, resLen = [-1, -1], float("infinity")
    l = 0
    # initialize count hashmap of t
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    # have is number of characters in s that matches t, need is number of characters needed to match t
    have, need = 0, len(countT)

    # iterate through s with r pointer incrementing after each loop
    for r in range(len(s)):

        # current character
        c = s[r]

        # add current character to window hashmap
        window[c] = 1 + window.get(c, 0)

        # if character is in the countT hashmap and the count in window matches the count in countT
        # increment have by 1
        if c in countT and window[c] == countT[c]:
            have += 1

        # as long as have is equal to need
        # compare the current window length match to the length of current minimum result and take the min
        while have == need:
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            
            # decrement the window count of the character at the left pointer
            # if the left pointer in string s is in countT AND
            # if by removing the character at the left of the window and the count is smaller than it's supposed to be, decrement have by 1
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1

            l += 1

    l, r = res

    if resLen != float("infinity"):
        return s[l:r+1]
    else:
        return ""

print(minWindowSubstring("ADOBECODEBANC", "ABC"))