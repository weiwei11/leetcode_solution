#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        else:
            s = f = head
            while f:
                if not s:
                    return False
                s = s.next
                if not f:
                    return False
                f = f.next
                if not f:
                    return False   
                f = f.next
                if s == f:
                    return True
            return False
        
# @lc code=end

