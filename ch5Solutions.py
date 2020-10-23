import pexpect
import sys
import os
import random
import math
import time
import helpers

from subprocess import Popen, PIPE, STDOUT


# text color constants
R = '\033[0;31m'    # red
BR = '\033[1;31m'   # bold red
G = '\033[0;32m'    # green
BG = '\033[1;32m'   # bold green
Y = '\033[0;33m'    # yellow
BY = '\033[1;33m'   # bold yellow
B = '\033[0;34m'    # blue
BB = '\033[1;34m'   # bold blue
P = '\033[0;35m'    # purple
BP = '\033[1;35m'   # bold purple
A = '\033[0;36m'    # aqua
BA = '\033[1;36m'   # bold aqua
X = '\033[0m'       # reset


def ch5_1(file):
    # generate integers for test case 1
    integers = []
    for i in range(random.randint(4, 11)):
        sign = random.randint(0, 1)
        if sign == 0:
            integers.append(random.randint(1, 20))
        else:
            integers.append(random.randint(-20, -1))
    integers.append(0)
    
    # summarize the data for case 1
    tally, positives, negatives, total = 0, 0, 0, 0
    for i in integers:
        if i != 0:
            tally += 1
            if i > 0:
                positives += 1
            else:
                negatives +=1
            total += i
    average = total / tally
    
    # generate the output for test case 1
    key = f'The number of positives is {positives}\r\n'
    key += f'The number of negatives is {negatives}\r\n'
    key += f'The total is {total}\r\n'
    key += f'The average is {average:.2f}\r\n'
    child = pexpect.spawnu(f'python3 {file}')
    # send the input
    for i in integers:
        child.sendline(str(i))
    # test the output
    helpers.assess(child, f'ch5_1.py Case 1', key)
    # test case 2
    child = pexpect.spawnu(f'python3 {file}')
    # send the input
    child.sendline(str(0))
    # correct output
    key = 'You didn\'t enter any number\r\n'
    # test the output
    helpers.assess(child, f'ch5_1.py Case 2', key)


def ch5_2(file):
    DELAY = .1
    CORRECT_LENGTH = 12
    WRONG_LENGTH = 26
    print(f'{BY}!!!+++Time may be off and cause a failure+++!!!{X}')
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    start = time.time()
    for i in range(10):
        # capture child out
        expression = child.read_nonblocking(size=18, timeout=-1).strip()
        # extract numbers from child out
        numbers = helpers.getOperands(expression)
        # determines if the response is 1 or 2 characters
        if len(str(sum(numbers))) == 1:
            size = 1
        else:
            size = 2
        # prints the question
        print(f'{P}{expression} {B}{str(sum(numbers))}{X}')
        # sends the correct response
        child.sendline(str(sum(numbers)))
        # delays so that all text is present before flushing
        time.sleep(DELAY)
        # flushes the inbetween text
        child.read_nonblocking(size=CORRECT_LENGTH + size, timeout=-1)

    duration = time.time() - start -.1
    key = f'You got 10 out of 10 correct\r\nTest time is {duration:.1f} seconds'
    helpers.assess(child, f'ch5_2.py Case 1', key)
    child.terminate()
    
    print(f'{BY}!!!+++Time may be off and cause a failure+++!!!{X}')
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    start = time.time()
    for i in range(10):
        # capture child out
        expression = child.read_nonblocking(size=18, timeout=-1).strip()
        # extract numbers from child out
        numbers = helpers.getOperands(expression)
        # determines if the response is 1 or 2 characters
        if len(str(sum(numbers))) == 1:
            size = 1
        else:
            size = 2
        print(f'{P}{expression} {B}{str(sum(numbers))}{X}')
        # sends the correct response
        child.sendline(str(sum(numbers) + 1))
        # delays so that all text is present before flushing
        time.sleep(DELAY)
        # flushes the inbetween text
        child.read_nonblocking(size=WRONG_LENGTH + size, timeout=-1)

    duration = time.time() - start
    key = f'You got 0 out of 10 correct\r\nTest time is {duration:.1f} seconds'
    helpers.assess(child, f'ch5_2.py Case 2', key)


def ch5_3(file):
    key = f'{"Kilograms":13}{"Pounds":>6}\r\n'
    kilograms = 1
    while kilograms <= 199:
        pounds = kilograms * 2.2
        key += f'{kilograms:<13}{pounds:>6.1f}\r\n'
        kilograms += 2
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    helpers.assess(child, f'ch5_3.py', key)
    
    
def ch5_4(file):
    key = f'{"Miles":7}Kilometers\r\n'
    miles = 1
    while miles <= 10:
        kilometers = miles * 1.609
        key += f'{miles:<7}{kilometers:.3f}\r\n'
        miles += 1
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    helpers.assess(child, f'ch5_4.py', key)


def ch5_5(file):
    key = f'{"Kilograms":<11}{"Pounds":<7}| {"Pounds":<7}{"Kilograms":<9}\r\n'
    kilograms1 = 1
    pounds2 = 20
    while kilograms1 <= 199:
        pounds1 = kilograms1 * 2.2 
        kilograms2 = pounds2 * .4536
        key += f'{kilograms1:<11}{pounds1:<7.1f}| {pounds2:<7}{kilograms2:<9.2f}\r\n'
        kilograms1 += 2
        pounds2 += 5
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    helpers.assess(child, f'ch5_5.py', key)


def ch5_6(file):
    key = f'{"Miles":<7}{"Kilometers":<11}| {"Kilometers":<11}{"Miles":<6}\r\n'
    miles1 = 1
    kilometers2 = 20
    while miles1 <= 10:
        kilometers1 = miles1 * 1.609 
        miles2 = kilometers2 * .621
        key += f'{miles1:<7}{kilometers1:<11.3f}| {kilometers2:<11}{miles2:<6.3f}\r\n'
        miles1 += 1
        kilometers2 += 5
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    helpers.assess(child, f'ch5_6.py', key)


