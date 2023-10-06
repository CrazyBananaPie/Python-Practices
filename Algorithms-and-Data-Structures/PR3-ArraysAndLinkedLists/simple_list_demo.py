from data_structures import SimpleList
from models_and_generators import Generator

simple_list = SimpleList()
gen = Generator()

simple_list.add(gen.generate_single())
simple_list.add(gen.generate_single())
simple_list.add(gen.generate_single())
simple_list.add(gen.generate_single())
simple_list.add(gen.generate_single())

print("Original of the list: ", simple_list.get_all())

print("""Method ADD: 
1 - without index
2 - with index
3 - with incorrect index
""")

print("#1")
simple_list.add("EXAMPLE#1")
print(simple_list.get_all(), "\n")

print("#2")
simple_list.add("EXAMPLE#2", 1)
print(simple_list.get_all(), "\n")

print("#3")
print(simple_list.add(gen.generate_single(), 67))
print(simple_list.get_all(), "\n")


print("""Method INSERT:
1 - index is in range of the list
2 - index is not in range of the list
""")

print("#1")
simple_list.insert("INSERTING", 1)
print(simple_list.get_all(), "\n")

print("#2")
print(simple_list.insert(gen.generate_single(), -1))
print(simple_list.get_all(), "\n")


print("""Method REMOVE
1 - value in list
2 - value not in list
""")

print("#1")
simple_list.remove("INSERTING")
print(simple_list.get_all(), "\n")

print("#2")
print(simple_list.remove(gen.generate_single()))
print(simple_list.get_all(), "\n")


print("""Method GET:
1 - index in range
2 - index not in range
""")

print("#1")
print(simple_list.get(4), "\n")

print("#2")
print(simple_list.get(1000), "\n")


print("""Method FIND:
1 - data in list
2 - not in list
""")

print("#1")
print(simple_list.find("EXAMPLE#1"), "\n")

print("#2")
print(simple_list.find("NODATA"), "\n")


print("""Method GET_ALL:""")
print(simple_list.get_all())


