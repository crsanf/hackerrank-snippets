import re
# Enter your code here. Read input from STDIN. Print output to STDOUT

def test_regex_pattern(pattern):
    try:
        m = re.search(pattern,pattern)
        print("True")
    except re.error:
        print("False")
        
T = int(input().strip())

for _ in range(T):
    pattern = input().strip()
    test_regex_pattern(pattern)
