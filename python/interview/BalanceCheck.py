class Stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
def balance_check(s):
    stack = Stack()
    lst = list(s)
    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return False
    if lst[0] == ")" or lst[0] == "]" or lst[0] == "}":
        return False
    stack.push(lst[0])
    for i in range(1,len(lst)):
        if lst[i] == ")" and stack.peek() == "(":
            stack.pop()
        elif lst[i] == "]" and stack.peek() == "[":
            stack.pop()
        elif lst[i] == "}" and stack.peek() == "{":
            stack.pop()
        else:
            stack.push(lst[i])
    
    return stack.isEmpty()
        
def balance_check2(s):
    if len(s)%2 != 0:
        return False
    opening = set('([{')
    matches = set([ ('(',')'), ('[',']'), ('{','}') ])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open,paren) not in matches:
                return False
    return len(stack) == 0
