class Stack:
    

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False

        pass

    def push(self, e):
        a=len(self.stack)
        self.stack.insert(a,e)
        return None
        pass
    def pop(self):
        a=self.stack[-1]
        del self.stack[-1]
        return a
        pass

        return
