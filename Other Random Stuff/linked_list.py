class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5


# finding 3 (which is in the middle)
nodes = node_1
while nodes.val != 3:
    nodes = nodes.next
print(nodes.val)

# adding 3.5 between 3 and 4
print('\n')

new_node = Node(3.5)
new_node.next = nodes.next
nodes.next = new_node

print('\n')

node = node_1
while node:
    print(node.val)
    node = node.next
