### Задача [Junior+] 6. Произведение цифр
### https://github.com/vitaly-efremov/pyteach-tusur-24/blob/main/PyCourses.%20Part%203.ipynb

###Немного запутался в заданиях. Это было в файле на GitHub к прошлому заданию. На всякий случай сделал.

def multiply_numbers_in_int(number):
    int(number)
    
    if(number ==0):
        return 0
    
    result = 1

    for i in range(len(str(number))):    
        if(int(str(number)[i]) == 0):
            continue
        else:
            result = result * int(str(number)[i])
    
    return result

number = 0
print(f"Произведение цифр числа {number} = {multiply_numbers_in_int(number)}")