#DSA-Exer-22

def order_heights(student_list,height_list):
    new_list=height_list.copy()
    students=[]
    new_list.sort()
    for height in new_list:
        students.append(student_list[height_list.index(height)])
    return[students,new_list]

#Pass different values to the function and test your program
student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
print("Initial student details :")
print("The students:",student_list)
print("Their heights:",height_list)
print()
result=order_heights(student_list,height_list)
print("After arranging the students in the order of their height:")
print("The students :",result[0])
print("Their heights:",result[1])
