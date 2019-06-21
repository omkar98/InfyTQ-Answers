#PF-Tryout
import random

def biased_flip(prob_true):
        return random.random()<prob_true
        

head,tail=0,0
for i in  range(1000):
    value=biased_flip(0.7)
    if value:
        head=head+1
    else:
        tail=tail+1
print("Heads: "+str(head))
print("Tails: "+str(tail))
