# leetcode URL - https://leetcode.com/problems/sliding-window-maximum/description/

# You are given an array of integers nums, there is a sliding window of size k which is
# moving from the very left of the array to the very right. You can only see the k 
# numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

import collections


def maxSlidingWindow(nums, k):
    output = []
    q = collections.deque() # stores index values, not actual value
    l,r = 0, 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l+=1

        r+=1

    return output

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))