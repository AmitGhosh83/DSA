class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    ## Custom Hash function based on Input Key
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)  
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value]) 
        # list inside a list

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]   
        return None    

    def keys(self):
        all_keylist =[]            
        for i in range (len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keylist.append(self.data_map[i][j][0])
        return all_keylist    
  


my_hashTable = HashTable()
my_hashTable.set_item('bolts', 1400)
my_hashTable.set_item('washers', 50)
my_hashTable.set_item('lumber', 70)    

my_hashTable.get_item('washers')
my_hashTable.get_item('amit')
my_hashTable.keys()