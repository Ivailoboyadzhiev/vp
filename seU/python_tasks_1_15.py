import random


def task1():
    number = input("Enter an integer: ")
    tuple1 = tuple(number)
    tuple2 = tuple(number[::-1])
    print(tuple1)
    print(tuple2)


def task2():
    n = int(input("Enter the number of elements: "))
    numbers = [random.randint(1, 100) for _ in range(n)]
    result = []

    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(numbers[i] + numbers[i + 1])

    print("Original list:", numbers)
    print("New list:", result)


def task3():
    text = input("Enter text: ")
    counts = {}

    for char in text:
        counts[char] = counts.get(char, 0) + 1

    print(counts)


def task4():
    n = int(input("Enter a positive integer: "))
    numbers = list(range(1, n + 1))
    result = {}

    for i in range(n):
        result[numbers[i]] = numbers[n - i - 1]

    print(result)


def task5():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for _ in range(n):
        numbers.append(int(input("Enter a number: ")))

    minimum = min(numbers)
    maximum = max(numbers)

    print("Minimum:", minimum)
    print("Minimum count:", numbers.count(minimum))
    print("Maximum:", maximum)
    print("Maximum count:", numbers.count(maximum))


def task6():
    numbers = [random.randint(1, 20) for _ in range(10)]
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    print("Original list:", numbers)
    print("List without repetitions:", unique_numbers)


def task7():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for _ in range(n):
        numbers.append(int(input("Enter a number: ")))

    x = int(input("Enter x: "))
    indexes = []

    for i in range(len(numbers)):
        if numbers[i] == x:
            indexes.append(i)

    if indexes:
        print("Indexes:", indexes)
    else:
        print("The number is not in the list.")


def task8():
    n1 = int(input("Enter the number of elements in the first list: "))
    list1 = []

    for _ in range(n1):
        list1.append(int(input("Enter a number: ")))

    n2 = int(input("Enter the number of elements in the second list: "))
    list2 = []

    for _ in range(n2):
        list2.append(int(input("Enter a number: ")))

    result = []

    for number in list1:
        if number in list2 and number not in result:
            result.append(number)

    print(result)


def task9():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for _ in range(n):
        numbers.append(int(input("Enter a number: ")))

    numbers_tuple = tuple(numbers)
    even_numbers = tuple(number for number in numbers_tuple if number % 2 == 0)

    print("Sum:", sum(numbers_tuple))
    print("Average:", sum(numbers_tuple) / len(numbers_tuple))
    print("Even numbers:", even_numbers)


def task10():
    sentence = input("Enter a sentence: ").lower()
    words = sentence.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    print(counts)


def task11():
    n = int(input("Enter the number of students: "))
    students = {}

    for _ in range(n):
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        students[name] = grade

    for name, grade in students.items():
        if grade > 4.50:
            print(name)

    print("Average grade:", sum(students.values()) / len(students))


def task12():
    n1 = int(input("Enter the number of products in the first dictionary: "))
    products1 = {}

    for _ in range(n1):
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        products1[name] = quantity

    n2 = int(input("Enter the number of products in the second dictionary: "))
    products2 = {}

    for _ in range(n2):
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        products2[name] = quantity

    result = products1.copy()

    for name, quantity in products2.items():
        result[name] = result.get(name, 0) + quantity

    print(result)


def task13():
    n1 = int(input("Enter the number of elements in the first set: "))
    set1 = set()

    for _ in range(n1):
        set1.add(int(input("Enter a number: ")))

    n2 = int(input("Enter the number of elements in the second set: "))
    set2 = set()

    for _ in range(n2):
        set2.add(int(input("Enter a number: ")))

    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference:", set1 - set2)
    print("Symmetric difference:", set1 ^ set2)


def task14():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for _ in range(n):
        numbers.append(int(input("Enter a number: ")))

    unique_numbers = set(numbers)
    repeated_numbers = set()

    for number in numbers:
        if numbers.count(number) > 1:
            repeated_numbers.add(number)

    print("Number of different elements:", len(unique_numbers))
    print("Repeated numbers:", repeated_numbers)


def task15():
    n = int(input("Enter a positive integer: "))
    result = {}

    for number in range(1, n + 1):
        result[number] = (number ** 2, number ** 3)

    print(result)


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    # task10()
    # task11()
    # task12()
    # task13()
    # task14()
    # task15()
    pass


if __name__ == "__main__":
    main()
