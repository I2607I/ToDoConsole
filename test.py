import requests

# put your python code here
a = input()
#b = input()
#c = input()
res = 'Уважаемый {0} {0}!  Поздравляем Вас с {0}-летием!'.format(a)
print(res)

print("\033[3m\033[33m\033[41m{}\033[0m".format("Htua_0111100000"))


class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print("vroom vroom")

my_car = Car("Volkswagen")

# Car.drive(my_car)
# my_car.drive(self)
my_car.drive()


def do_search(bookstore_url, params):
    response = requests.get(
        bookstore_url,
        params,
    )
    print(response.headers)


do_search('http://bookstore.com/search', {'author': 'Austen', 'title': 'Emma'})


import string
    
double_alphabet = dict()
for item in string.ascii_lowercase:      
    double_alphabet[item] = 2*item

print(double_alphabet)