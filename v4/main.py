l1 = ["поесть хлеб", "поиграть в майкнрафт", "почитать Фёдор Михалыча Д."]
l2 = ["написать скайнет", "почитать Войну и Мир", ""]
l3 = ["сходить в универ", "снять носки с люстры", "взять 100 интегралов"]
l4 = ["забрать посылку", "", ""]
l5 = ["", "", ""]
l6 = ["простоять в планке 15 минут", "поучить инглиш", "купить новогодний подарок"]
l7 = ["запилить видос про ?", "", ""]
l = [l1, l2, l3, l4, l5, l6, l7]
days = len(l)
for row in range(days//3 + 1):
    if row == days//3:
        r = days%3
    else:
        r = 3
    for j in range(r):
        print("\033[33m{}\033[0m".format("07.07.2022"), end="")
        print(' '*35, end="")
    print()
    for j in range(r):
        print('#'*40, end="")
        print(' '*5, end="")
    print()
    for i in range(len(l1)):
        for j in range(r):
            # print('j = ', j+3*row, row)
            task = l[j+3*row][i]
            len_space = 40 - 2 - len(task) - 1
            print("# ", task, " "*len_space, "#", sep="", end="")
            print(' '*5, end="")
        print()
    for j in range(r):
        print('#'*40, end="")
        print(' '*5, end="")
    print()
    print()
    
# for i in range(50):
#     print('#', end="")
print()
print(5, 2)