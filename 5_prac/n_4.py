
def invert_dict(original_dict):
    values_list:list = list(original_dict.values())
    keys_list:list = list(original_dict.keys())
    
    return dict(zip(values_list, keys_list))

def main():
    book_dict = {'Petr': '546810', 'Katya': '241815'}
    
    print(invert_dict(book_dict))
    

if __name__ == '__main__':
    main()
