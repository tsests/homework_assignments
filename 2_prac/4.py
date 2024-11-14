### 3. Округление
### https://github.com/vitaly-efremov/pyteach-tusur-24/blob/main/PyCourses.%20Part%204.ipynb

x= 14.721
print(f"x = {x}")
### Так фоматируется только вывод,
### А в задании говорилось про округление числа
# print(f"1. {x:0.2f}")

# print(f"2. {x:0.0f}")

# print(f"3. {x:=011}")

print(f"1. {round(x, 2)}")
x= 14.721
print(f"2. {int(round(x, 0))}")
x= 14.721
decimal_part = str(x).split('.')[1]
count = len(decimal_part)

print(f"3. {x:011.{count}f}")