#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        return len(nums) != len(set(nums))
# @lc code=end

