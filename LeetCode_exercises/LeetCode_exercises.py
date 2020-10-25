

import ex11_containerWithMostWater as ex11

ex11_ = ex11.Solution()
height1 = [1,8,6,2,5,4,8,3,7]
height2=[1,1]
height3=[4,3,2,1,4]
height4=[1,2,1]

for height in [height1, height2, height3, height4]:
    print(ex11_.maxArea(height))