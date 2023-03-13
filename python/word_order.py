num_of_inputs = int(input())

inputs = []
counts = {}

for i in range(num_of_inputs):
    word = input()
    
    try:
        counts[word]
    except KeyError:
        counts[word] = 0
        inputs.append(word)
        
    counts[word] += 1
    
print(len(inputs))
    
unique_count_string = ''

for word in inputs:
    unique_count_string += str(counts[word])
    unique_count_string += ' '
    
print(unique_count_string.strip())
