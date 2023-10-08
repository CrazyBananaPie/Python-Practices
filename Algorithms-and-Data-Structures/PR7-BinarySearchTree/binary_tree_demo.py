from data_structures import BinaryTree
from models_and_generators import Generator, RAM

print("Standard preparing of class objects...")
binary_tree = BinaryTree()
gen = Generator()

print("Creating a binary tree... (testing INSERT METHOD)")
for _ in range(13):
    binary_tree.insert(gen.generate_single())

print("\nThe elements of tree: (testing GET_ALL METHOD)")
for key, element in enumerate(binary_tree.get_all()):
    print(f"#{key}:  Element =--->  {element}")

print("""\nMETHOD FIND()
Testing the situations when:
1 - value is in the tree
2 - value is not""")

print(f"\n1. Searching value...")
ram = gen.generate_single()
binary_tree.insert(ram)
print(f"Output of the method: {binary_tree.find(ram)}")

ram = gen.generate_single()
while binary_tree.find(ram):
    ram = gen.generate_single()

print("\n2. Searching value with fail...")
print(f"Output of the method: {binary_tree.find(ram)}")

print("""\nMETHOD FIND_BY(attrs, values):
Testing with:
1 - correct attribute
2 - error-attribute""")

ram = RAM("Kingston", "ZP", 6, "DDR3", 1666, 3)
binary_tree.insert(ram)
values = ["Kingston", "ZP", 6]
attrs = ['manufacturer', 'model', 'size']
print(f"\n1. Trying to find element by correct attributes ! {attrs} : {values} !...")
print(f"Output of the method(__repr__ METHOD WORK): {binary_tree.find_by(attrs, values)}")

attrs = ['manufacturer', 'models1', 'size']
print(f"\n2. Trying to sort by error-attribute ! {attrs} ! (checking the AttributeError)...")
print(f"Output of the method: {binary_tree.find_by(attrs, values)}")

print("""\nMETHOD REPLACE:
Testing only:
1 - variant with existing element""")
c = gen.generate_single()
print(c)
print(f"Output of the method: {binary_tree.replace(ram, c)}")

print("""\nMETHODS MIN, MAX, __len__:
Testing only:
1 - outputs of all methods""")
c = gen.generate_single()
print(c)
print(f"Output of the methods: MIN: {binary_tree.min()}, MAX: {binary_tree.max()}, LEN: {len(binary_tree)}")

print("\nThe elements of tree:")
for key, element in enumerate(binary_tree.get_all()):
    print(f"#{key}:  Element =--->  {element}")

print("The last method: REMOVE a few elements")
print("Methods output")
print(binary_tree.remove(binary_tree.max()))
print(binary_tree.remove(binary_tree.max()))
print(binary_tree.remove(binary_tree.min()))
print(binary_tree.remove(binary_tree.min()))
print(binary_tree.remove(binary_tree.min()))

print("\nThe elements of tree: (testing GET_ALL METHOD)")
for key, element in enumerate(binary_tree.get_all()):
    print(f"#{key}:  Element =--->  {element}")