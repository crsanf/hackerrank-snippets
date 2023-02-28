# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

if __name__ == '__main__':
    string = str(input())
    
    key_function = lambda x: int(x)
    grouped_tuples = []
    
    for key, group in groupby(string,key_function):
        count = len([x for x in group])
        tup = tuple([count,key])
        grouped_tuples.append(tup)
        
    print(' '.join(str(tup) for tup in grouped_tuples))
