from data_structures import SimpleList, BinaryTree
from models_and_generators import Generator


def test_add_10000_elements_tree():
    gen = Generator()
    binary_tree = BinaryTree()

    input_data = gen.generate_10000()
    for element in input_data:
        binary_tree.insert(element)


def test_find_10000_elements_tree():
    gen = Generator()
    binary_tree = BinaryTree()

    input_data = gen.generate_10000()
    for element in input_data:
        binary_tree.insert(element)

    for element in input_data:
        binary_tree.find(element)


def test_add_list_10000():
    gen = Generator()
    simple_list = SimpleList()

    input_data = gen.generate_10000()
    for element in input_data:
        simple_list.add(element)


def test_find_list_10000():
    gen = Generator()
    simple_list = SimpleList()

    input_data = gen.generate_10000()
    for element in input_data:
        simple_list.add(element)

    for element in input_data:
        simple_list.find(element)
