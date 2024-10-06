def update_dict_values(d, new_value):
    for key, value in d.items():
        if isinstance(value, dict): 
            update_dict_values(value, new_value)
        elif isinstance(value, str):
            d[key] = new_value
        elif isinstance(value, list): 
            d[key] = [new_value if isinstance(item, str) else item for item in value]


my_dict = {
    'a': 'hello',
    'b': {
        'c': 'trert',
        'd': 'python'
    },
    'e': ['one', 'two', 'three'],
    'f': '123'
}

update_dict_values(my_dict, 'replaced')
print(my_dict)
