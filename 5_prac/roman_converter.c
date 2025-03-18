#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* int_to_roman(int num) {
    if (num < 1 || num > 3999) {
        return NULL;
    }

    const char* roman[] = {
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    };
    const int values[] = {
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    };

    char* result = (char*)malloc(20);
    if (!result) {
        return NULL;
    }
    result[0] = '\0';

    int i = 0;
    while (num > 0) {
        while (num >= values[i]) {
            strcat(result, roman[i]);
            num -= values[i];
        }
        i++;
    }

    return result;
}

int main() {
    int number = 3999;
    char* roman = int_to_roman(number);
    if (roman) {
        printf("Число %d в римских цифрах: %s\n", number, roman);
        free(roman);
    } else {
        printf("Ошибка преобразования числа!\n");
    }
    return 0;
}

