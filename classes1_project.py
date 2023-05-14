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
        else:
            print("I Started teaching few years ago")



Tr_1 = Teacher("HARON MURUMBA", "HOD", "SCIENCES", "BIO AND CHEM", 5, "lab\n")
print(f"My name is {Tr_1.name} and iam {Tr_1.position} {Tr_1.department} at \
Gikuni secondary school teachig {Tr_1.subject} for the last \
{Tr_1.experience} years and my office is in the school {Tr_1.office}")
