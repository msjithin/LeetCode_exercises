"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For this problem, assume that your function returns 231 − 1 when the division result overflows.
Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:
Input: dividend = 0, divisor = 1
Output: 0
Example 4:
Input: dividend = 1, divisor = 1
Output: 1

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""
class Solution:
    def divide( dividend: int, divisor: int) -> int:
        debug=True
        sign = 1 if divisor*dividend>0 else -1
        divisor, dividend = abs(divisor), abs(dividend)
        if(debug): print('dividend ={} divisor={}'.format(dividend, divisor ))
        quotient = 0
        the_sum = divisor
        outerloop=0
        while the_sum <= dividend:
            outerloop+=1
            if(debug): print('outer loop the_sum={} dividend={} quotient={}'.format(the_sum,dividend,quotient )   )
            current_quotient = 1
            innerloop=0
            while (the_sum + the_sum) <= dividend:
                innerloop+=1
                the_sum += the_sum
                current_quotient += current_quotient
                if(debug): print('     inner loop {}'.format(innerloop))
                if(debug): print('     inner loop the_sum={} current_quotient={}'.format(the_sum, current_quotient )  )
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient
            if(debug): print('outer loop {}'.format(outerloop))
            if(debug): print('end the_sum={} dividend={} quotient={}'.format(the_sum,dividend,quotient )   )
            if(debug): print('*'*10)

        if sign > 0:
            return min(2**31-1 , quotient*sign)
        else :
            return max(-2**31 , quotient*sign)

    def divide_bitwise(self, dividend: int, divisor: int) -> int:
        #With bitwise operators:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1            
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))

class Solution_2:
	def divide( self, x: int, y: int) -> int:    
		sign = 1 if x*y>0 else -1
		x , y = abs(x) , abs(y)
		if (x==-2147483648) and (y==-1): 
			return 1
		v= y
		if x > v:
			 quotient = 1
		elif x == v :
			return 1*sign
		else:
			return 0
		quotient=1
		moves = []
		quotients = []
		while v <= x:
			 moves.append(v)
			 quotients.append(quotient)
			 v+=v
			 quotient+=quotient
		print(len(moves), ' moves',moves)
		print(len(quotients),' quotinets',quotients )

		x-=moves[-1]
		result = quotients[-1]
		print('x to check', x, ' result now=',result)
		i=0
		while x >= y:
			if x - moves[i] >= 0:
				result += quotients[i]
				x -= moves[i]
			print( 'x =',x,'result=', result , ' i ', i , ' y', y)
			i+=1
			if i==len(moves):
				i=0

		if sign >0 :
			return min(2**31 -1 , result)
		else :
			return max( -2**31 , -result)