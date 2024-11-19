### https://github.com/vitaly-efremov/pyteach-tusur-24/blob/main/PyCources.%20Part%206.ipynb
### 1. Последний с четными

def multiply_last_with_even(numbers: list[int]):
    if (len(numbers) == 0):
        return 0
    
    return sum(numbers[::2]) * numbers[-1]

def main():
    numbers_list = [0, 1, 2, 3, 4, 5]
    print(f"Результат: {multiply_last_with_even(numbers_list)}")

if __name__=="__main__":
    main()
