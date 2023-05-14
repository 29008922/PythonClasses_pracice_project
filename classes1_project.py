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



Tr_1 = Teacher("HARON MURUMBA", "HOD", "SCIENCES", "BIO AND CHEM", "5", "lab")

print(f"Mr {self.name} is {self.position} {self.department}teaching {self.subject},
		with an experience of {self.experience}
		 and mostly you will find the {self.office}\n")
print(Tr_1.station)
print(Tr_1.teach(5))

