#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum([ord(x) for x in t]) - sum([ord(x) for x in s]))
# @lc code=end

