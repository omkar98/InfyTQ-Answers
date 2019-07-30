#DSA-Exer-18

def find_next_min(num_list,start_index):
    #Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    #start_index indicates the start index of the sub-list
    small=num_list[start_index]
    for i in range(start_index, len(num_list)):
        if small>num_list[i]:
            small=num_list[i]
    return num_list.index(small)
        

#Pass different values to the function and test your program
num_list=[10,2,100,67]
start_index=1
print("Index of the next minimum element is", find_next_min(num_list,start_index))
