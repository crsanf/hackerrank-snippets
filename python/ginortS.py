S = input().strip()

keys = [
    'lower',
    'upper',
    'odd_digit',
    'even_digit',
]

characters = {key: [] for key in keys}

for char in S:
    if char.isupper():
        characters['upper'].append(char)
    elif char.islower():
        characters['lower'].append(char)
    else:
        if int(char) % 2 == 0:
            characters['even_digit'].append(char)
        else:
            characters['odd_digit'].append(char)

sorted_string = ''
            
for key in keys:
    characters[key].sort()
    sorted_string += ''.join(characters[key])

print(sorted_string)
