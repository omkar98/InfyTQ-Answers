#PF-Tryout
#Assignment 18: Mandatory - Level 2

def convert_currency(amount_needed_inr,current_currency_name):
    converter = {
        'Euro': 0.01417,
        'British Pound': 0.0100,
        'Australian Dollar': 0.02140,
        'Canadian Dollar':0.02027
    }
    for Currency,Equivalent in converter.items():
        if Currency == current_currency_name:
            current_currency_amount = amount_needed_inr * Equivalent
            return current_currency_amount
    #write your logic here
    return -1

#currency_needed=convert_currency(2000,"Euro")
currency_needed=convert_currency(3500,"British Pound")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
