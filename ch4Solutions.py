import pexpect
import sys
import os
import random
import math
import time
import helpers

from subprocess import Popen, PIPE, STDOUT

# text color constants
R = '\033[0;31m'  # red
BR = '\033[1;31m'  # bold red
G = '\033[0;32m'  # green
BG = '\033[1;32m'  # bold green
Y = '\033[0;33m'  # yellow
BY = '\033[1;33m'  # bold yellow
B = '\033[0;34m'  # blue
BB = '\033[1;34m'  # bold blue
P = '\033[0;35m'  # purple
BP = '\033[1;35m'  # bold purple
A = '\033[0;36m'  # aqua
BA = '\033[1;36m'  # bold aqua
X = '\033[0m'  # reset


def ch4_1(file):
    def genCoefficients():
        while True:
            a = random.randint(-5, 5)
            b = random.randint(-5, 5)
            c = random.randint(-5, 5)
            discriminant = b**2 - 4 * a * c
            if 2 * a == 0:
                continue
            else:
                return a, b, c, discriminant

    # test case 1: d < 0, no roots
    a, b, c, discriminant = genCoefficients()
    while discriminant >= 0:
        a, b, c, discriminant = genCoefficients()
    key = "no real roots"
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{a}, {b}, {c}")
    helpers.assess(child, "ch4_1.py case 1", key)

    # test case 2: d == 0, one root
    while discriminant != 0:
        a, b, c, discriminant = genCoefficients()
    singleRoot = -b / (2 * a)
    key = f"The root is {singleRoot:.2f}"
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{a}, {b}, {c}")
    helpers.assess(child, "ch4_1.py case 2", key)

    # test case 3: d > 0, two roots
    while discriminant <= 0:
        a, b, c, discriminant = genCoefficients()
    pRoot = (-b + math.sqrt(discriminant)) / (2 * a)
    nRoot = (-b - math.sqrt(discriminant)) / (2 * a)
    key = f"The roots are {pRoot:.2f} and {nRoot:.2f}"
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{a}, {b}, {c}")
    helpers.assess(child, "ch4_1.py case 3", key)


def ch4_2(file):
  def getOperands():
    operands = []
    for i in message:
      if i.isdigit():
          operands.append(int(i))
    total = sum(operands) 
    return operands, total

  child = pexpect.spawnu(f'python3 {file}')
  message = child.read_nonblocking(size=20, timeout=-1).strip()
  operands, total = getOperands()

  child.sendline(str(total))
  key = f'{operands[0]} + {operands[1]} + {operands[2]} = {total} is True'
  helpers.assess(child, 'ch4_2.py: case 1', key, f'{message} ')
  
  child = pexpect.spawnu(f'python3 {file}')
  message = child.read_nonblocking(size=20, timeout=-1).strip()
  operands, total = getOperands()
  total += random.randint(1, 5)
  child.sendline(str(total))
  key = f'{operands[0]} + {operands[1]} + {operands[2]} = {total} is False'
  helpers.assess(child, 'ch4_2.py: case 2', key, f'{message} ')


def ch4_3(file):
    def genCoefficients():
        data = []
        for i in range(6):
            data.append(round(random.randint(-15, 15), 1))
        return data

    # case 1
    data = genCoefficients()
    while data[0] * data[3] - data[1] * data[2] == 0:
        data = genCoefficients()

    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(
        f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}")
    x = (data[4] * data[3] - data[1] * data[5]) / (data[0] * data[3] -
                                                   data[1] * data[2])
    y = (data[0] * data[5] - data[4] * data[2]) / (data[0] * data[3] -
                                                   data[1] * data[2])
    key = f"x is {x:.1f} and y is {y:.1f}"
    helpers.assess(child, "ch4_3.py: case 1", key)

    # case 2
    data = genCoefficients()
    while data[0] * data[3] - data[1] * data[2] != 0:
        data = genCoefficients()

    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(
        f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}")
    key = "The equation has no solution"
    helpers.assess(child, "ch4_3.py: case 2", key)


def ch4_4(file):
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=18, timeout=-1)
    operands = helpers.getOperands(inputOutput)
    child.sendline(str(sum(operands)))
    key = f'{operands[0]} + {operands[1]} + {operands[2]} = {sum(operands)} is True'
    helpers.assess(child, f'{file}: case 2', key, inputOutput)

    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=18, timeout=-1).strip()
    operands = helpers.getOperands(inputOutput)
    total = sum(operands) + random.randint(-5, 5)
    child.sendline(str(total))
    key = f'{operands[0]} + {operands[1]} + {operands[2]} = {total} is False'
    helpers.assess(child, f'{file}: case 2', key, inputOutput)


