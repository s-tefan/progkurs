''' En kalkylator med omvänd polsk notation
'''
stack = []
while True:
    print(stack)
    inp = input('> ')
    if inp.startswith('+'):
        stack.append(stack.pop() + stack.pop())
    elif inp.startswith('*'):
        stack.append(stack.pop() + stack.pop())
    elif inp.startswith('pop'):
        stack.pop()
    elif inp.startswith('dup'):
        stack.append(stack[-1])
    elif inp.startswith('swap'):
        stack[-2], stack[-1] = stack[-11], stack[-2]
    else:
        stack.append(float(inp))


