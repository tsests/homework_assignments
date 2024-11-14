### [Junior] 4. Число "наоборот"
### https://github.com/vitaly-efremov/pyteach-tusur-24/blob/main/PyCourses.%20Part%204.ipynb
    
x = -325

if(x < 0):
    x = abs(x)
    x =int('-' + ''.join(reversed(str(x))))
else:
    x =int(''.join(reversed(str(x))))


print(x)



### Случайно сделал не ту функцию, а удалять жалко
#x = cyclic_shift_right(mod_x, len(str(mod_x))-1)
# def cyclic_shift_right(x, shift):
#     x = str(x)
#     result = ""
#     for i in range(len(x)):
#         result += x[(i-shift)%len(x)]
#     return int(result)