def ch4_5(file):
    for i in range(3):
        days = [
            'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday'
        ]
        day = random.randint(0, 6)
        f = random.randint(2, 6)
        future = (day + f) % 7
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(str(day))
        child.sendline(str(f))
        key = f'Today is {days[day]} and the future day is {days[future]}'
        helpers.assess(child, f'ch4_5.py try {i + 1}', key)


def ch4_6(file):
    weight = random.randint(150, 230)
    feet = random.randint(4, 6)
    inch = random.randint(0, 11)

    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(weight))
    child.sendline(str(feet))
    child.sendline(str(inch))

    height = (feet * 12) + inch

    KILOGRAMS_PER_POUND = 0.45359237  # Constant
    METERS_PER_INCH = 0.0254  # Constant

    # Compute BMI
    weightInKilograms = weight * KILOGRAMS_PER_POUND
    heightInMeters = height * METERS_PER_INCH
    bmi = weightInKilograms / (heightInMeters * heightInMeters)

    # Display result
    s1 = f'BMI is {bmi:.2f}'
    if bmi < 18.5:
        s2 = 'Underweight'
    elif bmi < 25:
        s2 = 'Normal'
    elif bmi < 30:
        s2 = 'Overweight'
    else:
        s2 = 'Obese'
    key = f'{s1}\r\n{s2}'
    helpers.assess(child, f'ch4_6.py', key)


def ch4_7(file):
    def getMoney(amount):
        remainingAmount = int(amount * 100)
        oneDollars = remainingAmount // 100
        remainingAmount = remainingAmount % 100
        quarters = remainingAmount // 25
        remainingAmount = remainingAmount % 25
        dimes = remainingAmount // 10
        remainingAmount = remainingAmount % 10
        nickels = remainingAmount // 5
        pennies = remainingAmount % 5
        return [oneDollars, quarters, dimes, nickels, pennies]

    def getResult(amount, money):
        result = f'Your amount ${amount} consists of\r\n'
        if money[0] >= 1:
            if money[0] == 1:
                result += f'{money[0]} dollar\r\n'
            else:
                result += f'{money[0]} dollars\r\n'
        if money[1] >= 1:
            if money[1] == 1:
                result += f'{money[1]} quarter\r\n'
            else:
                result += f'{money[1]} quarters\r\n'
        if money[2] >= 1:
            if money[2] == 1:
                result += f'{money[2]} dime\r\n'
            else:
                result += f'{money[2]} dimes\r\n'
        if money[3] >= 1:
            if money[3] == 1:
                result += f'{money[3]} nickel\r\n'
            else:
                result += f'{money[3]} nickels\r\n'
        if money[4] >= 1:
            if money[4] == 1:
                result += f'{money[4]} penny\r\n'
            else:
                result += f'{money[4]} pennies\r\n'
        return result

    amount = [0.13, 1.41, 4.69]
    # amount = round(random.uniform(0, 6), 2)

    for i in range(3):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(str(amount[i]))
        money = getMoney(amount[i])
        key = getResult(amount[i], money)
        helpers.assess(child, f'ch4_7.py case {i + 2}', key)


def ch4_8(file):

    data = [[-8, -5, -2], [8, 9, 7], [15, 13, 14]]
    for i in range(3):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(f'{data[i][0]}, {data[i][1]}, {data[i][2]}')
        greatest = max(data[i])
        lowest = min(data[i])
        for j in range(3):
            if data[i][j] != greatest and data[i][j] != lowest:
                middle = data[i][j]
        key = f'max: {greatest} middle: {middle} min: {lowest}'
        helpers.assess(child, f'ch4_8.py case {i + 1}', key)


def ch4_9(file):
    def getData():
        weight1 = random.randint(25, 100)
        price1 = round(random.uniform(30, 10), 2)
        weight2 = random.randint(25, 100)
        price2 = round(random.uniform(30, 10), 2)
        return price1, weight1, price2, weight2

    # case 1 Package 1 has better price
    child = pexpect.spawnu(f'python3 {file}')
    while True:
        price1, weight1, price2, weight2 = getData()
        if price1 / weight1 < price2 / weight2:
            break
    child.sendline(f'{weight1}, {price1}')
    child.sendline(f'{weight2}, {price2}')
    key = f'Package 1: ${price1/weight1:.2f}\r\nPackage 2: ${price2/weight2:.2f}\r\nPackage 1 has a better price.'
    helpers.assess(child, f'ch4_9.py Case 1', key)

    # case 2 Package  has better price
    child = pexpect.spawnu(f'python3 {file}')
    while True:
        price1, weight1, price2, weight2 = getData()
        if price1 / weight1 > price2 / weight2:
            break
    child.sendline(f'{weight1}, {price1}')
    child.sendline(f'{weight2}, {price2}')
    key = f'Package 1: ${price1/weight1:.2f}\r\nPackage 2: ${price2/weight2:.2f}\r\nPackage 2 has a better price.'
    helpers.assess(child, f'ch4_9.py Case 2', key)

    # case 3 packages are same price
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f'{1}, {1}')
    child.sendline(f'{1}, {1}')
    key = f'Package 1: ${1:.2f}\r\nPackage 2: ${1:.2f}\r\nThey are the same price.'
    helpers.assess(child, f'ch4_9.py Case 3', key)


