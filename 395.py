class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for char in set(s):
            if s.count(char) < k:
                return max([self.longestSubstring(i,k) for i in s.split(char)])
        return len(s)
        
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87748/Java-O(n2)-iterator-and-backtracking-solution.