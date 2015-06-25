class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class Tree:

    root = None

    def __init__(self, node=None):
        self.root = node

    def add_node(self, node):
        if not self.root:
            self.root = node
        else:
            self._add(self.root, node)

    def _add(self, root, node):
        if node.data > root.data:
            if not root.right:
                root.right = node
            else:
                self._add(root.right, node)
        else:
            if not root.left:
                root.left = node
            else:
                self._add(root.left, node)
        return

    def add_iter(self, node):
        if self.root == None:
            self.root = node
            return
        current_node = self.root
        while True:
            if current_node == None:
                current_node = node
            elif node.data > current_node.data:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = node
                    break
            else:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = node
                    break

    def _find_highest_value(self):
        if not self.root:
            return
        current_node = self.root
        highest= 0
        while True:
            if current_node.data > highest:
                highest = current_node.data
            if current_node.right:
                current_node = current_node.right
            else:
                break
        return highest

    def find_node(self, node):
        self._find(self.root, node)

    def _find(self, root, node):
        if not root:
            print("Not found")
            return
        else:
            if root.data == node.data:
                print("Found! ")
                return root
            else:
                if root.data > node.data:
                    self._find(root.left, node)
                else:
                    self._find(root.right, node)

    def find_nodeIt(self, node):
        if not self.root:
            print("Not found")
            return
        current_node = self.root
        while True:
            if current_node.data == node.data:
                print("Found!")
                return current_node
            elif current_node.data > node.data:
                if current_node.left:
                    current_node = current_node.left
                else:
                    print("Not found")
                    return
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    print("Not found")
                    return

    def print(self):
        if not self.root:
            print('')
        else:
            print(self.root.data)
            self.print_tree(self.root.left)
            self.print_tree(self.root.right)

    def print_tree(self, root):
        if root:
            print(root.data)
            self.print_tree(root.left)
            self.print_tree(root.right)


t= Tree()

n1 = Node(25, None, None)
n2 = Node(12, None, None)
n3 = Node(35, None, None)
n4 = Node(8, None, None)
n5 = Node(20, None, None)
n6 = Node(30, None, None)
n7 = Node(40, None, None)
n8 = Node(18, None, None)
n9 = Node(3333, None, None)

t.add_node(n1)
t.add_node(n2)
t.add_node(n3)
t.add_node(n4)
t.add_node(n5)
t.add_node(n6)
t.add_node(n7)
t.add_node(n8)

# t.add_iter(n1)
# t.add_iter(n2)
# t.add_iter(n3)
# t.add_iter(n4)
# t.add_iter(n5)
# t.add_iter(n6)
# t.add_iter(n7)
# t.add_iter(n8)

t.print()

# t.find_node(n9)
print('Node with data ', n8.data, t.find_nodeIt(n8))


print('Found three highest node data --> ',t._find_highest_value())