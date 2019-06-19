#PF-Assgn-41
def find_ten_substring(num_str):
    final=[]
    temp=[]
    for index,value in enumerate(list(num_str)):
        l=[]
        temp=[]
        for i in range(index,len(num_str)):
            l.append(int(num_str[i]))
            s=sum(l)
            if s < 10:
                continue
            elif s==10:
                for value in l:
                    temp.append(str(value))
                sum_string = "".join(temp)
                final.append(sum_string)
                if i!=(len(num_str)-1):
                    if num_str[i+1]=='0':
                        temp=[]
                        continue
                break
            elif s>10:
                break
    return final
                    

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
