import random

from data_structures import OrganizedArray
from models_and_generators import RAM, Generator
from search_algorithms import SearchAlgorithms

print("Standard preparing of class objects...")
search_algorithms = SearchAlgorithms()
organized_array = OrganizedArray()
gen = Generator()

print("Creating an organized array, filled with values..")
for _ in range(6):
    organized_array.add(gen.generate_single())
example = RAM("Kingston", "ZP", 6, "DDR3", 1666, 3)
organized_array.add(example)

print("\nThe elements of array:")
for key, element in enumerate(organized_array.get_all()):
    print(f"#{key}:  Element =--->  {element}")

array_data = organized_array.get_all()

print("""\nMETHOD FIND_OBJECT
Testing with:
1 - variable from the list
2 - variable not from the list""")

example1 = array_data[random.randint(0, 7)]
print(f"\n1. Trying to find the chosen element: {example1} ...")
print(f"Result: {search_algorithms.find_object(array_data, example1)}")

example2 = example1
while example2 in array_data:
    example2 = gen.generate_single()
print(f"\n2. Trying to find the failed element: {example2} ...")
print(f"Result: {search_algorithms.find_object(array_data, example2)}")

print("\nThe elements of array:")
for key, element in enumerate(array_data):
    print(f"#{key}:  Element =--->  {element}")

print("""\nMETHOD FIND_OBJECT_BY_ATTRIBUTES
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

print(f"Result: {search_algorithms.find_object_by_attributes(array_data, attrs, values)}")

values = ['Kingstone', 'ZPRQ', 613]
print(f"""\n2. Trying to find the failed element by attributes (changing the searched values of attributes)...
attributes: {attrs}
values: {values}""")

print(f"Result: {search_algorithms.find_object_by_attributes(array_data, attrs, values)}")

attrs = ['manufacturer', 'season', 'size']
values = ['Kingston', 'ZP', 6]
example2 = gen.generate_single()
print(f"""\n3. Trying to find the element by error of the attributes (checking the AttributeError)...
element: {example2}
attributes: {attrs}
values: {values}""")

print(f"Result: {search_algorithms.find_object_by_attributes(array_data, attrs, values)}")
