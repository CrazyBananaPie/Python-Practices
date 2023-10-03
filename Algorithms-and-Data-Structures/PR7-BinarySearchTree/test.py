from list import JustList
from tree import SearchBinaryTree
from pr_2 import Generator


def test_add_tree_10000():
    g = Generator()
    b = SearchBinaryTree()
    sm_l = g.generate_10000()
    for el in sm_l:
        b.insert(el)


def test_find_tree_10000():
    g = Generator()
    b = SearchBinaryTree()
    sm_l = g.generate_10000()
    for el in sm_l:
        b.insert(el)
    for el in sm_l:
        b.find(el)


def test_add_list_10000():
    g = Generator()
    jl = JustList()
    sm_l = g.generate_10000()
    for el in sm_l:
        jl.add(el)


def test_find_list_10000():
    g = Generator()
    jl = JustList()
    sm_l = g.generate_10000()
    for el in sm_l:
        jl.add(el)
    for el in sm_l:
        jl.find(el)
