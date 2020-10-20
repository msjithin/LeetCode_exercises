"""
You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.
"""

'''
////// using SingleLinkedList
inputlist1=[9,9,9,9,9,9,9]
inputlist2=[9,9,9,9]
list1= SingleLinkedList()
list2= SingleLinkedList()
for current_item in inputlist1:
    list1.addLinkedListItem(current_item)
for current_item in inputlist2:
    list2.addLinkedListItem(current_item)
list1.outputList()
list2.outputList()
outList = addTwoNumbers_fn(list1, list2)

///// using ListNode
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(linked_list_str(l1))

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(linked_list_str(l2))

s = Solution()
l3 = s.addTwoNumbers(l1, l2)
print(linked_list_str(l3))
'''

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        return 
    def has_value(self, val):
        "method to compare the value with the node data"
        if self.val == val:
            return True
        else:
            return False
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    def addLinkedListItem(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return
    def listLength(self):
        count=0
        current_node = self.head
        while current_node is not None:
            count+=1
            current_node = current_node.next
        return count
    def outputList(self):
        current_node = self.head
        str_out=''
        while current_node is not None:
            str_out += str(current_node.val)+' -> '
            current_node = current_node.next
        print(str_out)
        return


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None
        return 
# Recursively print linked list
def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)


class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = curr = ListNode(0)
        takeAway = 0

        while l1 or l2 or takeAway:
            v1 = v2 = 0
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2=l2.next
            total = v1 + v2 +takeAway
            takeAway = total //10
            val = total%10
            curr.next = ListNode(val)
            curr = curr.next
        return ret.next
    
def addTwoNumbers_fn(l1 , l2):
    returnList = SingleLinkedList()
    takeAway = 0
    currNode1=l1.head
    currNode2=l2.head
    while currNode1 or currNode2 or takeAway:
        v1 = v2 = 0
        if currNode1 :
            v1=currNode1.val
            currNode1=currNode1.next
        if currNode2:
            v2=currNode2.val
            currNode2=currNode2.next
        total = v1 + v2 +takeAway
        takeAway = total //10
        val = total%10
        returnList.addLinkedListItem(val)
    returnList.outputList()
    return returnList