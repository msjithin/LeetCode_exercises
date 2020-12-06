"""
Given the head of a linked list, rotate the list to the right by k places.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 0
        current = head
        while current :
            length += 1
            current = current.next
        #print('length found = ', length)
        if length<2 or k == 0:
            return head
        positionToMove = length - k%length 
        #print('position to move =', positionToMove)
        tmp = ListNode(0)
        current = tmp
        while positionToMove>0:
            newNode = ListNode(head.val)
            #print(newNode)
            current.next = newNode
            current = newNode
            positionToMove -= 1
            head = head.next
        #print('tmp=', tmp)
        current = head
        while current:
            if current.next is None:
                current.next = tmp.next
                break
            current = current.next
        if not current:
            return tmp.next
        return head
    
    
    
    
