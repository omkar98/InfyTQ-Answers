#OOPR-Assgn-10
#Efficient Program by Minal Kaminwar
class CallDetail:
    def __init__(self, phoneno, called_no, duration, call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]
        for each_call in list_of_call_string:
            call_detail_list=each_call.split(",")
            # print(call_detail_list)
            # obj=[]
            # for attribute in call_detail_list:
            #     obj.append(attribute)
            a=CallDetail(call_detail_list[0],call_detail_list[1],call_detail_list[2],call_detail_list[3])
            self.list_of_call_objects.append(a)

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(['9990000001,9330000001,23,STD', '9990000001,9330000002,54,Local', '9990000001,9330000003,6,ISD'])
