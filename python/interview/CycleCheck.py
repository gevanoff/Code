class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        
def cycle_check(node):
    node_seen = set()
    while node.nextnode != None:
        if node.nextnode in node_seen:
            return True
        else:
            node_seen.add(node.nextnode)
    return False

def cycle_check2(node):
    marker1 = node
    marker2 = node
    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        if marker2 == marker1:
            return True
    return False

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a

cycle_check(a)
