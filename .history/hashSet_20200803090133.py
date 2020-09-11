class Bucket:
    def __init__(self,bucket,found):
        self.bucket = []
        
    def update(self,key):
        found = False
        for i in range(self.bucket):
            if i == key:
                self.bucket[i] = key
                self.found = True 
                break 
        if self.found == False:
            self.bucket.insert(len(self.bucket-1,key))
    def get(self,key):
        for k in self.bucket:
            if k == key:
                return True 
        return False    
    def remove(self,key):
        for i in range(len(self.bucket)):
            if self.bucket[i] == key:
                del self.bucket[i]        


class myHashSet:
    def __init__(self):
        self.keyspace = 2096

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




