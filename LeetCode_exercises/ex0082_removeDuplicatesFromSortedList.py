"""
    Given a sorted linked list, delete all nodes that have duplicate numbers, 
    leaving only distinct numbers from the original list.
    Return the linked list sorted as well.
    Example 1:
    Input: 1->2->3->3->4->4->5
    Output: 1->2->5
    Example 2:
    Input: 1->1->1->2->3
    Output: 2->3
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        res = {}
        while head:
            if head.val not in res:
                res[head.val] = 1
            else:
                res[head.val] += 1
            head = head.next
        #print(res)
        head_node = ListNode(0)
        current = head_node 
        for key,val in res.items():
            if val == 1:
                new_node = ListNode(key)
                current.next = new_node
                current = new_node 
        return head_node.next
