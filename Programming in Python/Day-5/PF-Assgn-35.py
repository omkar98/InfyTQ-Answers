#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    avg = sum(list_of_marks)/len(list_of_marks)
    count = 0
    for marks in list_of_marks:
        if marks>avg:
            count=count+1
    return (count*10)
        
    
def sort_marks():
    return sorted(list(list_of_marks))

def generate_frequency():
    l=[]
    for value in range(0,26):
        l.append(list_of_marks.count(value))
    return l

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
