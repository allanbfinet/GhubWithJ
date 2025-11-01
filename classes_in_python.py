# CLASSES IN PYTHON 
# -> also object-oriented programming 

# -> class is a blueprint/template of an object 
# Person 

#   -> person1(Allan)
#   -> person2(Joshua)

class Person:
    species = "human" # class variable

    def __init__(self, name, country, hobby):  # initialize our attributes/x-tics
        self.name = name                  # instance variables
        self.country = country
        self.hobby = hobby

    def working(self, profession):  # method/action 
        print(f"{self.name} is working as {profession}")

        # method -> check health status 
    def health(self, status):
        print(f"{self.name} is feeling {status}")

    # [TASK: create another method and access the method in the for loop for 
    #         each of the objects created ]

    def introduce(self):
        print(f"Hi, I'm {self.name} from {self.country}, and I love {self.hobby}.")

    # create objects
person1 = Person("Allan", "US", "reading")
person2 = Person("Joshua", "Uganda", "football")

# person1.working('DE')

# loop through them and call methods
for person in (person1, person2):
    person.introduce()
    person.working("Software Developer")
    person.health("great")

# initialize an object off of the class 
person1 = Person('Allan', 'US', 'Basketball')

# access the attributes  -> using . (dot) syntax
print(f"my name is: {person1.name}")
print(f"my country is: {person1.country}")
print(f"my hobby is: {person1.hobby}")
print(f"my species is: {person1.species}")


# accessing the methods (. (dot) syntax)
person1.working('Data Engineer')
person1.health('sick')




person2 = Person('Joshua', 'Kenya', 'football')

# access attributes for person2 
print(f"my name is: {person2.name}")
print(f"my country is: {person2.country}")
print(f"my hobby is: {person2.hobby}")
print(f"my species is: {person2.species}")


# accessing methods (. (dot) synthax)
person2.working('Instructor')
person2.health('cold')


# loop through several objects  
person3 = Person("Gardy", "Nigeria", "table tennis")
person4 = Person("peter", "Ghana", "golf")
person5 = Person("fritz", "Canada", "hockey") 
# person5.name 

# initialize an empty list  
people = []
people.append(person1)
people.append(person2)
people.append(person3)
people.append(person4)
people.append(person5)

print()
# print("our people list: ", people)
profession = ["DE", "Instr.", "Lawyer", "Foreman", "Architect"]
      # list1  list2
# zip(object, profession)

for person, prof in zip(people, profession):
    print(f"name: {person.name}, country: {person.country}, hobby: {person.hobby}, species: {person.species}")

    # method  
    # print(f"profession: {person.working(prof)}")
    person.working(prof)
    print()

# working()
print()



# Inheritance and Subclass  

# profession 
# goes to school 

# name, country, hobby
                        #  -> Person - parent/super class 
# class Student(Person):   # -> Student - subclass 
#     def __init__(self, name, country, hobby, school_name):
#         super().__init__(name, country, hobby)
#         self.school_name = school_name
#          #self.year = year

#     # [TASK 2: create a method for the Student subclass]

#     def study(self, subject):
#        print(f"{self.name} is studying {subject} at { self.school_name}.")

    




# # # # initialize an object off of the Student subclass  
# stud1 = Student("john", "UK", "soccer", "highcrest")


# print(f"my name is: {stud1.name}")
# print(f"my country is: {stud1.country}")
# print(f"my hobby is: {stud1.hobby}")
# print(f"my school is: {stud1.school_name}")


# # # [TASK 3: Try access the health() method from the parent class 
# # #         what do you notice?]
# #                 #  -> here: access methods off of the parent class 
                

# # # accessing the parent class method
# stud1.health("happy")

# call the method before the overriding  
# stud1.working("student")
# print(")


# METHOD OVERRIDING  
            # -> allows subclass to provide a different implementation of a method that's already 
                # present in the parent class 

class Student(Person):   # -> Student - subclass 
    def working(self, year):  # working() method was previously in parent class
        print(f"{self.name} is a student in year {year}")

        #  [TASK 4]: Override the 'introduce()'method to introduce the student with specific course in mind 


  
# create an object off of the Student subclass & invoke the working() method 
stud1 = Student("John", "UK", "Soccer")
  


# call/invoke the attributes using the . (dot) syntax
print(f"my name is: {stud1.name}")
print(f"my country is: {stud1.country}")
print(f"my hobby is: {stud1.hobby}")
# print(f"my school is: {stud1.school_name}")


# invoking the method using the . (dot) syntax
stud1.working(1995)
print()


                        # ENCAPSULATION
                        # -> restrict direct access to some parts of the object 

class Computer: 
    def __init__(self, type, price):  # initializing our attributes using __init__()
        self.type = type
        self.__price = price

    def get_price(self): 
        return self.__price

    def set_price(self, new_price): 
        self.__price = new_price

    # method
    def age(self, condition):
        print(f"{self.type} is in a {condition} condition.") 


# create an object off of the Computer class
desktop1 = Computer('Macbook pro', "$5000")

# call/invoke the attributes
# desktop1.__price
print(f"my type is: {desktop1.type}")
print(f"my price is: {desktop1.get_price()}")


desktop1.set_price = 6000
print(f"new price for {desktop1.type} is {desktop1.set_price}")
print('\n \n')



                        #  PROPERTY DECORATORS 
                        # -> helps call a method just like an attribute 
class Computer: 
    def __init__(self, type, price):  # initializing our attributes using __init__()
        self.type = type
        self.__price = price

    @property  # property decorator
    def max_price(self): 
        return self.__price

    @max_price.setter
    def set_price(self, new_price): 
        self.__price = new_price

    @max_price.deleter
    def del_price(self): 
        print("deleting brand ...")
        del self.__price

    def start(self): 
        return "Starting Computer..."



# create an object off of the Computer class
desktop2 = Computer('Macbook M1', "$4000")

# call/invoke the attributes
# desktop1.__price
print(f"my type is: {desktop2.type}")

print(f"my price is: {desktop2.max_price}")

# set a new price  
desktop2.set_price = 3500
print(f"My new price for  {desktop2.type} is ${desktop2.set_price}")
print('\n \n')




                        #  POLYMORPHISM
                        # -> many forms 
                        # -> use the same method across multiple classes 
# here, create GamingLaptop subclass that should inherit from Computer

class GamingLaptop(Computer):
    def start(self):
        print(f"{self.name} booting Gaming Laptop and activate GPU")

class BusinessLaptop(Computer):
    def start(self):
        return "Booting Business Laptop & connect to company VPN"


                        
                        # ABCs (ABSTRACT BASE CLASSES)
from abc import ABC, abstractmethod 

class AbstractComputer(ABC): 
    @abstractmethod
    def shutdown(self):
        pass 

# create an object off of AbstractComputer()
# ShapedAI = AbstractComputer()

class GamingLaptop(AbstractComputer): 
    def shutdown(self): 
        return "shutting down gaming laptop"

# create an object off of GamingLaptop()
shapeSize = GamingLaptop()

