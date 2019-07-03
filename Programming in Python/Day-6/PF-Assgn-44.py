#PF-Assgn-44

def find_duplicates(list_of_numbers):
    dup=[]
    for num in list_of_numbers:
        if (list_of_numbers.count(num)>1) and (num not in dup):
            dup.append(num)
    return  dup

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
