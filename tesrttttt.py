def update_dict_keys_values(d, transform_func):
    updated_dict = {}
    for key, value in d.items():

        new_key = transform_func(key) if isinstance(key, str) else key

        if isinstance(value, dict):
            updated_dict[new_key] = update_dict_keys_values(value, transform_func)

        elif isinstance(value, str):
            updated_dict[new_key] = transform_func(value)

        elif isinstance(value, list):
            updated_dict[new_key] = [transform_func(item) if isinstance(item, str) else item for item in value]
        else:
            updated_dict[new_key] = value  
    return updated_dict

def my_transform_func(s):
    return s.upper() 

my_dict = {
    'a': 'hello',
    'b': {
        'c': 'world',
        'd': 'python'
    },
    'e': ['one', 'two', 'three'],
    'f': 123
}

new_dict = update_dict_keys_values(my_dict, my_transform_func)
print(new_dict)
