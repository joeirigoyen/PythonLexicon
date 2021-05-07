class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item: str):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        string = ""
        string += "[ "
        for item in self.items:
            string += item + " "
        string += "]"
        return string