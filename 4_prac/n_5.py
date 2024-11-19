### [Junior+] 5. Полосатые слова 

import re

def count_number_of_striped_words(text: str):
    if (len(text) == 0):
        return 0
    
    vowels = ["A", "E", "I", "O", "U", "Y"]
    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    text = text.upper()

    text_list = list(re.findall(r'\b\w+\b', text))

    words_count = 0

    for word in text_list:
        if not word.isalpha() or len(word) < 2:
            continue
        
        part_one = list(word[::2])  # Символы с чётными индексами
        part_two = list(word[1::2])  # Символы с нечётными индексами

        if (
            all(char in vowels for char in part_one) and all(char in consonants for char in part_two)
        ) or (
            all(char in consonants for char in part_one) and all(char in vowels for char in part_two)
        ):
            words_count += 1


    return words_count    

def main():
    data: str = "Dog,cat,mouse,bird.Human."
    print(f"Результат: {count_number_of_striped_words(data)}")
    
if __name__=="__main__":
    main()
