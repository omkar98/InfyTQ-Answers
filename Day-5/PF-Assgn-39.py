#PF-Assgn-39
#This verification is based on string match.     
#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]

def place_order(*item_tuple):
    customer_items=[]
    customer_quantity=[]
    for i in range(len(item_tuple)):
        if i%2==0:
            customer_items.append(item_tuple[i])
        else:
            customer_quantity.append(item_tuple[i])
    for index,item in enumerate(customer_items):
        if item not in menu:
            print (item + " is not available")
            continue
        else:
            i=menu.index(item)
            if check_quantity_available(i,customer_quantity[index]):
                print (item + " is available")
            else:
                print(item +" stock is over")
    
'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if quantity_available[index]<=quantity_requested:
        return 1
    else:
        return 0

#Provide different values for items ordered and test your program
#place_order("Veg Roll",2,"Noodles",2)
place_order("Fried Rice",2,"Soup",1)

