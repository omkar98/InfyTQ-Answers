#PF-Assgn-38

def check_double(number):
    double = number * 2
    number1 = str(number)
    double1 = str(double)
    if len(number1) == len(double1):
        for index, digit in enumerate(list(double1)):
            if (digit in number1) and (digit != number1[index]):
                status = True
            else:
                status = False
    else:
        status=False
    return status

#Provide different values for number and test your program
print(check_double(125874))
