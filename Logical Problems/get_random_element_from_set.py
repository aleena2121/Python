import random
class RandomizedSet:

    def __init__(self):
        self.arr = []

    def insert(self, val: int) -> bool:
        if len(self.arr) == 0 or val not in self.arr:
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_1 = obj.insert(3)
param_1 = obj.insert(4)
param_1 = obj.insert(4)
param_2 = obj.remove(4)
param_3 = obj.getRandom()