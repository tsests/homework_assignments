### 2. Римские цифры
import ctypes

def int_to_roman(num: int) -> str:
    roman_numerals = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    result = ""
    for value, symbol in roman_numerals.items():
        while num >= value:
            result += symbol
            num -= value
    return result
    # lib = ctypes.CDLL('./roman_converter.so')
    # lib.int_to_roman.restype = ctypes.c_char_p
    # return lib.int_to_roman(number).decode('utf-8')

def main():
    number = 13
    print(int_to_roman(number))

if __name__=="__main__":
    main()
