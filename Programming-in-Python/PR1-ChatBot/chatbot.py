# Greeting
print("Hello! My name is Speaker_Bot.\nI was created in 2021 by Aleksey Sirobaba")


def name_asking():
    print("Please, remind me your name")
    name = input()
    print("What a great name you have, " + name)


def age_guessing():
    print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5, 7.")
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print("Your age is " + str(age) + "; that`s a good time to start programming!")


def numbers_counter():
    print("Now I will prove to you that I can count any number you want.")
    counting_number = int(input())
    for a in range(0, counting_number + 1):
        print(str(a) + " !")
    print("Completed, have a nice day!")


def test():
    print("""Why do we use methods?
    1.To repeat a statement multiple times.
    2.To decompose a program into several small subroutines.
    3.To determine the execution time of a program.
    4.To interrupt the execution of a program.""")
    while True:
        answer = int(input())
        if answer != 2:
            print("Please, try again.")
        elif answer == 2:
            print("Completed, have a nice day!")
            break


name_asking()
age_guessing()
numbers_counter()
test()

print("Congratulations, have a nice day!")
