

import ex9_palindromeNumber as ex9

exsln = ex9.Solution()

print( exsln.isPalindrome(121)  )

import ex4_medianOfTwoSortedArrays as ex4

input_arrays=[ [[1,3], [2]], [ [1,2], [3,4]], [[0,0], [0,0]], [[], [1]], [[2],[]], [[1,1], [1,2]]]

ex = ex4.Solution()
for ar in input_arrays:
    print('input arrays : ', ar[0], ar[1])
    print('   median :', ex.findMedianSortedArrays(ar[0], ar[1])   )