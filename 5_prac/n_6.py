def define_winner(data) -> chr:
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
        
    return "D"



def main():
    data = [
        "OOX",
        "XOO",
        "OXX"
     ]
    
    print(define_winner(data))
   
if __name__ == '__main__':
    main()
