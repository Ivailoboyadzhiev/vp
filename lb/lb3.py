def task1():
    n = int(input())
    max_num = int(input())

    for i in range(n - 1):
        num = int(input())
        if num > max_num:
            max_num = num

    print(max_num)


def task2():
    n = int(input())
    total = 0

    for i in range(n):
        num = int(input())
        total += num

    print(total)


def task3():
    n = int(input())

    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


def task4():
    n = int(input())
    is_prime = True

    if n < 2:
        is_prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")


def main():
    task1()
    # task2()
    # task3()
    # task4()

if __name__ == "__main__":
    main()
