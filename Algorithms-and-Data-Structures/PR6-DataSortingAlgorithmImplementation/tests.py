from data_structures import SimpleList, DynamicArray
from sort_algorithms import SortAlgorithms
from models_and_generators import Generator


def test_list_sort_10000():
    gen = Generator()
    simple_list = SimpleList()

    for element in gen.generate_10000():
        simple_list.add(element)

    assert simple_list.size == 10000

    simple_list.sort()


def test_custom_algorithm_sort_10000():
    gen = Generator()
    dynamic_array = DynamicArray()
    sort_algorithms = SortAlgorithms()

    for element in gen.generate_10000():
        dynamic_array.add(element)

    assert dynamic_array.length == 10000

    sort_algorithms.sort(dynamic_array.get_all())
