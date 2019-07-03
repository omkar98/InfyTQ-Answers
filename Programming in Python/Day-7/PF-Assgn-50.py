#PF-Assgn-50
vowels=['a','e','i','o','u']
def sms_encoding(data):
    temp=[]
    l=data.split(" ")
    for word in l:
        temp_word=[]
        for letter in word:
            if letter.lower() not in vowels:
                temp_word.append(letter)
        if len(temp_word)==0:
            temp_word.append(word)
        temp.append("".join(temp_word))
    return " ".join(temp)
        
                
data="GOOD DAYS AND BAD DAYS"
print(sms_encoding(data))
