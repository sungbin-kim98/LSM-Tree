import os

class LSMTree():
    def __init__(self, segment = 0, segment_capacity = 10):
        self.cache = [{}]
        self.segment = 0
        self.segment_capacity = segment_capacity

    def compaction(self) -> None:
        merged_cache = {}
        for i in range(self.segment + 1):
            with open(f'disk{i}.txt', 'r') as file:
                for line in file:
                    if len(line.split(",", 1)) == 2:
                        key, value = line.split(",", 1)
                        merged_cache[key] = value.strip()

        new_segment = 0
        new_cache = [{}] 
        current_capacity = 0
        for key in merged_cache:
            if current_capacity == 0:
                os.remove(f'disk{new_segment}.txt')
            with open(f'disk{new_segment}.txt', 'a+') as file:
                file.write(key + ',' + merged_cache[key] + '\n')
            new_cache[new_segment][key] = merged_cache[key]
            current_capacity += 1
            if current_capacity >= self.segment_capacity:
                current_capacity = 0
                new_cache.append({})
                new_segment += 1

        if new_segment < self.segment:
            for i in range(new_segment + 1, self.segment + 1):
                os.remove(f'disk{i}.txt')
        
        self.segment = new_segment
        self.cache = new_cache

    def db_get(self, key: str) -> None:
        if key in self.cache[self.segment]:
            print(f'{key},{self.cache[self.segment][key]}')
            return 
        
        with open(f'disk{self.segment}.txt', 'r') as file:
            for line in file:
                if key in line:
                    print(line.strip())

    def db_set(self, key: str, value: str) -> None:
        try:
            with open(f'disk{self.segment}.txt', 'rb') as file:
                num_lines = sum(1 for _ in file)
                if (num_lines >= self.segment_capacity):
                    self.cache.append({})
                    self.segment += 1
                    print(f'Writing to new segment {self.segment}')
        except FileNotFoundError:
            pass

        with open(f'disk{self.segment}.txt', 'a+') as file:
                file.write(key + ',' + value + '\n')

        self.cache[self.segment][key] = value
         