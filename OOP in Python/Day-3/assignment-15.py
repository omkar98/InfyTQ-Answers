#OOPR-Assgn-15

class Parrot:
    __counter=7000
    def __init__(self, name, color):
        self.__unique_number=Parrot.__counter+1
        self.__color=color
        self.__name=name
        Parrot.__counter+=1
    def get_unique_number(self):
        return self.__unique_number
    def get_color(self):
        return self.__color
    def get_name(self):
        return self.__name

p1=Parrot("blue", "Sam")
p2=Parrot("blue", "Sm")
p3=Parrot("blue", "Sm")
p4=Parrot("blue", "Sm")
p5=Parrot("blue", "Sm")
p6=Parrot("blue", "Sm")
print(Parrot._Parrot__counter)
