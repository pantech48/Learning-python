"""
Форматы данных
"""

data = {
    'users': [
        {
            'id':1,
            'name': 'Linux Torvalds',
            'skills': ('C++', 'Linux'),
            'is developer': True,
        },
        {
            'id':2,
            'name': 'Richard Stallman',
            'skills': ('C', 'GNU'),
            'is developer': True,
        },
    
    ]

}

# todo: pickle

import pickle

with open('users.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('users.pickle', 'rb') as f:
    loaded_data = pickle.load(f)
    print(f'Данные, прочитанные из PICKLE файла:\n{loaded_data}')  

# todo: JSON (JavaScript Object Notation) - автор Дуглас Крокверк

import json

with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('users.json') as f:
    loaded_data = json.load(f)
    print(f'Данные, прочитанные из JSON файла:\n{loaded_data}')  

"""
todo: CSV

id;name;skills;is_developer
1;Linus Torvalds;C++,Linux;1
2;RIchard Stallman;C,GNU;1
"""

import csv

with open('users.csv', 'w') as f:
    users = data.get('users', [])
    if users:
        fieldnames = users[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

with open('users.csv') as f:
    reader = csv.DictReader(f)
    users = list(reader)
    print(f'Данныйб прочитанные из CSV файла:\n{users}')

"""
todo: XMl (lxml)

<users>
    <user>
        <id1>1</id>
    </user>
</users>
"""

# todo: Yaml (PyYAML)

# todo: INI - Конфигурация



