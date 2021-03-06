'''
Time:  O(n)
Space: O(k)

Given an array nums, there is a sliding window of size k
which is moving from the very left of the array to the
very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Q,result = [],[]
        for i, n in enumerate(nums):
            while Q and nums[Q[-1]]<n:
                Q.pop()
            Q.append(i)
            if Q[0] == i-k:
                Q.pop(0)
            if i >= k-1:
                result+=nums[Q[0]],
        return result