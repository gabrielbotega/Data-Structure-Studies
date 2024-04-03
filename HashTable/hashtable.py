class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        myHash = 0
        for letter in key:
            # ord() returns the unicode point of a character
            # this operation will always return a number between 0 and 6 (inclusive)
            myHash = (myHash + ord(letter) * 23) % len(self.data_map)
        return myHash
    
    def print_table(self):
        for i, lst in enumerate(self.data_map):
            print(i, ": ", lst)

    def set_pair(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        listOfInterest = self.data_map[index]
        if listOfInterest is not None:
            for i in range(len(listOfInterest)):
                if listOfInterest[i][0] == key:
                    return listOfInterest[i][1]
        return None
    
    def keys(self):
        allKeys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    allKeys.append(self.data_map[i][j][0])
        return allKeys



myHashTable = HashTable()
myHashTable.set_pair('nails', 1000)
myHashTable.set_pair('nuts', 1200)
myHashTable.set_pair('bolts', 500)
myHashTable.set_pair('camelo', 2)

myHashTable.print_table()

print("======= My Hash Table Data Map =======")
print (myHashTable.data_map)

print("======= Get =======")
print (myHashTable.get_item('nuts'))

print("======= Keys =======")
print (myHashTable.keys())