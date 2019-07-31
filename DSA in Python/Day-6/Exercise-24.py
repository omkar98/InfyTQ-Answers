#DSA-Exer-24

def make_change(denomination_list, amount):
    '''Remove pass and implement the Greedy approach to make the change for the amount using the currencies in the denomination list.
    The function should return the total number of notes needed to make the change. If change cannot be obtained for the given amount, then return -1. Return 1 if the amount is equal to one of the currencies available in the denomination list.  '''
    denomination_list.sort()
    l=[]
    current_amount=amount
    while(sum(l)!=amount):
        if amount in denomination_list:
            return 1
        else:
            i=len(denomination_list)
            maxi=max(denomination_list[0:i])
            while(maxi>current_amount):
                if i:
                    maxi=max(denomination_list[0:i])
                    i-=1
                else:
                    return -1
            l.append(maxi)
            current_amount-=maxi
    print(l)
    return len(l)
                  
#Pass different values to the function and test your program
amount= 3
denomination_list = [10,20,30]
print(make_change(denomination_list, amount))
