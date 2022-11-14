for i in range(90):
    print(" ", end="")

print()
l = ["поесть хлеб", "поиграть в майкнрафт", "почитать Фёдор Михалыча Д."]
for i in range(50):
    print('#', end="")
print()
for task in l:
    len_space = 50 - 2 - len(task) - 1
    print("# ", task, " "*len_space, "#", sep="")
for i in range(50):
    print('#', end="")
print()
print(5, 2)