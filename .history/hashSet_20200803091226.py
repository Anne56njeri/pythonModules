class Bucket:
    def __init__(self):
        self.bucket = []
        
    def update(self,key):
        found = False
        for i in range(len(self.bucket)):
            if self.bucket[i] == key:
                self.bucket[i] = key
                found = True 
                break 
        if found == False:
            self.bucket.append(key)
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
        self.hash_table = [Bucket() for i in range(self.keyspace)]

    def add(self,key:int):
        dict_key = key %self.keyspace 
        self.hash_table[dict_key].update(key)
        
        

    def remove(self,key:int):
        dict_key = key % self.keyspace 
        print("here",k)
        self.hash_table[dict_key].remove(key)

    def contains(self,key:int):
        dict_key = key % self.keyspace
        return self.hash_table[dict_key].get(key)        

number = myHashSet()
number.add(1)
number.add(2)
number.add(3)
print(number.contains(4))
number.remove(5)


