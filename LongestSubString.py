# author: yprakash
# https://leetcode.com/problems/longest-substring-without-repeating-characters
# https://leetcode.com/submissions/detail/691741223/

class LongestSubString:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0  # Initilize left, right pointers
        longest = 0  # Length of longest substring seen so far
        chars = {}   # HashMap to save characters seen so far

        while r < len(s):
            if s[r] in chars and chars[s[r]] >= l:
                l = chars[s[r]] + 1
            elif longest < 1 + r - l:
                longest = 1 + r - l

            chars[s[r]] = r
            r += 1

        return longest
