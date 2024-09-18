from typing import Union

class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [[] for _ in range(self.size)]
        self.len = 0
    
    def length(self) -> int:
        return self.len

    def get_hash(self, key: str) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size
    
    def __getitem__(self, key: str) -> str:
        h = self.get_hash(key)

        for e in self.table[h]:
            if e[0] == key:
                return e[1]
        raise KeyError(f'key: {key} not found')

    def __setitem__(self, key: str, val: str) -> None:
        h = self.get_hash(key)
        for idx, e in enumerate(self.table[h]):
            if e[0] == key:
                self.table[h][idx] = key, val
                return
        self.table[h].append((key,val))
        self.len += 1
    
    def __delitem__(self, key) -> None:
        h = self.get_hash(key)
        for idx, e in enumerate(self.table[h]):
            if e[0] == key:
                del self.table[h][idx]
                self.len -= 1
                return
        raise KeyError(f'key: {key} not found')
        
table = HashTable()

table["august 15"] = "walid"
table["october 10"] = "zakaria"
table["junuary 14"] = "zakia"
table["december 11"] = "ismail"

print(table.length())
print(table["august 15"])
