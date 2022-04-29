import logging


def mnozenie(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        return "Złe dane!"


#
# print(mnozenie("4", "t"))
# print(mnozenie("4", "5")) # OK
# print(mnozenie(None, 1))

def _check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        if int(user['age']) < age:
            count += 1
        return count


def check_age(users, age):

    try:
        return _check_age(users, age)
    except KeyError:
        print(f'Niepoprawne dane')
    except ValueError:
        print(f'Niepoprawny wiek')



valid_data = [{'name': 'Jan', 'age': 'age'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
print(check_age(valid_data, 18))
