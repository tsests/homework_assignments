### 4. [Junior] Медиана

def calculate_list_median(numbers: list):
    if (len(numbers) == 0):
        return -1
    # Если на входе был tuple
    numbers_list: list = list(numbers)

    numbers_list.sort()

    even_or_odd_len = len(numbers_list) % 2
    index_return = len(numbers_list) // 2
    return numbers_list[index_return] if even_or_odd_len == 1 else ((numbers_list[index_return] + numbers_list[index_return - 1]) / 2)


def main():
    elements = [3, 6, 20, 99, 10, 15]
    print(f"Результат: {calculate_list_median(elements)}")

if __name__=="__main__":
    main()
