from data_structures import SingleLinkedList
from models_and_generators import  Generator

linked_List = SingleLinkedList()
gen = Generator()

linked_List.add(gen.generate_single())
linked_List.add(gen.generate_single())
linked_List.add(gen.generate_single())
linked_List.add(gen.generate_single())
linked_List.add(gen.generate_single())

print("Original of linked list: ", linked_List.get_all())

print("""Method ADD: 
1 - without index
2 - with index
3 - with incorrect index
""")

print("#1")
linked_List.add("EXAMPLE#1")
print(linked_List.get_all(), "\n")

print("#2")
linked_List.add("EXAMPLE#2", 1)
print(linked_List.get_all(), "\n")

print("#3")
print(linked_List.add(gen.generate_single(), 67))
print(linked_List.get_all(), "\n")


print("""Method INSERT:
1 - index is in range of the list
2 - index is not in range of the list
""")

print("#1")
linked_List.insert("INSERTING", 1)
print(linked_List.get_all(), "\n")

print("#2")
print(linked_List.insert(gen.generate_single(), -1))
print(linked_List.get_all(), "\n")


print("""Method REMOVE
1 - value in list
2 - value not in list
""")

print("#1")
linked_List.remove("INSERTING")
print(linked_List.get_all(), "\n")

print("#2")
print(linked_List.remove([gen.generate_single()]))
print(linked_List.get_all(), "\n")


print("""Method GET:
1 - index in range
2 - index not in range
""")

print("#1")
print(linked_List.get(4), "\n")

print("#2")
print(linked_List.get(1000), "\n")


print("""Method FIND:
1 - data in list
2 - not in list
""")

print("#1")
print(linked_List.find("EXAMPLE#1"), "\n")

print("#2")
print(linked_List.find("NODATA"), "\n")


print("""Method GET_ALL:""")
print(linked_List.get_all())


