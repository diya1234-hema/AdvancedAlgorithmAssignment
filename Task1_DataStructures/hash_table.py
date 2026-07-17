class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, city_name, population):
        self.table[city_name] = population

    def search(self, city_name):
        return self.table.get(city_name)
hash_table = HashTable()

hash_table.insert("Kathmandu", 1400000)
hash_table.insert("Pokhara", 600000)
hash_table.insert("Butwal", 200000)

print("Population of Pokhara:")
print(hash_table.search("Pokhara"))