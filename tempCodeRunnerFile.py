a_dictionary = {'a': 1, 'b':2, 'c':3}
b_dictionary = {value: key for key, value in a_dictionary.items()}
print(b_dictionary)