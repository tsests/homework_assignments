### 1. Fizz Buzz

def fizz_buzz (value:int):
    Fizz: int = 3
    Buzz: int = 5
    if (value % Fizz == 0) and (value % Buzz == 0):
        print("Fizz Buzz")
    elif value % Fizz == 0:
        print("Fizz")
    elif value % Buzz == 0:
        print("Buzz")
    else:
        print(value)
    
def main():
    user_input: str = input()
    user_input_int: int = int(user_input)
    abs_user_input_int: int = abs(user_input_int)
    fizz_buzz(abs_user_input_int)
    
if __name__ == "__main__":
    main()
