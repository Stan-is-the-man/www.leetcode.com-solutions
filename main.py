def letter_combinations(digits: str):
    my_dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    my_list = []
    final_list = []
    for x in digits:
        my_list.append(my_dict[x])

    for element in my_list:
        for letter in element:





a = "23"
b = letter_combinations(a)
print(a)
