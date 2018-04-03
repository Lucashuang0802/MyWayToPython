N = 5
M = ')'

class Node:
    def __init__(self, key):
        self.key = key
        self.children = [None] * N
    
def serialize(root, fp):
    if root:    
        fp.write(root.key)  
    for i in range(len(root.children)):
        if root.children[i]:
            serialize(root.children[i], fp)
    fp.write(M)

def traverse(root):
    if root:    
        print(root.key)
    for i in range(len(root.children)):
        if root.children[i]:
            traverse(root.children[i])

def deserialize(root, fp):
    
    next_char = fp.read(1)
    if not next_char or next_char == M:
        return

    root = Node(next_char)
    for i in range(N):
        deserialize(root.children[i], fp)


def createDummyTree():
    root = Node('A')
    root.children[0] = Node('B')
    root.children[1] = Node('C')
    root.children[2] = Node('D')
    root.children[0].children[0] = Node('E')
    root.children[0].children[1] = Node('F')
    root.children[2].children[0] = Node('G')
    root.children[2].children[1] = Node('H')
    root.children[2].children[2] = Node('I')
    root.children[2].children[3] = Node('J')
    root.children[0].children[1].children[0] = Node('K')
    return root

# with open('n-ary.txt', 'w') as f:
#     root = createDummyTree()
#     serialize(root, f)
#     traverse(root)

with open('n-ary.txt', 'r') as f:
    root = createDummyTree()
    deserialize(root, f)
    traverse(root)
