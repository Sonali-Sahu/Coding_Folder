class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def isEmpty(self):
        return len(self.queue) == 0
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print(my_queue.dequeue())  # Output: 10
print(my_queue.dequeue())  # Output: 20
print(my_queue.isEmpty())  # Output: False
print(my_queue.dequeue())  # Output: 30
print(my_queue.isEmpty())  # Output: True
