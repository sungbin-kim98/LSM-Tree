from src.lsm_tree import LSMTree

def main():
    db = LSMTree()
    while True:
        print('\nEnter a command below.')
        args = input("$ ").lower().split(' ')
        if args[0] == 'db_set':
            db.db_set(args[1], args[2])
        elif args[0] == 'db_get':
            print(db.db_get(args[1]))
        elif args[0] == 'settings':
            db = LSMTree(int(args[1]), int(args[2]))
        elif args[0] == "compaction":
            db.compaction()

if __name__ == '__main__': 
    main()