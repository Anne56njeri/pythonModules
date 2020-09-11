class Person:
    age = 0 
    # this is  a constructor 
    def  __init__(self,initialAge):
        if initialAge > 0:
            self.age = initialAge
        self.age = 0 
        print("Age is not valid")
            



