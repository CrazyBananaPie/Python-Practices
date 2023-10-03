from tree import SearchBinaryTree
from pr_2 import Generator, RAM


print("Standard preparing of class objects...")
b = SearchBinaryTree()
g = Generator()

print("Creating a binary tree... (testing INSERT METHOD)")
for _ in range(13):
    b.insert(g.generate_single())

print("\nThe elements of tree: (testing GET_ALL METHOD)")
for key, el in enumerate(b.get_all()):
    print(f"#{key}:  Element =--->  {el}")

print("""\nMETHOD FIND()
Testing the situations when:
1 - value is in the tree
2 - value is not""")

print(f"\n1. Searching value...")
a = g.generate_single()
b.insert(a)
print(f"Output of the method: {b.find(a)}")

a = g.generate_single()
while b.find(a):
    a = g.generate_single()

print("\n2. Searching value with fail...")
print(f"Output of the method: {b.find(a)}")

print("""\nMETHOD FIND_BY(attrs, values):
Testing with:
1 - correct attribute
2 - error-attribute""")

a = RAM("Kingston", "ZP", 6, "DDR3", 1666, 3)
b.insert(a)
values = ["Kingston", "ZP", 6]
attrs = ['manufacturer', 'model', 'size']
print(f"\n1. Trying to find element by correct attributes ! {attrs} : {values} !...")
print(f"Output of the method(__repr__ METHOD WORK): {b.find_by(attrs, values)}")

attrs = ['manufacturer', 'models1', 'size']
print(f"\n2. Trying to sort by error-attribute ! {attrs} ! (checking the AttributeError)...")
print(f"Output of the method: {b.find_by(attrs, values)}")

print("""\nMETHOD REPLACE:
Testing only:
1 - variant with existing element""")
c = g.generate_single()
print(c)
print(f"Output of the method: {b.replace(a, c)}")

print("""\nMETHODS MIN, MAX, __len__:
Testing only:
1 - outputs of all methods""")
c = g.generate_single()
print(c)
print(f"Output of the methods: MIN: {b.min()}, MAX: {b.max()}, LEN: {len(b)}")

print("The last method: REMOVE a few elements")
print("Methods output")
print(b.remove(b.max()))
print(b.remove(b.max()))
print(b.remove(b.max()))
print(b.remove(b.min()))
print(b.remove(b.min()))
print(b.remove(b.min()))
