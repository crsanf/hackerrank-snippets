# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt,asin,degrees

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    ac = sqrt((ab ** 2) + (bc ** 2))
    m = ac / 2
    
    opp_hyp = ab / ac
    sin_radians = asin(opp_hyp)
    sin_degrees = degrees(sin_radians)
    
    degrees_rounded = int(round(sin_degrees,0))

    print(f"{degrees_rounded}\N{DEGREE SIGN}")
    
    
