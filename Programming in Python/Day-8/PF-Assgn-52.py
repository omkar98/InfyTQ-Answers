#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func==None:
        return sum(list_of_num)
    else:
        return sum(filter_func)
        
    
def even(data):
    e=[]
    for num in data:
        if num%2!=0:
            e.append(num)
    return e

def odd(data):
    o=[]
    for num in data:
        if num%2!=0:
            o.append(num)
    return o
sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))
