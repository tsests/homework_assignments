### 2. Оценка числа

def estimate_value (value:int):
    if value % 2 != 0:
        print("Плохо")
        return
    if (value >= 2) and (value <= 5):
        print("Неплохо")
    # Проверка на левую границу, так как число может быть меньше нуля(в услоывиях хадаи ничего про это нет)
    elif(value >= 6) and (value <= 20):
        print("Так себе")
    elif(value > 20):
        print("Отлично")

    

user_input: str= input()
user_input_int: int = int(user_input)
estimate_value(user_input_int)

#for i in range(1, 25):
#    print(i, end=" ")
#    estimate_value(i)


