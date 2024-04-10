from src.lsm_tree import LSMTree

def main():
    db = LSMTree()
    while True:
        print('\nEnter a command below.')
        args = input("$ ").lower().split(' ')
        if args[0] == "db_set":
            db.db_set(args[1], args[2])
        elif args[0] == "db_get":
            print(db.db_get(args[1]))


if __name__ == '__main__': 
    main()