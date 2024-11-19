### 3. Умная сортировка 

def sort_abs_elements(numbers: tuple):
    if (len(numbers) == 0):
        return numbers
    
    numbers_list: list = list(numbers)
    numbers_list.sort(key = lambda x : abs(x))
    
    return numbers_list

def main():
    elements = (-1, -2, -3, 0)
    print(f"Результат: {sort_abs_elements(elements)}")

if __name__=="__main__":
    main()
