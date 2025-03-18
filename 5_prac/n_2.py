### 2. Римские цифры
import ctypes

def int_to_roman(number: int) -> str:
    lib = ctypes.CDLL('./roman_converter.so')
    lib.int_to_roman.restype = ctypes.c_char_p
    return lib.int_to_roman(number).decode('utf-8')

def main():
    number = 13
    print(int_to_roman(number))

if __name__=="__main__":
    main()
