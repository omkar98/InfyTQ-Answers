#PF-Assgn-15
def find_product(num1,num2,num3):
    args=[]
    args.extend([num1,num2,num3])
    product=1
    if 7 in args:
        i = args.index(7)
        if i is (len(args)-1):
            return -1
    else:
        i = -1
    for index in range(i+1,len(args)):
        product = product * args[index]
        
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,6,2)
print(product)
