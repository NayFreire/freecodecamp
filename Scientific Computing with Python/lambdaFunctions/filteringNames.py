people = [
    {
        'name': 'Maria',
        'surname': 'Smith',
        'age': 43
    },
    {
        'name': 'Rose',
        'surname': 'Former',
        'age': 32
    },
    {
        'name': 'Carl',
        'surname': 'Pierce',
        'age': 38
    },
    {
        'name': 'Gabriel',
        'surname': 'Johnson',
        'age': 25
    }
]

sorted_people_surname = lambda person: person['surname']
sorted_people_name = lambda person: person['name']
sorted_people_age = lambda person: person['age']

sorted_by_surnames = sorted(people, key=sorted_people_surname)
sorted_by_name = sorted(people, key=sorted_people_name)
sorted_by_age = sorted(people, key=sorted_people_age)

print(sorted_by_surnames)
print(sorted_by_name)
print(sorted_by_age)