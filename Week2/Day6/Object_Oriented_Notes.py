# An object is a construct that holds methods (functions) and properties (similarly to attributes)
# Object Oriented Programming
# Objects, Classes, Abstraction, Encapsulation, Inheritance, Polymorphism
# Objects - ways to represent real life, attributes = properties / behaviors = functionality
# Classes - similar to a template
# Abstraction - narrow the focus of what is needed; defining the requirements
# Encapsulation - encapsulate methods and properties (enclosement of data and methods by protecting data)
# Inheritance - 
# Polymorphism - same class to yield varying results

# Class Notes - class is a construct that holds variables (consisting of functions AKA a method)

# class Student:
#     def __init__(self, firstN, lastN):
#         self.firstName = firstN  # By convention, a constructor uses "__". # Self points to the individual object itself
#         self.lastName = lastN
#     def greetStudent(self):
#         print(f'Hello {self.firstName} {self.lastName}') # self.firstName is the variable that we set in our class.
#     def greeting(self, person):
#         print("hello world " + person)
    

# Anuj = Student("Anuj", "Saheba") # Do NOT pass anything to "self"
# Anuj.greetStudent()

# Anuj.firstName = "AJ"
# Anuj.greetStudent()


# Erick = Student("Erick", "Thai") # Do NOT pass anything to "self"
# Erick.greetStudent()

# Anuj = Student.greeting("Erick") #Dot operator allows you to call the method
# Erick = Student.greeting("Anuj") 

class Car:
    greeting = "hello world" # This is a class variable that can be used with any object within the class
    def __init__(self, make, model, color): # This here is our constructor method
        self.make = make # Example of instance variable
        self.model = model # Example of instance variable
        self.color = color # Example of instance variable
    def changeColor(self, toColor): # Method
        print (f"Changing from {self.color} to {toColor}") 
        self.color = toColor
        print (f"New color is {self.color}")
    def openDoor(self):
        print("open door")
    def displayColor(self):
        print (f"The color of he car is {self.color}")
        return self.color
    @classmethod # Look into staticmethod
    def instanceMethod(cls):
        print ("This is an instance")

class electricCar(Car): # Inheritance of "Car" Class
    def __init__(self, make, model, color, range, autopilot):
        super().__init__(make, model, color)
        self.range = range
        self.autopilot = autopilot
    def batteryLife(self, life):
        print (f'Battery life is: {life} ')

class hybrid(Car):
    def __init__(self, make, model, color, batteryLife):
        super().__init__(make,model,color)
        self.batteryLife = batteryLife



# tesla = electricCar("Tesla", "Model S", "red", "3 hours", "yes")
# print (tesla.batteryLife("3 hours"))
# print(tesla.displayColor())
# print(tesla.make)

myHybrid = hybrid ("Toyota", "Prius", "Silver", "2 hours")
myHybrid.changeColor("lime")

# car = Car ("Toyota", "Tundra", "Red")
# car.instanceMethod()
# car.changeColor("Green")
# car2 = Car("Honda", "Civic", "Blue")
# car2.instanceMethod()
