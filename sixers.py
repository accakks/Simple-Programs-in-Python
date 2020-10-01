import datetime

def print_header():
    print('----------------------------------')
    print('        Philadelphia 76ers')
    print('----------------------------------')
    print()

def get_days():
    return (datetime.date(2018, 10, 17)-datetime.date.today())

def main():
    print_header()
    print(get_days(), "days!")

main()
