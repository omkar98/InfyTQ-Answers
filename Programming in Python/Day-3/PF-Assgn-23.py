#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    for gem in reqd_gems:
        if gem in gems_list:
            i1=gems_list.index(gem)
            i2=reqd_gems.index(gem)
            bill_amount=bill_amount+(price_list[i1]*reqd_quantity[i2])
            if bill_amount>=30000:
                bill_amount = bill_amount*0.95
        else:
                return -1
    return bill_amount
    
reqd_quantity=[2, 1, 3]
reqd_gems=['Amber', 'Opal', 'Topaz']
gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']
price_list=[4392, 1342, 8734, 6421]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
