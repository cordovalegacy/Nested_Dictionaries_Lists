x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x[1][0])

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])


z = [
    {
        'x': 10,
        'y': 20
    }
]
z[0]['y'] = 30
print(z)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterate_dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key, value in list[i].items():
            output += f"{key} - {value},"
            print(output)


iterate_dictionary(students)


def iterate_dictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        for key, value in some_list[i].items():
            if key == key_name:
                print(value)


print(iterate_dictionary2('first_name', students))
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(dojo_dict):
    print(dojo_dict)
    for key, value in dojo_dict.items():
        print("    -    ")
        print(f'{len(value)} {key.upper()}')
        for i in range(0, len(value)):
            print(value[i])


print_info(dojo)
