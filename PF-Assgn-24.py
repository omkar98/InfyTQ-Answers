#PF-Assgn-24
def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    l = [num1, num2, num3]
    for n in l:
        if n >= l[(l.index(n)+1)%3]+l[(l.index(n)+2)%3]:
            return failure
    return success

num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)
