import re

#Get Input
s = input().strip()
k = input().strip()

index = 0

while index < len(s):
    m = re.search(k,s[index:])

    if m == None:
        if index == 0:
            print(tuple([-1,-1]))
            break
        else:
            break
    
    start = m.start() + index
    end = m.end() + index - 1
    print(tuple([start,end]))

    if len(k) > 1:
        index = end
    else:
        index = end + 1
