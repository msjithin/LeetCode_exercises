

import ex8_stringToInteger as ex8

ex8sln = ex8.Solution()
in_strings=["42", "  -42", "4193 with words", "words and 987", "-91283472332", "3.1459", "+-12",  ".1", "00000-42a1234", " 004.345 " ,""]

for myString in in_strings:
    print("input: {} , output : {} ".format(myString, ex8sln.myAtoi(myString))    )



