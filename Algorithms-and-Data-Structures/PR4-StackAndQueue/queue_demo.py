from data_structures import Queue
from models_and_generators import Generator

queue = Queue()
gen = Generator()

queue.enqueue(gen.generate_single())
queue.enqueue(gen.generate_single())
queue.enqueue(gen.generate_single())
queue.enqueue(gen.generate_single())


print(f"""Method ENQUEUE combined with GET_ALL:
{queue.get_all()}
""")

print(f"""Length of Queue:
{queue.__len__()}
""")

print(f"""Front element:
{queue.front()}
""")

print("DEQUEUE method for all elements and when there are no elements:")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

print(queue.get_all())
print(f"No elements: {queue.dequeue()}\n")

print(f"""Length of empty queue:{queue.__len__()}, front:{queue.front()}""")

