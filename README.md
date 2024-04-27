# LSM-Tree
## 156-160 Implement a key-value store

* Write O(1)
    * Append-only 
    * Single disk
* Read O(n)

`db_set` performance: 0.0002760887145996094

`db_get` performance: 0.0016160011291503906

## 160-162 Implement hash indices

* Write O(1)
* Read
    * Best case: O(1)
    * Worst case: O(n)

`db_set` performance: 0.00031685829162597656

`db_get` performance: 0.00000905990600585938
