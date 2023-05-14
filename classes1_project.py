#!/usr/bin/python3

#a code implemented in a class that passe pycodestyle

class Teacher:
    #attribute of the class
    station = 'ACK. GIKUNI SECONDARY SCHOOL'
    
    #Defining dunder method or magic method to initialize a class
    
    def __init__(self, name, position, department, subject, experience, office):
    #attribute of the method initantiated in a class
    
        self.name = name
        self.position = position
        self.department = department
        self.subject = subject
        self.experience = experience
        self.office = office
    
    
    #methods of a class
    def teach(self, experience):
        if experience:
            print("have taught for over 30 year")
        print("Good work Teacher")
    print('\n')


#object1
Tr_1 = Teacher('HARON MURUMBA', 'HOD', 'SCIENCES', 'CHEMISTRY', 5, 'HODs SC Office')
print(f"My name is {Tr_1.name} and iam {Tr_1.position} {Tr_1.department} at \
Gikuni secondary school teachig {Tr_1.subject} for the last \
{Tr_1.experience} years and my office is {Tr_1.office}")
print(Tr_1.station)
print(Tr_1.teach(30))
print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


#object 2
Tr_2 = Teacher('MARYANN K', 'DEPUTY PRINCIPAL', 'COMP SCI', 'MATH', 4, 'DPs Office')  

print(f"Her name is {Tr_2.name} and she is {Tr_2.position} at Gikuni secondary\
 school also teaching {Tr_2.subject} for the last {Tr_2.experience} years")

print(Tr_2.station)
print(Tr_2.teach(20))
