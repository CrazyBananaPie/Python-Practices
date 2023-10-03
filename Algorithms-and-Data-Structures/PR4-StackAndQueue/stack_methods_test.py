from cls_gen_and_ram import Generator
from stack import Stack

s = Stack()
g = Generator()

print("Method PUSH combined with method TOP")
s.push(g.generate_single())
print(s.top())
s.push(g.generate_single())
print(s.top())
s.push(g.generate_single())
print(s.top())
s.push(g.generate_single())
print(s.top(), '\n')

print("Printing the output of method POP (5 times)")
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop(), '\n')

print(f"Printing top in empty stack: {s.top()}")
