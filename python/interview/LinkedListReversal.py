class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        
def reverse_list(node):
    node_array = []
    marker = node
    while marker.nextnode != None:
        node_array.append(marker)
        marker = marker.nextnode
    new_head = marker
    while node_array:
        marker.nextnode = node_array.pop()
        marker = marker.nextnode
    marker.nextnode = None
    return new_head

def reverse(head):
    current = head
    previous = None
    nextnode = None
    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode
    return previous

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverse(a).value

print(b.nextnode.value)
print(c.nextnode.value)
print(d.nextnode.value)
