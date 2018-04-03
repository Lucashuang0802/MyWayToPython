
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, val):
        if not val: return None
        find_node = self.head
        while find_node:
            if find_node.data == val: return find_node
            find_node = find_node.next
        return None

    def insert_at_front(self, val):
        if val is None: return False
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        return True
    
    def insert_at_node(self, node, val):
        if val is None or not node: return False
        find_node = self.head
        while find_node:
            if find_node == node:
                new_node = Node(val)
                new_node.next = find_node.next
                find_node.next = new_node
                return True
            find_node = find_node.next
        return False

    def insert_at_end(self, val):
        if val is None: return False

        # insert as a new head
        if not self.head:
            self.head = Node(val)
            return True

        # insert to an existing list
        end_node = self.head
        while end_node and end_node.next:
            end_node = end_node.next
        end_node.next = Node(val)
        return True

    def traverse_and_print(self):
        if not self.head: return ""
        res = []
        node = self.head
        while node:
            res.append(str(node.data))
            node = node.next
        return '->'.join(res)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_front(12)
    ll.insert_at_end(13)
    ll.insert_at_end(14)
    ll.insert_at_front(15)
    ll.insert_at_front(None)

    node = ll.find(15)
    ll.insert_at_node(node, 16)

    node = ll.find(20)
    ll.insert_at_node(node, 100)

    print(ll.traverse_and_print())
