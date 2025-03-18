
def find_min_rate_bank(rates_dict):
    if not rates_dict:  # Если словарь пустой
        return set()
    values:list = rates_dict.values()
    
    min_value:int = min(values)
    
    return {i: rates_dict[i] for i in rates_dict if rates_dict[i] == min_value}


def main():
    rates_dict = {'Sberbank': 55.8, 'VTB24': 53.91, 'MyBank': 53.91, 'Name': 98.99}
    
    result = find_min_rate_bank(rates_dict)

    for bank, rate in result.items():
        print(f"{bank} -> {rate}")
        
    

if __name__ == '__main__':
    main()
