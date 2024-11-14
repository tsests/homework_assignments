### 1. Среднее
### https://github.com/vitaly-efremov/pyteach-tusur-24/blob/main/PyCourses.%20Part%204.ipynb

from random import randint

first_random = randint(0, 100)
second_random = randint(0, 100)
third_random = randint(0, 100)

print(f"Среднее значение для трех случайных чисел {first_random}, {second_random}, {third_random} = {(first_random + second_random + third_random)/3}")