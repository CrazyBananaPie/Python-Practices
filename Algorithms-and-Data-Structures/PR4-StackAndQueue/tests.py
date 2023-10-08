from data_structures import Queue, Stack
from models_and_generators import Generator


def test_stack_push_10000_elements():
    stack = Stack()
    gen = Generator()
    input_data = gen.generate_10000()

    for element in input_data:
        stack.push(element)

    return stack


def test_queue_enqueue_10000_elements():
    queue = Queue()
    gen = Generator()
    input_data = gen.generate_10000()

    for element in input_data:
        queue.enqueue(element)

    return queue


def test_stack_pop_10000_elements():
    stack = test_stack_push_10000_elements()

    while stack.pop():
        stack.pop()


def test_queue_dequeue_10000_elements():
    queue = test_queue_enqueue_10000_elements()

    while queue.dequeue():
        queue.dequeue()
