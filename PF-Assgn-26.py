#PF-Assgn-26
"""
x = no. of chickens
y = no. of rabbits
x+y = no. of heads  ---- (1)
    2x + 4y = no. of legs
or  x+2y = (legs/2) ----- (2)
heads - y + 2y = (legs/2) ,i.e substitute (1) in (2)
hence, y = (legs/2) - heads
       x = heads - y
"""


def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if legs%2==0:#legs must be even multiples
        rabbit_count = (legs//2) - heads
        chicken_count = heads - rabbit_count
    
        if rabbit_count<0 or chicken_count<0:
            print(error_msg)
        else:
            print(chicken_count,rabbit_count)
    else:
        print(error_msg)
    

#Provide different values for heads and legs and test your program
solve(38,131)
