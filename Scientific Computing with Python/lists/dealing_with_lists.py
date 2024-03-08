import string
import random

alphabet = string.ascii_lowercase

def creating_full_name():
    name_size = random.randint(3, 10)
    name = ''.join([random.choice(alphabet) for letter in range(name_size)])

    surname_size = random.randint(3, 10)
    surname = ''.join([random.choice(alphabet) for letter in range(surname_size)])
    full_name = name + ' ' + surname
    return full_name

def creating_data(number_itens):
    items_list = []
    for item in range(number_itens):
        item = {}
        item['name'] = creating_full_name()
        item['age'] = random.randint(15, 70)

        items_list.append(item)
    print('#Items: ', items_list)
    return items_list


def order_by_name(items):
    order_names = lambda item: item['name']
    sorted_by_names = sorted(items, key=order_names)

    print(sorted_by_names)

def order_by_age(items):
    order_ages = lambda item: item['age']
    sorted_by_age = sorted(items, key=order_ages)

    print(sorted_by_age)

def order_by_surname(items):
    order_by_surname = lambda item: item['name'].split(' ')[1]
    sorted_by_surname = sorted(items, key=order_by_surname)

    print(sorted_by_surname)

items = creating_data(10)
order_by_name(items)
order_by_age(items)
order_by_surname(items)