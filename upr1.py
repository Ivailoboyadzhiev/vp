import math


def sales():
    number = float(input())
    procent1 = float(input())
    procent2 = float(input())

    finalnum = number * (1 - procent1 / 100)
    finalnum = finalnum * (1 - procent2 / 100)

    print(f"{finalnum:.2f}")


def taxiAvtobus():
    kmAvto = float(input())
    kmTaxi = float(input())
    priceAvto = float(input())
    priceTaxi = float(input())

    distance = kmAvto + kmTaxi
    total = kmAvto * priceAvto + kmTaxi * priceTaxi

    print(f"{distance:.2f}")
    print(f"{total:.2f}")


def salary():
    hours = float(input())
    rate = float(input())
    bonus = float(input())
    tax = float(input())

    final = hours * rate
    final = final * (1 + bonus / 100)
    final = final * (1 - tax / 100)

    print(f"{final:.2f}")


def restaurant():
    food = float(input())
    drinks = float(input())
    tax = float(input())
    people = int(input())

    total = (food + drinks) * (1 + tax / 100)
    per_person = total / people

    print(f"{total:.2f}")
    print(f"{per_person:.2f}")


def para():
    l = float(input())
    w = float(input())
    h = float(input())

    volume = l * w * h
    surface = 2 * (l * w + l * h + w * h)

    print(f"{volume:.3f}")
    print(f"{surface:.3f}")


def drinks():
    drink1 = float(input())
    price1 = float(input())
    drink2 = float(input())
    price2 = float(input())

    total_drinks = drink1 + drink2
    average_price = (
        drink1 * price1 + drink2 * price2
    ) / total_drinks

    print(f"{total_drinks:.2f}")
    print(f"{average_price:.2f}")


def travel():
    km = float(input())
    speed = float(input())
    rest = float(input())

    time = km / speed * 60 + rest

    print(f"{time:.2f}")


def painting():
    length = float(input())
    width = float(input())
    height = float(input())
    openings = float(input())
    coverage = float(input())
    price_per_liter = float(input())

    wall_area = 2 * (length + width) * height
    paint_area = wall_area - openings
    liters = paint_area / coverage
    cost = liters * price_per_liter

    print(f"{liters:.2f}")
    print(f"{cost:.2f}")


def weighted_grade():
    grade1 = float(input())
    weight1 = float(input())
    grade2 = float(input())
    weight2 = float(input())
    grade3 = float(input())
    weight3 = float(input())

    result = (
        grade1 * weight1
        + grade2 * weight2
        + grade3 * weight3
    ) / 100

    print(f"{result:.2f}")


def bank():
    money = float(input())
    proc = float(input())
    years = float(input())

    interest = money * proc / 100 * years
    total = money + interest

    print(f"{interest:.2f}")
    print(f"{total:.2f}")


def sec():
    s = int(input())

    hours = s // 3600
    minutes = (s % 3600) // 60
    seconds = s % 60

    print(hours)
    print(minutes)
    print(seconds)


def floor():
    a = float(input())
    b = float(input())
    tile = float(input())
    reserve = float(input())
    price = float(input())

    floor_area = a * b
    needed_tiles = math.ceil(
        floor_area * (1 + reserve / 100) / tile
    )
    total_price = needed_tiles * price

    print(needed_tiles)
    print(f"{total_price:.2f}")


def tok():
    power = float(input())
    hours = float(input())
    days = float(input())
    price = float(input())

    consumption = power / 1000 * hours * days
    cost = consumption * price

    print(f"{consumption:.2f}")
    print(f"{cost:.2f}")


def distance():
    d1 = float(input())
    s1 = float(input())
    d2 = float(input())
    s2 = float(input())

    total_distance = d1 + d2
    total_time = d1 / s1 + d2 / s2
    avg = total_distance / total_time

    print(f"{total_time:.2f}")
    print(f"{avg:.2f}")


def sale2():
    n = int(input())
    price = float(input())
    delivery = float(input())
    expenses = float(input())

    revenue = n * price
    total_expenses = n * delivery + expenses
    profit = revenue - total_expenses

    print(f"{revenue:.2f}")
    print(f"{total_expenses:.2f}")
    print(f"{profit:.2f}")



#sales()
# taxiAvtobus()
salary()
# restaurant()
# para()
# drinks()
# travel()
# painting()
# weighted_grade()
# bank()
# sec()
# floor()
# tok()
# distance()
# sale2()