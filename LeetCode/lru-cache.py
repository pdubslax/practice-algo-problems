class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keyToValueMap = {}
        self.keyQueue = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keyToValueMap:
            self.keyQueue.remove(key)
            self.keyQueue.append(key)
            return self.keyToValueMap[key]
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keyQueue:
            self.keyQueue.remove(key)
        elif self.capacity == len(self.keyQueue):
            # evict
            del self.keyToValueMap[self.keyQueue[0]]
            self.keyQueue.pop(0)
    
        self.keyQueue.append(key)
        self.keyToValueMap[key] = value
        return None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)