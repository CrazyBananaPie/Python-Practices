import random
from data_structures import SimpleList, SingleLinkedList
from models_and_generators import Generator


def test_list_insert_10000_elements_head():
    gen = Generator()
    input_data = gen.generate_10000()

    simple_list = SimpleList()
    for element in input_data:
        simple_list.add(element, 0)


def test_linked_list_insert_10000_elements_head():
    gen = Generator()
    input_data = gen.generate_10000()

    linked_list = SingleLinkedList()
    for element in input_data:
        linked_list.add(element, 0)


def test_list_insert_10000_elements_tail():
    gen = Generator()
    input_data = gen.generate_10000()

    simple_list = SimpleList()
    for element in input_data:
        simple_list.add(element)
    return simple_list


def test_linked_list_insert_10000_elements_tail():
    gen = Generator()
    input_data = gen.generate_10000()

    linked_list = SingleLinkedList()
    for element in input_data:
        linked_list.add(element)
    return linked_list


def test_list_change_10000_elements():
    simple_list = test_list_insert_10000_elements_tail()
    input_data = test_list_insert_10000_elements_tail()

    for index in range(10000):
        simple_list.insert(input_data.get(index), index)


def test_linked_list_change_10000_elements():
    link_list = test_linked_list_insert_10000_elements_tail()
    new_list = test_linked_list_insert_10000_elements_tail()

    for index in range(new_list.length):
        link_list.insert(new_list.get(index), index)


def test_list_find_10000_elements():
    simple_list = test_list_insert_10000_elements_tail()
    number = random.randint(4500, 5500)

    element = simple_list.get(0)
    simple_list.find(element)

    element = simple_list.get(simple_list.size - 1)
    simple_list.find(element)

    element = simple_list.get(number)
    simple_list.find(element)


def test_linked_list_find_10000_elements():
    linked_list = test_linked_list_insert_10000_elements_tail()
    number = random.randint(4500, 5500)

    element = linked_list.get(0)
    linked_list.find(element)

    element = linked_list.get(linked_list.length - 1)
    linked_list.find(element)

    element = linked_list.get(number)
    linked_list.find(element)


def test_list_get():
    simple_list = test_list_insert_10000_elements_tail()
    number = 9999

    element = simple_list.get(number)
    return element


def test_linked_list_index_10000():
    link_list = test_linked_list_insert_10000_elements_tail()
    num = 9999

    element = link_list.get(num)
    return element


def test_list_remove_10000():
    simple_list = test_list_insert_10000_elements_tail()

    while simple_list.size != 0:
        element = simple_list.get(0)
        simple_list.remove(element)

    simple_list = test_list_insert_10000_elements_tail()

    while simple_list.size != 0:
        element = simple_list.get(simple_list.size - 1)
        simple_list.remove(element)


def test_linked_list_remove_10000():
    linked_list = test_linked_list_insert_10000_elements_tail()

    while linked_list.length != 0:
        element = linked_list.get(0)
        linked_list.remove(element)

    linked_list = test_linked_list_insert_10000_elements_tail()

    while linked_list.length != 0:
        element = linked_list.get(linked_list.length - 1)
        linked_list.remove(element)
