import random
from pr_2 import Generator
from sort_algs import SortAlg


print("Standard preparing of class objects...")
s = SortAlg()
g = Generator()

print("Creating an array, filled with values..")
for _ in range(6):
    s.add(g.generate_single())

print("\nThe elements of array:")
for key, el in enumerate(s.get_all()):
    print(f"#{key}:  Element =--->  {el}")

print("""\nMETHOD SORT()
Testing only the situation of sorting array:
1 - sorting the array""")

print(f"\n1. Sorting array...")
print(f"Output of the method: {s.sort()}")

print("\nThe result of sorting (will be used for the testing of the next method):")
for key, el in enumerate(s.get_all()):
    print(f"#{key}:  Element =--->  {el}")

print("""\nMETHOD SORT_BY(attr):
Testing with:
1 - correct attribute
2 - error-attribute""")

attrs = random.choice(['size', 'model', 'mem_type', 'frequency', 'timing'])
print(f"\n1. Trying to sort array by correct attribute ! {attrs} !...")
print(f"Output of the method: {s.sort_by(attrs)}")

print(f"\nThe result of sorting by attribute ! {attrs} !:")
for key, el in enumerate(s.get_all()):
    print(f"#{key}:  Element =--->  {el}")

attrs = 'season'
print(f"\n2. Trying to sort by error-attribute ! {attrs} ! (checking the AttributeError)...")
print(f"Output of the method: {s.sort_by(attrs)}")

print(f"\nChecking that array was not changed by error-attribute ! {attrs} !:")
for key, el in enumerate(s.get_all()):
    print(f"#{key}:  Element =--->  {el}")
