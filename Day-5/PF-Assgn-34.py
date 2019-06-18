#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    count=0
    for index,num in enumerate(num_list):
        for i in range(index+1,len(num_list)):
            if num+num_list[i]==n:
                count=count+1
    return count
                 

num_list=[1, 2, 4, 5, 6]
n=7
print(find_pairs_of_numbers(num_list,n))
