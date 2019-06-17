#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    if quantity_ordered>=1 and distance_in_kms>0:
        deli_cost = 0
        bill_amount=0
        dist = [(3,0),(6,3),(7,6)]
        if food_type == 'V':
            food_cost = quantity_ordered * 120
        elif food_type == 'N':
            food_cost = quantity_ordered * 150
        else:
            return -1
        dist_covered = 0
        while dist_covered <= distance_in_kms:
            for distance in dist:
                if dist_covered <= distance[0]:
                    value = distance[1]
                    break
            deli_cost = deli_cost + value
            dist_covered=dist_covered+1
            
        bill_amount = food_cost + deli_cost
        return bill_amount
    else:
        return -1
    

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
