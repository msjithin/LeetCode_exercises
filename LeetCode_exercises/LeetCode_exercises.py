

import ex0014_longestCommonPrefix as ex14

mysln = ex14.Solution()
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
strs3 = ["dog","dog3",""]
strs4 = ["dog1","dog3","dog4"]
strs5 = ["a"]
strs6 = ["flower", "flower","flower","flower","flower"]
strs7 =  ["flowereee","flow","flighteee", "someth", "flow"]
for strs in [strs1, strs2, strs3, strs4, strs5, strs6, strs7]:
    print('input ', strs, 'output' , mysln.longestCommonPrefix_2(strs)   )