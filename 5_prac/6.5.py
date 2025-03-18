from random import randint
import os

def define_winner(data) -> chr:
    if five_moves < 5:
        return "C"
    for row in data:
        if row[0] == row[1] == row[2] != ".":
            return row[0]
    
    for col in range(len(data)):
        if data[0][col] == data[1][col] == data[2][col] != ".": 
            return data[0][col]
    # Прямая диагональ 
    if(data[0][0] == data [1][1] == data[2][2] != "."):
        return data[1][1]
    
    # Обратная диагональ
    if(data[2][0] == data [1][1] == data[0][2] != "."):
        return data[1][1]
    if five_moves > 9: 
        return "D"


def random_move(data):
    success_flag = 0
    while success_flag != 1:
        if all(cell != "." for row in data for cell in row):
            return data
        place = randint(0, 8)
        place_line = place // 3
        place_pos = place % 3
        s = list(data[place_line])
        if s[place_pos] == ".":
            s[place_pos] = "O"
            data[place_line] = "".join(s)
            success_flag =1
    global five_moves 
    five_moves += 1
    return data
    
def print_table(data):
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in data:
        print(line)
        
def meat_move(data):
    success_flag = 0
    while success_flag != 1:
        try:
            meat_line = int(input("Введите номер линии:"))
            meat_pos = int(input("Введдите положение:"))
        except ValueError:
            print("Введите число!")
            continue
        if meat_pos > 3 or meat_pos < 1:
            print("Ошиблись в позиции")
            continue
        if meat_line > 3 or meat_line < 1:
            print("Ошиблись в линии")
            continue
        meat_line -= 1 
        meat_pos -= 1
        s = list(data[meat_line])
        if s[meat_pos] == ".":
            s[meat_pos] = "X"
            data[meat_line] = "".join(s)
            success_flag =1
        else:
            print("На занятую клетку тыкать нельзя")
    global five_moves 
    five_moves += 1
    return data


five_moves = 1
def main():
    data = [
        "...",
        "...",
        "..."
    ]
        
    print_table(data)
    while(1): 
        #Ходит игрок
        meat_move(data)
        if define_winner(data) == "X":
            print_table(data)
            print("Вы победили!")
            break
        elif(define_winner(data) == "D"):
            print_table(data)
            print("Ничья! Надо тренироваться лучше!")
            break
        
        # Ходит робот
        data = random_move(data)
        print_table(data)
        if define_winner(data) == "O":
            print_table(data)
            print("Вы проиграли!")
            break
        elif(define_winner(data) == "D"):
            print_table(data)
            print("Ничья! Надо тренироваться лучше!")
            break
        
        
if __name__ == '__main__':
    main()
