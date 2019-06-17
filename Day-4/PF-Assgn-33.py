#PF-Assgn-33

def find_common_characters(msg1,msg2):
    l=[]
    msg11=msg1.replace(" ", "")
    msg22=msg2.replace(" ", "")
    for letter in msg11:
        if letter in msg22:
            l.append(letter)
    if len(l)!=0:
        return "".join(l)
    else:
        return -1
            

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
