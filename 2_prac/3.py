### 2. Деление и еще раз деление
### https://github.com/vitaly-efremov/pyteach-tusur-24/blob/main/PyCourses.%20Part%204.ipynb

from random import randint

first_random = randint(0, 100)
second_random = randint(0, 100)

if second_random != 0:
    print(f"x = {first_random} и y = {second_random}")
    print(first_random//second_random, end="")
    print(", ", end="")
    print(first_random%second_random)
else:
   print("На ноль делить нельзя")
