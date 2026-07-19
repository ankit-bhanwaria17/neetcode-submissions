class DLL:
    def __init__(self, key, next, prev):
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.last = None
        self.first = None
        self.hashmap = {} # key -> [value, Node]        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.makeKeyRecentlyUsed(key)
        return self.hashmap[key][0]

    def put(self, key: int, value: int) -> None:
        if len(self.hashmap) == 0:
            node = DLL(key, None, None)
            self.first = self.last = node
            self.hashmap[key] = [value, node]
            return
        if key in self.hashmap:
            self.hashmap[key][0] = value
            self.makeKeyRecentlyUsed(key)
        else:
            node = DLL(key, None, None)
            self.first.next = node
            node.prev = self.first
            self.first = node
            self.hashmap[key] = [value, node]
        if len(self.hashmap) > self.capacity:
            self.hashmap.pop(self.last.key, None)
            secondLast = self.last.next
            self.last.next = None
            secondLast.prev = None
            self.last = secondLast
    
    def makeKeyRecentlyUsed(self, key: int) -> None:
        node = self.hashmap[key][1]
        if node.next is None:
            return
        if node.prev:
            node.prev.next = node.next
        node.next.prev = node.prev
        if node.prev is None:
            self.last = node.next
        node.next = None
        node.prev = self.first
        self.first.next = node
        self.first = node


        
