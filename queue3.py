# implementing a priority queue in Python using a min-heap approach and the heapq module.

import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item, priority):
        heapq.heappush(self.heap, (priority, item))


    def remove(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)