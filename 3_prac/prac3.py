### 3. Последовательность
def main():
    user_input_int: int = 0
    while user_input_int < 1 or user_input_int > 9:
        user_input: str = input()
        user_input_int = int(user_input)
    
    for i in range(user_input_int):
        print(i+1, end = "")
    
    # У меня без этого переноса появляеьтся символ терминала в конце строки.
    print()

if __name__ == "__main__":
    main()
