from data_structures import Stack
from models_and_generators import Generator

stack = Stack()
gen = Generator()

print("Method PUSH combined with method TOP")
stack.push(gen.generate_single())
print(stack.top())
stack.push(gen.generate_single())
print(stack.top())
stack.push(gen.generate_single())
print(stack.top())
stack.push(gen.generate_single())
print(stack.top(), '\n')

print("Printing the output of method POP (5 times)")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop(), '\n')

print(f"Printing top in empty stack: {stack.top()}")
