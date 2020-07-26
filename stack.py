from collections import deque

stack = deque()
stack.append("First Element")
stack.append("Second Element")
stack.append("Third Element")
stack.append("Fourth Element")
print(stack)

# Alternate Way

class Stack:
    def __init__(self):
        self.container = deque()
    def __str__(self):
        res = list(map(str,self.container))
        res.reverse()
        ret = "Output Sequence : "
        ret += " -> ".join(res)
        return ret
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def is_empty(self):
        return len(self.container) == 0

stack_obj = Stack()
for item in stack:
    stack_obj.push(item)
print(stack_obj)

ques = "We will conquere COVID-19"
stack_obj2 = Stack()
for char in ques:
    stack_obj2.push(char)
res = ''
while stack_obj2.is_empty() is False:
    res += stack_obj2.pop()
print(res)

ques2 = input("INPUT :")
stack_obj3 = Stack()
flag = 0
for char in ques2:
    if (char == "{") or (char == "(") or (char == "["):
        stack_obj3.push(char)
    elif char == ")":
        if stack_obj3.is_empty():
            flag = 1
            break
        elif stack_obj3.peek() == "(":
            stack_obj3.pop()
        else:
            flag = 1
            break
    elif char == "}":
        if stack_obj3.is_empty():
            flag = 1
            break
        elif stack_obj3.peek() == "{":
            stack_obj3.pop()
        else:
            flag = 1
            break
    elif char == "]":
        if stack_obj3.is_empty():
            flag = 1
            break
        elif stack_obj3.peek() == "[":
            stack_obj3.pop()
        else:
            flag = 1
            break
if flag == 1:
    print("False")
else:
    print("True")