from main import RAM, Generator

def test_ram_creation():
    ram = RAM("some", "example", 132, "testing", 1000, 1)
    assert ram.manufacturer == "some"
    assert ram.model == "example"
    assert ram.size == 132
    assert ram.memory_type == "testing"
    assert ram.frequency == 1000
    assert ram.timing == 1


def test_gen_single_types():
    gen = Generator()
    ram = gen.generate_single()
    assert isinstance(ram, RAM)
    assert isinstance(ram.manufacturer, str)
    assert isinstance(ram.model, str)
    assert isinstance(ram.size, int)
    assert isinstance(ram.memory_type, str)
    assert isinstance(ram.frequency, int)
    assert isinstance(ram.timing, int)


def test_gen_1000_type():
    gen = Generator()
    ram_list = gen.generate_1000()
    assert isinstance(ram_list, list)
    assert isinstance(ram_list[0], RAM)
    assert len(ram_list) == 1000


def test_gen_10000_type():
    gen = Generator()
    ram_list = gen.generate_10000()
    assert isinstance(ram_list, list)
    assert isinstance(ram_list[0], RAM)
    assert len(ram_list) == 10000
