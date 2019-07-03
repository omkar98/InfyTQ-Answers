#PF-Assgn-47
vowels=['a','e','i','o','u']

def encrypt_sentence(sentence):
    final=[]
    list_sentence = sentence.split(" ")
    for index,word in enumerate(list_sentence):
        if (index+1)%2!=0:
            final.append(word[::-1])
        else:
            v=[]#to store all vowels
            t=[]#to store the letters temporily
            for letter in word:
                if letter not in vowels:
                    t.append(letter)
                else:
                    v.append(letter)
            t.extend(v)
            final.append("".join(t))
    #if len(final)>1:
    return " ".join(final)
                    
sentence="the"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
sentence="hello i am omkar"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
