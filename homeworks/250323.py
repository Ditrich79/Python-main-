import json
from random import choice


def get_person():
    name = ''
    tel = ''
    tel2 = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    while len(tel2) != 10:
        tel2 += choice(nums)

    person = {
        tel2:
        {
            'name': name,
            'tel': tel
        }
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('person2.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open('person2.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(get_person())
