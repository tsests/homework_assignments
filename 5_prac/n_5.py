def create_currency_dict(dates, rates):
    return dict(zip(dates, rates))


def main():
    dates = ['2017-03-01', '2017-03-02','2017-03-03','2017-03-04', '2017-03-05']
    rates = [55.7, 55.2, 23.1, 54.5, 1.1]
    
    
    print(create_currency_dict(dates, rates))
    

if __name__ == '__main__':
    main()
