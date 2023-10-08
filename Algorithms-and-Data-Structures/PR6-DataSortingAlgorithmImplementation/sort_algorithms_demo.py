import random
from models_and_generators import Generator
from sort_algorithms import SortAlgorithms
from data_structures import DynamicArray

print("Standard preparing of class objects...")
sort_algs = SortAlgorithms()
gen = Generator()
dynamic_array = DynamicArray()

print("Creating an array filled with values..")
for _ in range(6):
    dynamic_array.add(gen.generate_single())

array_body = dynamic_array.get_all()

print("\nThe elements of array:")
for key, el in enumerate(array_body):
    print(f"#{key}:  Element =--->  {el}")

print("""\nMETHOD SORT()
Testing only the situation of sorting array:
1 - sorting the array""")

print(f"\n1. Sorting array...")
print(f"Output of the method: {sort_algs.sort(array_body)}")

print("\nThe result of sorting (will be used for the testing of the next method):")
for key, el in enumerate(array_body):
    print(f"#{key}:  Element =--->  {el}")

print("""\nMETHOD SORT_BY(attr):
Testing with:
1 - correct attribute
2 - error-attribute""")

attr: str = random.choice(["size", "model", "memory_type", "frequency", "timing"])
print(f"\n1. Trying to sort array by correct attribute ! {attr} !...")
print(f"Output of the method: {sort_algs.sort_by(array_body, attr)}")

print(f"\nThe result of sorting by attribute ! {attr} !:")
for key, el in enumerate(array_body):
    print(f"#{key}:  Element =--->  {el}")

attr = 'season'
print(f"\n2. Trying to sort by error-attribute ! {attr} ! (checking the AttributeError)...")
print(f"Output of the method: {sort_algs.sort_by(array_body, attr)}")

print(f"\nChecking that array was not changed by error-attribute ! {attr} !:")
for key, el in enumerate(array_body):
    print(f"#{key}:  Element =--->  {el}")
