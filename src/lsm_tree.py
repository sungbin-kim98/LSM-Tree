class LSMTree():
    def __init__(self):
        self.cache = {}

    def db_get(self, key: str) -> None:
        if key in self.cache:
            print(f'{key},{self.cache[key]}')
            return 
        
        with open('disk.txt', 'r') as file:
            for line in file:
                if key in line:
                    print(line.rstrip())

    def db_set(self, key: str, value: str) -> None:
        file = open('disk.txt', 'a')
        file.write(key + "," + value + "\n")
        self.cache[key] = value
        file.close()
         