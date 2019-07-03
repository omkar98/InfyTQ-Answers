def check_type(type):
    vehicle_type=['Two Wheeler', 'Four Wheeler']
    if type not in vehicle_type:
            return 0
    return 1
class Vehicle:
    def __init__(self):
        pass
    def set_vehicle_id(self,id):
        self.__vehicle_id=id
    def set_vehicle_type(self,type):
        if check_type(type):
            self.__vehicle_type=type
        else:
            return "invalid Vehicle DETAILS"
    def set_vehicle_cost(self,cost):
        self.__vehicle_cost=cost
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
        
    id = property(get_vehicle_id, set_vehicle_id)
    type = property(get_vehicle_type, set_vehicle_type)
    cost = property(get_vehicle_cost, set_vehicle_cost)
        
v1 = Vehicle()
v1.id=10
print(v1.id)
    
