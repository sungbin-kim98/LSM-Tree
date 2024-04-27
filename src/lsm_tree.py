class LSMTree():
    def db_get(self, key):
        with open('disk.txt', 'r') as file:
            for line in file:
                if key in line:
                    print(line.rstrip())

    def db_set(self, key, value):
        file = open('disk.txt', 'a')
        file.write(key + "," + value + "\n")
        file.close()
         