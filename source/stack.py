class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item: str):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def flush(self):
        self.items = []

    def __str__(self) -> str:
        string = ""
        string += "[ "
        for item in self.items:
            string += item + " "
        string += "]"
        return string