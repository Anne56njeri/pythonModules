class Bucket:
    def __init__(self,bucket,found):
        self.bucket = []
        
    def update(self,key):
        found = False
        for i in range(len(self.bucket)):
            if self.bucket[i] == key:
                self.bucket[i] = key
                found = True 
                break 
        if found == False:
            self.bucket.append(key))
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
        self.hash_table = [Bucket()for i in range(self.keyspace)]

    def add(self,key:int):
        
        

    def remove(self,key:int,values):
        for i in values:
            if i == value:
                del self.value

    def contains(self,key:int):
        for i in values:
            if i == value:
                return True 
        return False        




