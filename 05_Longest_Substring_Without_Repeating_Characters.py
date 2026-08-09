class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = set()
        max_ps = 0
        left = 0

        for right in range(len(s)):
            while s[right] in p:
                p.remove(s[left])
                left += 1
            p.add(s[right])

            max_ps = max(max_ps, right - left + 1)
        return max_ps

s = "abcabcbb"

ps = Solution()
print(ps.lengthOfLongestSubstring(s))
        