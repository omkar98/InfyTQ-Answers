#DSA-Exer-23

def arrange_tickets(tickets_list):
    new_list=[]
    for i in range(1,21):
        if "T"+str(i) in tickets_list:
            new_list.append("T"+str(i))
        else:
            if i<=10:
                new_list.append('V')
    print(new_list)
    counter=10
    for index,ticket in enumerate(new_list):
        if ticket=='V' and index<=10:
            new_list[index]=new_list[counter]
            counter+=1
    return new_list[:10]

tickets_list = ['T5', 'T17', 'T10', 'T2', 'T9', 'T15', 'T17', 'T19', 'T16', 'T1', 'T12', 'T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
