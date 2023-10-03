from queue import QueueL
from cls_gen_and_ram import Generator

q = QueueL()
g = Generator()

q.enqueue(g.generate_single())
q.enqueue(g.generate_single())
q.enqueue(g.generate_single())
q.enqueue(g.generate_single())


print(f"""Method ENQUEUE combined with GET_ALL:
{q.get_all()}
""")

print(f"""Length of Queue:
{q.__len__()}
""")

print(f"""Front element:
{q.front()}
""")

print("DEQUEUE method for all elements and when there are no elements:")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.get_all())
print(f"No elements: {q.dequeue()}\n")

print(f"""Length of empty queue:{q.__len__()}, front:{q.front()}""")

