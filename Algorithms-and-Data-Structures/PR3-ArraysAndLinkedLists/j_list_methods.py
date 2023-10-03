from list import JustList
from pr_2 import Generator

new_list = JustList()
g = Generator()

new_list.add(g.generate_single())
new_list.add(g.generate_single())
new_list.add(g.generate_single())
new_list.add(g.generate_single())
new_list.add(g.generate_single())

print("Original of the list: ", new_list.get_all())

print("""Method ADD: 
1 - without index
2 - with index
3 - with incorrect index
""")

print("#1")
new_list.add("EXAMPLE#1")
print(new_list.get_all(), "\n")

print("#2")
new_list.add("EXAMPLE#2", 1)
print(new_list.get_all(), "\n")

print("#3")
print(new_list.add(g.generate_single(), 67))
print(new_list.get_all(), "\n")


print("""Method INSERT:
1 - index is in range of the list
2 - index is not in range of the list
""")

print("#1")
new_list.insert("INSERTING", 1)
print(new_list.get_all(), "\n")

print("#2")
print(new_list.insert(g.generate_single(), -1))
print(new_list.get_all(), "\n")


print("""Method REMOVE
1 - value in list
2 - value not in list
""")

print("#1")
new_list.remove("INSERTING")
print(new_list.get_all(), "\n")

print("#2")
print(new_list.remove(g.generate_single()))
print(new_list.get_all(), "\n")


print("""Method GET:
1 - index in range
2 - index not in range
""")

print("#1")
print(new_list.get(4), "\n")

print("#2")
print(new_list.get(1000), "\n")


print("""Method FIND:
1 - data in list
2 - not in list
""")

print("#1")
print(new_list.find("EXAMPLE#1"), "\n")

print("#2")
print(new_list.find("NODATA"), "\n")


print("""Method GET_ALL:""")
print(new_list.get_all())


