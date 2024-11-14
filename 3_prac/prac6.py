### [Junior+] 6. Мир захватили левши

import re

def jokes (commands):
    result = re.sub("right", "bad", ",".join(commands)) # Для проверки автоматики ьуь уюбрал left и поставил bad
    return result


data_in = [
    ["left", "right", "left", "stop"],
    ["bright aright", "ok"],
    ["enough", "jokes"]
]

for i in data_in:
    print(jokes(i))
