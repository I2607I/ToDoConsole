l1 = ["поесть хлеб", "поиграть в майкнрафт", "почитать Фёдор Михалыча Д."]
l2 = ["написать скайнет", "почитать Войну и Мир", ""]
l3 = ["сходить в универ", "снять носки с люстры", "взять 100 интегралов"]
l = [l1, l2, l3]
days = len(l)
for j in range(days):
    print("07.07.2022", end="")
    for i in range(35):
        print(' ', end="")
print()
for j in range(days):
    for i in range(40):
        print('#', end="")
    for i in range(5):
        print(' ', end="")
print()
for i in range(len(l1)):
    for j in range(days):
        task = l[j][i]
        len_space = 40 - 2 - len(task) - 1
        print("# ", task, " "*len_space, "#", sep="", end="")
        for k in range(5):
            print(' ', end="")
    print()
for j in range(days):
    for i in range(40):
        print('#', end="")
    for i in range(5):
        print(' ', end="")
print()
    
# for i in range(50):
#     print('#', end="")
print()
print(5, 2)