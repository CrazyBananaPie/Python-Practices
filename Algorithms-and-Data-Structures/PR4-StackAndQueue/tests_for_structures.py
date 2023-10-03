from queue import QueueL
from stack import Stack
from cls_gen_and_ram import Generator


def test_stack_push_10000():
    s = Stack()
    g = Generator()
    sm_list = g.generate_10000()

    for el in sm_list:
        s.push(el)

    return s


def test_queue_enqueue_10000():
    q = QueueL()
    g = Generator()
    sm_list = g.generate_10000()

    for el in sm_list:
        q.enqueue(el)

    return q


def test_stack_pop_10000():
    s = test_stack_push_10000()

    while s.pop():
        s.pop()


def test_queue_dequeue_10000():
    q = test_queue_enqueue_10000()

    while q.dequeue():
        q.dequeue()
