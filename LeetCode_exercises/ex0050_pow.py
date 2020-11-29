"""
    Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

"""
class Solution:
    def myPow( x: float, n: int) -> float:
        print(' Calcuating {} ^ {}'.format(x, n)  )
        if x==0:
            return 0
        if n==0:
            return 1
        if abs(x) == 1.0:
            return 1 if n%2==0 else x
        num = x
        npow = abs(n)
        f_out=1
        counter=0
        while npow>0:
            if f_out==0:
                break
            tmp , tmpf_out=1, num
            while tmp+tmp < npow :
                counter+=1
                if tmp==0 or tmpf_out==1 :
                    break
                tmp+=tmp
                tmpf_out*=tmpf_out
            counter+=1
            npow-=tmp
            f_out *= tmpf_out
        print(' outer loop counter = ', counter , 'f_out=', f_out,'')
        if n < 0:
            return 1/f_out
        
        return f_out

class Solution2:
    def myPow( x: float, n: int) -> float:    
        print('calculate {} ^{}'.format(x,n))
        if n<0:
            x = 1/x
            n = -n
        if abs(x)==1:
            return 1 if n%2==0 else x
        res = 1
        current_product = x
        while n>0:
            if current_product==0 or current_product==1:
                res=current_product
                break
            if n%2:
                res *= current_product
            current_product *= current_product
            n=n//2        
        return res