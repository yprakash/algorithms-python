# author: yprakash
# https://leetcode.com/problems/valid-palindrome
# https://leetcode.com/submissions/detail/692020512

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]+', '', s).lower()
        n = len(s)
        if n < 2:
            return True
        return next((False for i in range(int(n/2)) if s[i] != s[n-1-i]), True)


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
