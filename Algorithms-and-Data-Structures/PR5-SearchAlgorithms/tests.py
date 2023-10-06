from models_and_generators import Generator
from search_algorithms import SearchAlgorithms
from data_structures import SimpleList, OrganizedArray


def test_search_algorithm_10000():
    search_algorithms = SearchAlgorithms()
    organized_array = OrganizedArray()
    gen = Generator()

    for element in gen.generate_10000():
        organized_array.add(element)
    array_body = organized_array.get_all()

    assert len(array_body) == 10000

    for element in array_body:
        search_algorithms.find_object(array_body, element)


def test_find_list_10000():
    simple_list = SimpleList()
    gen = Generator()

    for element in gen.generate_10000():
        simple_list.add(element)

    assert len(simple_list.get_all()) == 10000

    for element in simple_list.get_all():
        simple_list.find(element)
