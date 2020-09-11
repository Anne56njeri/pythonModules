class Bucket:
    def __init__(self,bucket,found):
        self.bucket = []
        self.found = False
    def update(self,key):
        for i in self.bucket:
            if i == key:
                self.bucket[i] = key
                found = True 
                break 
            

class myHashSet:
    def __init__(self,value):
        self.value = value
        self.values = []

    def add(self,key:int,values):
        values.push(value)
        

    def remove(self,key:int,values):
        for i in values:
            if i == value:
                del self.value

    def contains(self,key:int):
        for i in values:
            if i == value:
                return True 
        return False        




