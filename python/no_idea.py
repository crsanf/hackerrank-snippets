# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    input() #Skip the initial length indicators
    n = list(map(int,input().split(' ')))
    A = set(map(int,input().split(' ')))
    B = set(map(int,input().split(' ')))
    
    happiness = 0
    
    for i in n:
        check = set([i])
        
        if len(check.intersection(A)) > 0:
            happiness += 1
        
        if len(check.intersection(B)) > 0:
            happiness -= 1
            
    print(happiness)