def ch4_10(file):
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=15, timeout=-1)
    operands = helpers.getOperands(inputOutput)
    child.sendline(str(operands[0] * operands[1]))
    key = 'correct :)'
    helpers.assess(child, f'ch4_10.py Case 1', key, inputOutput)

    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=15, timeout=-1)
    operands = helpers.getOperands(inputOutput)
    total = operands[0] * operands[1] + random.randint(1, 9)
    child.sendline(str(total))
    key = 'incorrect :('
    helpers.assess(child, f'ch4_10.py Case 2', key, inputOutput)


def ch4_12(file):
    number = random.randint(-1000, 1000)
    child = pexpect.spawnu(f'python3 {file}')
    while not (number % 5 == 0 and number % 6 == 0):
        number = random.randint(-1000, 1000)
    child.sendline(str(number))
    key = f'{number} is divisible by 5 and 6'
    helpers.assess(child, 'ch4_12.py case 1', key)

    child = pexpect.spawnu(f'python3 {file}')
    while not (number % 5 == 0 and number % 6 != 0):
        number = random.randint(-1000, 1000)
    child.sendline(str(number))
    key = f'{number} is divisible by 5'
    helpers.assess(child, 'ch4_12.py case 2', key)

    child = pexpect.spawnu(f'python3 {file}')
    while not (number % 5 != 0 and number % 6 == 0):
        number = random.randint(-1000, 1000)
    child.sendline(str(number))
    key = f'{number} is divisible by 6'
    helpers.assess(child, 'ch4_12.py case 3', key)

    child = pexpect.spawnu(f'python3 {file}')
    while not (number % 5 != 0 and number % 6 != 0):
        number = random.randint(-1000, 1000)
    child.sendline(str(number))
    key = f'{number} is not divisible by 5 or 6'
    helpers.assess(child, 'ch4_12.py case 4', key)

# solutions below here need update to assess function

def ch4_16(file):
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=1, timeout=-1).strip()
    if 65 <= ord(inputOutput) <= 90:
        print(f'{G}:) ch4_16.py == passed!{X}')
    else:
        print(f'{R}:( ch4_16.py failed{X}')


def ch4_17(file):
    def testChild(player, file):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(str(player))
        child.expect('computer picked .*', timeout=-1)
        output = (child.after).split('\r\n')
        # Extract computer value
        computer = helpers.getOperands(output[0])[0]
        # Extract user submitted output
        computerOutput = output[1]
        child.terminate
        return computer, computerOutput

    def checkGame(player, computer):
        if computer == player:
            return 'draw'
        # player is rock
        elif player == 0:
            if computer == 2:
                return 'player wins - rock beats scissor'
            else:
                return 'computer wins - paper beats rock'
        # player is paper
        elif player == 1:
            if computer == 0:
                return 'player wins - paper beats rock'
            else:
                return 'computer wins - scissor beats paper'
        else:
            if player == 2:
                if computer == 1:
                    return 'player wins - scissor beats paper'
                else:
                    return 'computer wins - rock beats scissor'

    def testKey(computerOutput, key, case):
        if computerOutput == key:
            print(f'{BY}Output is correct!')
            print(f'\n{G}{key}')
            print(f'\n{BY}:) ch4_17.py case {case} == passed!{X}')
        else:
            print(f'{BY}Expected output of:\n\n{R}{key}')
            print(f'\n{BY}Actual output was:\n\n{R}{computerOutput}')
            print(f'{BY}:( ch4_17.py test case {case} == failed{X}')

    case = 0
    for player in range(3):
        for computerValue in range(3):
            case += 1
            while True:
                computer, computerOutput = testChild(player, file)
                if computer == computerValue:
                    break
            key = checkGame(player, computer)
            testKey(computerOutput, key, case)


def ch4_24(file):
    def createDeck():
        """generates a deck of cards"""
        cards = []
        for number in range(2, 11):
            cards.extend([
                str(number) + suite
                for suite in ['\u2664', '\u2661', '\u2662', '\u2667']
            ])
        for face in 'JQKA':
            cards.extend([
                face + suite
                for suite in ['\u2664', '\u2661', '\u2662', '\u2667']
            ])
        random.shuffle(cards)
        return cards

    cards = createDeck()
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=5, timeout=-1).strip()
    
    if inputOutput in cards:
        print(f'{G}{inputOutput}{X}')
        print(f'{G}:) ch4_24.py == passed!{X}')
    else:
        print(f'{R}{inputOutput}{X}')
        print(f'{R}:( ch4_24.py failed{X}')
