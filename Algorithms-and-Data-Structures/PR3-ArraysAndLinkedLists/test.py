import random
from list import JustList
from pr_2 import Generator
from linked_list import SingleLinkList


def test_list_10000_head():
    g = Generator()
    el = g.generate_10000()
    sm_list = JustList()
    for elem in el:
        sm_list.add(elem, 0)


def test_linked_list_10000_head():
    g = Generator()
    el = g.generate_10000()
    link_list = SingleLinkList()
    for elem in el:
        link_list.add(elem, 0)


def test_list_10000_tail():
    g = Generator()
    el = g.generate_10000()
    sm_list = JustList()
    for elem in el:
        sm_list.add(elem)
    return sm_list


def test_linked_list_10000_tail():
    g = Generator()
    el = g.generate_10000()
    link_list = SingleLinkList()
    for elem in el:
        link_list.add(elem)
    return link_list


def test_list_change_10000_el():
    sm_list = test_list_10000_tail()
    new_list = test_list_10000_tail()
    for i in range(10000):
        sm_list.insert(new_list.get(i), i)


def test_linked_list_change_10000_el():
    link_list = test_linked_list_10000_tail()
    new_list = test_linked_list_10000_tail()
    for i in range(new_list.length):
        link_list.insert(new_list.get(i), i)


def test_list_find_10000():
    sm_list = test_list_10000_tail()
    num = random.randint(4500, 5500)

    element = sm_list.get(0)
    sm_list.find(element)

    element = sm_list.get(sm_list.size - 1)
    sm_list.find(element)

    element = sm_list.get(num)
    sm_list.find(element)


def test_linked_list_find_10000():
    link_list = test_linked_list_10000_tail()
    num = random.randint(4500, 5500)

    element = link_list.get(0)
    link_list.find(element)

    element = link_list.get(link_list.length - 1)
    link_list.find(element)

    element = link_list.get(num)
    link_list.find(element)


def test_list_index_10000():
    sm_list = test_list_10000_tail()
    num = 4300

    element = sm_list.get(num)


def test_linked_list_index_10000():
    link_list = test_linked_list_10000_tail()
    num = 4300

    element = link_list.get(num)


def test_list_remove_10000():
    sm_list = test_list_10000_tail()

    while sm_list.size != 0:
        element = sm_list.get(0)
        sm_list.remove(element)

    sm_list = test_list_10000_tail()

    while sm_list.size != 0:
        element = sm_list.get(sm_list.size - 1)
        sm_list.remove(element)


def test_linked_list_remove_10000():
    link_list = test_linked_list_10000_tail()

    while link_list.length != 0:
        element = link_list.get(0)
        link_list.remove(element)

    link_list = test_linked_list_10000_tail()

    while link_list.length != 0:
        element = link_list.get(link_list.length - 1)
        link_list.remove(element)

