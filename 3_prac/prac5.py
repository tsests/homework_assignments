### [Junior] 5. Три слова

def is_contain_three_words_in_a_row(text_data:str):
    words = text_data.split(' ')
    string_count:int = 0
    true_flag = False

    for word in words:
        if word.isdecimal() == False:
            string_count += 1
            if string_count >= 3:
                true_flag = True
                break
        else:
            string_count = 0
    
    return true_flag

text_data = [
    "Hello World hello",
    "He is 123 man",
    "1 2 3 4",
    "start 5 one two three 7 end"
]

for i in text_data:
    print(is_contain_three_words_in_a_row(i))
