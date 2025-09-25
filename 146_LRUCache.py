# Definition for doubly linked list node
class Node(object):
    def __init__(self, key=0, value=0):
        self.key = key      # Store the key
        self.value = value  # Store the value
        self.prev = None    # Pointer to previous node
        self.next = None    # Pointer to next node

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity  # Maximum cache size
        self.map = {}             # Dictionary: key -> node
        self.head = Node()        # Dummy head node
        self.tail = Node()        # Dummy tail node
        self.head.next = self.tail  # Head points to tail
        self.tail.prev = self.head  # Tail points back to head

    # Remove a node from the linked list
    def _remove(self, node):
        node.prev.next = node.next  # Bypass node from previous
        node.next.prev = node.prev  # Bypass node from next

    # Insert a node right after head (most recently used)
    def _insert(self, node):
        node.next = self.head.next  # Node points to first real node
        node.prev = self.head       # Node points back to head
        self.head.next.prev = node  # First real node points back to node
        self.head.next = node       # Head points to new node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1  # Key not found
        node = self.map[key]        # Get node from map
        self._remove(node)          # Remove from current position
        self._insert(node)          # Move to front (most recent)
        return node.value           # Return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self._remove(self.map[key])  # Remove old node if exists
        node = Node(key, value)           # Create new node
        self._insert(node)                # Insert at front
        self.map[key] = node              # Add to map
        if len(self.map) > self.capacity:
            lru = self.tail.prev          # Least recently used node
            self._remove(lru)             # Remove from linked list
            del self.map[lru.key]         # Remove from map
