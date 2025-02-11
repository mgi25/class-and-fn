# 1. write a python program that has a class to store details of a student with the following specification.
# 2. Data Members: name, dob, addfress., phone,email
# 3. member Function: __init__() to init values 
# print() -> prints the values
# Create an object for alen and danish and print their details 


#update the program

# a dictnoray to store subjects, total marks, and obtained marks
# create a function to store the marks for alen/ danish
# print th ecomplete details of danish/ alen

class student:
    def __init__(self,name,dob,address,phone,email):
        self.name = name
        self.dob = dob
        self.address = address
        self.phone = phone
        self.email = email
        self.subjects = []
    
    
    def marks(self,subject,total_mark,obtained_mark):
        self.subjects.append({"subject":subject,"total_mark":total_mark,"obtained mark":obtained_mark})
    
    def details(self):
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"address: {self.address}")
        print(f"Phone: {self.phone}")
        print(f"email: {self.email}")
        print("Marks:",str(self.subjects))
        
        print("----------------------")
        
alen = student("Alen","25/10/2005","HVS 168","9393939393","alenjinmgi@gmail.com") 
danish = student("danish","10/01/2005","G block","444444444","danish@gmail.com")

alen.details()
danish.details()

alen.marks("Maths",100,90)
alen.marks("Science",100,95)
alen.marks("English",100,80)

alen.details()
