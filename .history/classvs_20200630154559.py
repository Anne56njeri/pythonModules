class Person:
    age = 0 
    # this is  a constructor 
    def  __init__(self,initialAge):
        if initialAge > 0:
            self.age = initialAge
        self.age = 0 
        print("Age is not valid, setting age to 0.. ")

    def yearPasses(self):
        self.age = self.age +1 
        return self.age 
    def amOld(self):
        if self.age < 13:
            print("You are young..")   
        if self.age >= 13 and self.age < 18:
            print("You are a teenager..")
        else:
            print("You are old..")    
# this is an object
person = Person(10)

person.yearPasses()
person


