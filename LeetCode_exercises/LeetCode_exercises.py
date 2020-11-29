import datetime 

import ex0038_countAndSay as ex38

begin_time1 = datetime.datetime.now()
exsn= ex38.Solution()  
print( exsn.countAndSay(10 )  )
begin_time2 = datetime.datetime.now()
exsn2= ex38.Solution2()  
print( exsn2.countAndSay(10 )  )
begin_time3 = datetime.datetime.now()
print( begin_time2- begin_time1 )
print( begin_time3- begin_time2 )
