from src.lsm_tree import LSMTree
import random
import string
import time 
import unittest

# https://www.geeksforgeeks.org/python-generate-random-string-of-given-length
def generate_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters, k=length))

class LSMTreeTests(unittest.TestCase):
    def test_db_set_and_db_get(self):
        key, value = generate_random_string(3), generate_random_string(100)
        db = LSMTree()
        setStartTime = time.time()
        db.db_set(key, value)
        setEndTime = time.time()
        print("db_set performance: ", setEndTime - setStartTime)
        getStartTime = time.time()
        db.db_get(key)
        getEndTime = time.time()
        print("db_get performance: ", getEndTime - getStartTime)

if __name__ == '__main__':
    unittest.main()