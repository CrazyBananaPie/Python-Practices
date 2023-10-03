from list import JustList
from sort_algs import SortAlg
from pr_2 import Generator


def test_list_sort_10000():
    g = Generator()
    jl = JustList()

    for el in g.generate_10000():
        jl.add(el)
    assert jl.size == 10000

    jl.sort()


def test_self_sort_10000():
    g = Generator()
    s = SortAlg()

    for el in g.generate_10000():
        s.add(el)
    assert s.length == 10000

    s.sort()