def ch5_7(file):
    key = f'{"Degree":<8}{"Sin":<10}{"Cos":<6}\r\n'
    degree = 0
    while degree <= 360:
        sin = math.sin(math.radians(degree))
        cos = math.cos(math.radians(degree))
        key += f'{degree:<8}{sin:<10.4f}{cos:<6.4f}\r\n'
        degree += 10
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    helpers.assess(child, f'ch5_7.py', key)


def ch5_8(file):
    key = f'{"Number":<8}{"Square Root":<11}\r\n'
    number = 0
    while number <= 20:
        root = math.sqrt(number)
        key += f'{number:<8}{root:<11.4f}\r\n'
        number += 1
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    helpers.assess(child, f'ch5_8.py', key)


def ch5_11(file):
    
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    NUM_OF_STUDENTS = random.randint(2, 9)
    child.sendline(str(NUM_OF_STUDENTS))
    grades = []
    for i in range(NUM_OF_STUDENTS):
        temp = random.randint(50, 100)
        child.sendline(str(temp))
        grades.append(temp)
    highScore, runnerUp = 0, 0
    for i in grades:
        if i > highScore:
            runnerUp = highScore
            highScore = i
        else:
            if i > runnerUp:
                runnerUp = i
    key = f'High Score: {highScore} Second Highest Score: {runnerUp}'
    helpers.assess(child, f'ch5_11.py Case 1', key)
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline('0')
    key = '0 was entered for the number of students'
    helpers.assess(child, f'ch5_11.py Case 2', key)
    

def ch5_12(file):
    
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    i = 100
    while i <= 1000:
        count = 0
        line = ''
        while count < 10 and i <= 1000:
            if i % 5 == 0 and i % 6 == 0:
                line += str(i)
                count += 1
                if count != 10:
                    line += ' '
            i += 1
        key += f'{line}\r\n' 
    helpers.assess(child, f'ch5_12.py', key)
    
    
def ch5_13(file):
    
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    i = 100
    while i <= 200:
        count = 0
        key = ''
        line = ''
        while count < 10 and i <= 200:
            if i % 5 == 0 or i % 6 == 0 and not(i % 5 == 0 and i % 6 == 0):
                line += str(i)
                count += 1
                if count != 10:
                    line += ' '
            i += 1
        key += f'{line}\r\n' 
    helpers.assess(child, f'ch5_13.py', key)  
    
    
def ch5_14(file):
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    n = 0
    while n**2 < 12000:
        key += f'{n} is not the answer\r\n'
        n += 1
    key += f'{n} is the answer\r\n'
    helpers.assess(child, f'ch5_14.py', key)  
       

def ch5_15(file):
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    n = 1
    while n**3 < 12000:
        n += 1
    key += f'{n - 1}\r\n'
    helpers.assess(child, f'ch5_15.py', key)  


def ch5_17(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    for char in range(33, 127, 10):
        for each in range(10):
            key += f'{chr(char)} '
            char += 1
        key += '\r\n'
    helpers.assess(child, f'{file}', key)


def ch5_19(file):
    child = pexpect.spawnu(f'python3 {file}')
    height = random.randint(2, 9)
    child.sendline(str(height))
    spaces = height * 2 - 2
    key = ''
    for digit in range(1, height + 1):
        for space in range(spaces):
            key +=' '
        digitCopy = digit
        while digitCopy > 1:
            key += f'{digitCopy} '
            digitCopy -= 1
        while digitCopy <= digit:
            key += f'{digitCopy} '
            digitCopy += 1
        spaces -= 2
        key += '\r\n'
    helpers.assess(child, file, key)


def ch5_20A(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    for row in range(1, 7):
        for digit in range(row):
           key += f'{digit + 1} '
        key += '\r\n'
    helpers.assess(child, file, key)
   

def ch5_20B(file):
    child = pexpect.spawnu(f'python3 {file}')
    height = 6
    key = ''
    for row in range(1, 7):
        for digit in range(1, height + 1):
            key += f'{digit} '
        height -= 1
        key += '\r\n'
    helpers.assess(child, file, key)   


def ch5_20C(file):
    child = pexpect.spawnu(f'python3 {file}')
    key  = 'Pattern C\r\n'
    i, spaces = 1, 5
    for i in range(1, 7):
        for j in range(spaces * 2):
            key += ' '
        for j in range(i, 0, -1):
            key += str(j)
            key += ' '
        spaces -= 1
    helpers.assess(child, file, key)


def ch5_20D(file):
    child = pexpect.spawnu(f'python3 {file}')
    digits = 7
    key = 'Pattern D\r\n'
    for i in range(1, 7):
        for j in range(1, digits):
            key += str(j)
            key += ' '
        digits -= 1
    helpers.assess(child, file, key)


def ch5_21(file):
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    LINES = 8
    spaces = LINES * 4 - 4
    # loops for the number of rows
    for i in range(1, LINES + 1):
        output = ''
        # creates the spaces part of the row
        for j in range(spaces):
            output += ' '
        
        # creates the left digits decreasing part of a row
        power = 0
        for j in range(i):
            output += f'{str(2 ** power):>4}'
            power += 1
            
        
        # creates the right digits increasing part of a row
        power = i - 2
        for j in range(i - 1):
            output += f'{str(2 ** power):>4}'
            power -= 1
        key += f'{output}\r\n'
        
        # update counters
        spaces -= 4
    helpers.assess(child, f'ch5_21.py', key)
