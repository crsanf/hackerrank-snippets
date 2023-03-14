#!/bin/python3
import math
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    datetime_t1 = parse_datetime_string(t1)
    datetime_t2 = parse_datetime_string(t2)
    delta = datetime_t1 - datetime_t2
    total_seconds = (delta.days * 24 * 60 * 60) + delta.seconds
    return int(math.fabs(total_seconds))

def parse_datetime_string(datetime_string):
    datetime_split = datetime_string.split(' ')
    recompiled_datetime_string = '-'.join(datetime_split[1:])
    format_pattern = '%d-%b-%Y-%X-%z'
    datetime_tx = datetime.strptime(recompiled_datetime_string,format_pattern)
    return datetime_tx
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
