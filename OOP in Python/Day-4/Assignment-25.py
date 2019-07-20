#OOPR-Assgn-25
class FruitInfo:
    __fruit_name_list=['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    __fruit_price_list=[100, 800, 70, 110, 600]
    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name.title() in FruitInfo.__fruit_name_list:
            return FruitInfo.__fruit_price_list[FruitInfo.__fruit_name_list.index(fruit_name.title())]
        else:
            return -1
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
class Purchase:
    __counter=101
    def __init__(self, customer,fruit_name, quantity):
        self.__purchase_id=None
        self.__customer=customer
        self.__fruit_name=fruit_name.title()
        self.__quantity=quantity
    def get_purchase_id(self):
        return self.__purchase_id
    def get_customer(self):
        return self.__customer
    def get_quantity(self):
        return self.__quantity
    def calculate_price(self):
        each_fruit_price=FruitInfo.get_fruit_price(self.__fruit_name)
        if each_fruit_price>0:
            self.__purchase_id = 'P' + str(Purchase.__counter)
            Purchase.__counter += 1
            price=each_fruit_price*self.__quantity
            if each_fruit_price==max(FruitInfo.get_fruit_price_list()) and self.__quantity>1:
                price*=0.98
            if each_fruit_price==min(FruitInfo.get_fruit_price_list()) and self.__quantity>=5:
                price*=0.95
            #even if you insert 'Wholesale' in customer type, and check here for 'Wholesale'(i.e if Customer.get_cust_type(self.__customer) is 'Wholesale' and you are checking against 'Wholesale'), still the program will not pass all the test cases. It has to be 'wholesale' and not 'Wholesale'. So it is very very important to read the question carefully and only mention those words/letters as instructed in the questoion.
            if Customer.get_cust_type(self.__customer)=='wholesale':
                price*=0.90
            return (price)
        else:
            return -1
                
            
class Customer():
    def __init__(self, customer_name, cust_type):
        self.__customer_name=customer_name.title()
        #self.__cust_type=cust_type.title() will give wrong answer because in the question it is clearly mentioned that if the customer_type is 'wholesale' not 'Wholesale'. Also check at Line 40 
        self.__cust_type=cust_type.lower()
    def get_customer_name(self):
        return self.__customer_name
    def get_cust_type(self):
        return self.__cust_type
        
c=Customer("Tom", "wholesale")
p=Purchase(c,"Orange", 5)
print(p.calculate_price())

