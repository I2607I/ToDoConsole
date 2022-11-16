import settings as sts
import datetime
def show():
    l1 = ["поесть хлеб", "поиграть в майкнрафт", "почитать Фёдор Михалыча Д."]
    l2 = ["написать скайнет", "почитать Войну и Мир", ""]
    l3 = ["сходить в универ", "снять носки с люстры", "взять 100 интегралов"]
    l4 = ["забрать посылку", "", ""]
    l5 = ["", "", ""]
    l6 = ["простоять в планке 15 минут", "поучить инглиш", "купить новогодний подарок"]
    l7 = ["запилить видос про ?", "", ""]
    l = [l1, l2, l3, l4, l5, l6, l7]
    days = len(l)
    ROWS = days//sts.COLUMN
    DATE = datetime.date.today()
    date = DATE
    if days%sts.COLUMN != 0:
        ROWS+=1
    for row in range(ROWS):
        if row == days//sts.COLUMN:
            r = days%sts.COLUMN
        else:
            r = sts.COLUMN
        for j in range(r):
            date += datetime.timedelta(days=1)
            res_date = date.strftime("%a %d.%m.%Y")
            print(f'\033[33m{res_date}\033[0m', end="")
            print(' '*31, end="")
        print()
        for j in range(r):
            print(sts.SYMB*40, end="")
            print(' '*5, end="")
        print()
        for i in range(len(l1)):
            for j in range(r):
                # print('j = ', j+3*row, row)
                task = l[j+sts.COLUMN*row][i]
                len_space = 40 - 2 - len(task) - 1
                print(sts.SYMB, ' ', f'\033[41m\033[32m{task}\033[0m', " "*len_space, sts.SYMB, sep="", end="")
                print(' '*5, end="")
            print()
        for j in range(r):
            print(sts.SYMB*40, end="")
            print(' '*5, end="")
        print()
        print()
        
    # for i in range(50):
    #     print('#', end="")
    print()
    print(5, 2)