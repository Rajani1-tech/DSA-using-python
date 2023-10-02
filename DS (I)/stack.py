# stack implementation in python

#creating a stack
def create_stack():
    stack = []
    return stack


# creating an empty stack
def check_empty(stack):
    return len(stack)== 0

# adding items into stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)

# removing an element from the stack
def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
push(stack, str(7))
push(stack, str(8))
print("popped item: " + pop(stack))
print("stack after poppong an element:" + str(stack))    
