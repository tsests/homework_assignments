### [Junior+] 6. Мир захватили левши

import re

def jokes (commands):
    result = re.sub("right", "left", ",".join(commands)) 
    return result


data_in = [
    ["left", "right", "left", "stop"],
    ["bright aright", "ok"],
    ["enough", "jokes"]
]

for i in data_in:
    print(jokes(i))
