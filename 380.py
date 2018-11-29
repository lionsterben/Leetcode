class RandomizedSet:
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = []
        self.pos = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.num.append(val)
            self.pos[val] = len(self.num)-1
            return True
        return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx, last = self.pos[val], self.num[-1]
            self.num[idx] = last
            self.pos[last] = idx
            self.num.pop()
            del self.pos[val]
            return True
        return False
        

        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, len(self.num)-1)
        return self.num[idx]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

## point 交换num最后一个和要删去的值，同时改变pos的对应index