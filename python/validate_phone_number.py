from re import search

regex = r'''^[789]{1}\d{9}$'''

for _ in range(int(input().strip())):
    string = input().strip()
    m = search(regex,string)

    if m is not None:
        print("YES")
    else:
        print("NO")
