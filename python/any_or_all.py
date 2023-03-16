#Challenge to complete in 3 lines of code
N = input().strip()
arr = input().strip().split(' ')
print('True') if all(int(x) >= 0 for x in arr) and any(x == ''.join(reversed(x)) for x in arr) else print('False')
