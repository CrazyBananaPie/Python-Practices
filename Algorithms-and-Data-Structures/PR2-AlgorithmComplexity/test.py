from pr_2 import RAM
from pr_2 import Generator


def test_ram():
    r = RAM("some", "example", 132, "testing", 1000, 1)
    assert r.manufacturer == "some"
    assert r.model == "example"
    assert r.size == 132
    assert r.mem_type == "testing"
    assert r.frequency == 1000
    assert r.timing == 1


def test_gen_single_types():
    g = Generator()
    s = g.generate_single()
    assert isinstance(s, RAM)
    assert isinstance(s.manufacturer, str)
    assert isinstance(s.model, str)
    assert isinstance(s.size, int)
    assert isinstance(s.mem_type, str)
    assert isinstance(s.frequency, int)
    assert isinstance(s.timing, int)


def test_gen_1000_type():
    g = Generator()
    l = g.generate_1000()
    assert isinstance(l, list)
    assert isinstance(l[0], RAM)
    assert len(l) == 1000


def test_gen_10000_type():
    g = Generator()
    bl = g.generate_10000()
    assert isinstance(bl, list)
    assert isinstance(bl[0], RAM)
    assert len(bl) == 10000
