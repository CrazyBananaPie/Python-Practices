import random
from pr_2 import RAM, Generator
from find_alg import FindAlg

print("Standard preparing of class objects...")
f = FindAlg()
g = Generator()

print("Creating an organized array, filled with values..")
for _ in range(6):
    f.add(g.generate_single())
example = RAM("Kingston", "ZP", 6, "DDR3", 1666, 3)
f.add(example)

print("\nThe elements of array:")
for key, el in enumerate(f.get_all()):
    print(f"#{key}:  Element =--->  {el}")

print("""\nMETHOD OBJ_FIND
Testing with:
1 - variable from the list
2 - variable not from the list""")

example1 = f.get_all()[random.randint(0, 7)]
print(f"\n1. Trying to find the chosen element: {example1} ...")
print(f"Result: {f.obj_find(example1)}")

example2 = example1
while example2 in f.get_all():
    example2 = g.generate_single()
print(f"\n2. Trying to find the failed element: {example2} ...")
print(f"Result: {f.obj_find(example2)}")

print("\nThe elements of array:")
for key, el in enumerate(f.get_all()):
    print(f"#{key}:  Element =--->  {el}")

print("""\nMETHOD FIND_BY_ATTR
Testing with:
1 - variable from the list
2 - variable not from the list
3 - error-attributes""")

attrs = ['manufacturer', 'model', 'size']
values = ['Kingston', 'ZP', 6]
print(f"""\n1. Trying to find the chosen element by attributes...
element: {example}
attributes: {attrs}
values: {values}""")

print(f"Result: {f.find_by_attr(attrs, values)}")

values = ['Kingstone', 'ZPRQ', 613]
print(f"""\n2. Trying to find the failed element by attributes (changing the searched values of attributes)...
attributes: {attrs}
values: {values}""")

print(f"Result: {f.find_by_attr(attrs, values)}")

attrs = ['manufacturer', 'season', 'size']
values = ['Kingston', 'ZP', 6]
example2 = g.generate_single()
print(f"""\n3. Trying to find the element by error of the attributes (checking the AttributeError)...
element: {example2}
attributes: {attrs}
values: {values}""")

print(f"Result: {f.find_by_attr(attrs, values)}")
