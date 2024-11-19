### 2. Max-min Дано: массив чисел (float или/и int)

def calculate_difference_max_min(numbers: list):
    if (len(numbers) == 0):
        return 0
    
    min_naumber = min(numbers)
    max_number = max(numbers)

    return round(max_number - min_naumber, 3)

def main():
    elements_list = [10.28292783, -2.239487, 0, 1.1, 0.5]
    print(f"Результат: {calculate_difference_max_min(elements_list)}")

if __name__=="__main__":
    main()
