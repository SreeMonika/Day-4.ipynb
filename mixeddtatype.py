mixedatatypelist = [34,"abc",True,433.4,4+3j]
print((type(mixedatatypelist)))
for item in mixedatatypelist:
 print("{} is of the data type {}".format(item,type(item)))