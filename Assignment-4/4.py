#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # write your logic here

    P, O, E = 0, 0, 0
    for index in range(len(patient_medical_speciality_list)):
        if patient_medical_speciality_list[index] == 'P': P = P + 1
        elif patient_medical_speciality_list[index] == 'O': O = O + 1
        elif patient_medical_speciality_list[index] == 'E': E = E + 1
        else: continue

    if P > O and P > E: return "Pediatrics"
    elif O > P and O > E: return "Orthopedics"
    else: return "ENT"

#provide different values in the list and test your program
patient_medical_speciality_list = [301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P":"Pediatrics", "O":"Orthopedics", "E":"ENT"}
speciality = max_visited_speciality(patient_medical_speciality_list, medical_speciality)
print(speciality)