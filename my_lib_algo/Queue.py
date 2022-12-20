class Queue:
     
    def __init__(self):
        self.queue = []

    def is_empty(self) :

        if len(self.queue)==0:
            return True
        else:
            return False

        pass

    def enqueue(self, e):

        a=len(self.queue)
        self.queue.insert(a,e)
        return None
        pass

    def dequeue(self):
        a=self.queue[0]
        del self.queue[0]
        return a
        pass