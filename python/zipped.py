from math import fsum
#Get all input data
N,X = map(int,input().strip().split(' '))
scores = []

for _ in range(X):
    scores.append(list(map(float,input().strip().split(' '))))
    
#Calculate Averages
zipped_scores = zip(*scores)
for student in zipped_scores:
    sum = fsum(student)
    average = round(sum / X,1)
    print(average)
