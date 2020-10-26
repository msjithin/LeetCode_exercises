import ex12_integerToRoman as ex12


mysln = ex12.Solution()
for num in [3, 4, 5, 58, 1994, 2513]:
    print(str(num), mysln.intToRoman(num))