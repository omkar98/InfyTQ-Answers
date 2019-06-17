#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    l=[]
    for key,value in medical_speciality.items():
            l.append(patient_medical_speciality_list.count(key))
    speciality=tuple(medical_speciality.values())[l.index(max(l))]
    return speciality
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
