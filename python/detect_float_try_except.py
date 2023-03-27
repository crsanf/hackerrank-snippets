N = int(input().strip())

for i in range(N):
    s = input().strip()
    try:
        float(s)
        if s.index('.') != len(s) - 1:
            print("True")
        else:
            print("False")
    except ValueError:
        print("False")
