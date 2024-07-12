class CircularQueue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.queue = [None] * capacity
    
    def enqueue(self,item):
        if self.is_full():
            raise Exception("Pila llena")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Pila vacía")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity


# uCrea una cola circular de al menos 6 elementos.
cola = CircularQueue(6)

# uCrea un ciclo para que se vallan introduciendo los siguientes valores: [20,10,80,30,40,90]
for valores in [20, 10, 80, 30, 40, 90]:
    cola.enqueue(valores)

#uElimina 3 de los elementos.
cola.dequeue()
cola.dequeue()
cola.dequeue()

#uImprime los resultados
while not cola.is_empty():
    print(cola.dequeue())


