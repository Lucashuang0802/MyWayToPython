
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def push(self, data):
        if data is None: return False
        # instead of inserting at the end, we can insert at the head
        new_node = StackNode(data)
        new_node.next = self.root
        self.root = new_node
        return True

    def pop(self):
        if self.root is None: return False
        
        return_node = self.root
        self.root = return_node.next
        return return_node.data

    def peek(self):
        return False if self.root is None else self.root.data

# Driver program to test above class 
stack = Stack()
stack.push(10)        
stack.push(20)
stack.push(30)
 
print("%d popped from stack" % (stack.pop()))
print("Top element is %d " %(stack.peek()))
print("%d popped from stack" % (stack.pop()))
print("Top element is %d " %(stack.peek()))
print("%d popped from stack" % (stack.pop()))
print("Top element is %d " %(stack.peek()))
print("%d popped from stack" % (stack.pop()))
print("Top element is %d " %(stack.peek()))
