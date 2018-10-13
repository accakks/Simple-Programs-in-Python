import datetime

def print_header():
    print('----------------------------------')
    print('        Philadelphia 76ers')
    print('----------------------------------')
    print()

def get_days():
    print("The 76ers' next game is in ")
    today = datetime.date.today()
    gameday = datetime.date(2018, 10, 17)
    differenceBetweenDates = gameday - today
    return differenceBetweenDates.days

def main():
    print_header()
    print(get_days(), "days!")

main()
