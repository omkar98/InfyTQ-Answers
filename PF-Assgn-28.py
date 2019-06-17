#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    l = [max_num]
    if num1<num2:
         for num in range(num1,num2+1):
            if len(str(num)) == 2:
                sum = 0
                for digit in str(num):
                    sum = sum + int(digit)
                if sum%3==0:
                    if num%5==0:
                        l.append(num)
    return max(l)

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
