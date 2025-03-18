### 1. Анализ текста. Популярность.
def analyze_text(input_string: str):
    words_popularity:dict = {}
    chars_popularity:dict = {}

    chars_popularity = dict.fromkeys(input_string, 0)
    words_popularity = dict.fromkeys(input_string.split(), 0)
    
    words_in_text = input_string.split()
    for i in words_in_text:
        words_popularity[i] += 1

    for char in input_string:
        chars_popularity[char] += 1
    return chars_popularity, words_popularity

def main():
    text = "hello, word of word"
    chars_popularity, words_popularity = analyze_text(text)
    print(chars_popularity)
    print(words_popularity)

if __name__=="__main__":
    main()
