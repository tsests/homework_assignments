### [Junior+] 5. Число "наоборот" (усложненное)
### https://github.com/vitaly-efremov/pyteach-tusur-24/blob/main/PyCourses.%20Part%204.ipynb
    
number_value = -1563847412

if(number_value < 0):
    number_value = abs(number_value)
    number_value =int('-' + ''.join(reversed(str(number_value))))
else:
    number_value =int(''.join(reversed(str(number_value))))

if(abs(number_value) > 2147483647):
    number_value = 0

print(number_value)
