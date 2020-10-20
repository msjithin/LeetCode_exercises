from ex1_twoSum import Class_twoSum
from ex2_addTwoNumbers import *
###### two sum
#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.
two_sum = Class_twoSum()
in_list=[2,7,11,15]
target = 9
print(
    two_sum.twoSum(in_list, target)
      )


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


