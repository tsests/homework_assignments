### 1. Анализ текста. Популярность.
import re
from collections import Counter

def analyze_text(input_string: str):
    text_clean = re.sub(r'[^\w\s]', '', input_string)
    chars = Counter(text_clean.replace(" ", "").lower())
    words = Counter(text_clean.lower().split())
    
    return chars, words

def main():
    text = "hello, word of word"
    chars_popularity, words_popularity = analyze_text(text)
    print(chars_popularity)
    print(words_popularity)

if __name__=="__main__":
    main()
