from pr_2 import Generator
from find_alg import FindAlg
from list import JustList


def test_find_obj_self_10000():
    f = FindAlg()
    g = Generator()
    for el in g.generate_10000():
        f.add(el)
    assert len(f.get_all()) == 10000
    for el in f.get_all():
        f.obj_find(el)


def test_find_list_10000():
    l = JustList()
    g = Generator()
    for el in g.generate_10000():
        l.add(el)
    assert len(l.get_all()) == 10000
    for el in l.get_all():
        l.find(el)