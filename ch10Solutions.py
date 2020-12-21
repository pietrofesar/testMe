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


def ch10_1(file):
    students = [random.randint(21, 97) for each in range(random.randint(4, 7))]
    
    best = max(students)
    
    answer_key = ''
    for i in range(len(students)):
        if students[i] >= best - 10:
            answer_key+= f'Student score is {students[i]} and the grade is A\r\n'
        elif students[i] >= best - 20:
            answer_key += f'Student score is {students[i]} and the grade is B\r\n'
        elif students[i] >= best - 30:
            answer_key += f'Student score is {students[i]} and the grade is C\r\n'
        elif students[i] >= best - 40:
            answer_key += f'Student score is {students[i]} and the grade is D\r\n'
        else:
            answer_key += f'Student score is {students[i]} and the grade is F\r\n'
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(' '.join(str(n) for n in students))
    helpers.assess(child, f'ch10_1.py', answer_key)


def ch10_2(file):
    integers = [random.randint(1, 99) for each in range(random.randint(4, 9))]
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(' '.join(str(n) for n in integers))
    integers.reverse()
    helpers.assess(child, f'ch10_2.py', str(integers))
    

def ch10_3(file):
    integers = [random.randint(1, 100) for each in range(random.randint(3, 6))]
    num = random.randint(1, 50)
    for each in range(random.randint(2, 4)):
        integers.append(num)
    num = random.randint(51, 100)
    for each in range(random.randint(2, 4)):
        integers.append(num)
    random.shuffle(integers)
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(' '.join(str(n) for n in integers))
    
    integers.sort()
    numbers = []
    counts = []
    answer_key = ''
    for i in range(len(integers)):
        if integers[i] not in numbers:
            numbers.append(integers[i])
            counts.append(integers.count(integers[i]))
    
    for i in range(len(counts)):
        if counts[i] > 1:
            answer_key += f'{numbers[i]} occurs {counts[i]} times\r\n'
        else:
            answer_key += f'{numbers[i]} occurs {counts[i]} time\r\n'
    
    helpers.assess(child, f'ch10_3.py', answer_key)
    
    
def ch10_4(file):
    
    def data_summary(scores):
        average = int(sum(scores) / len(scores))
        
        above_average = 0
        below_average = 0
        equal = 0
        
        for score in scores:
            if score > average:
                above_average += 1
            elif score < average:
                below_average += 1
            else:
                equal += 1
        
        answer_key = f'average is {average}\r\n'
        if above_average > 0:
            answer_key += f'{above_average} above average\r\n'
        if below_average > 0:
            answer_key += f'{below_average} below average\r\n'
        if equal > 0:
            answer_key += f'{equal} equal\r\n'
        return answer_key
    
    reg_scores = [random.randint(30, 100) for each in range(random.randint(6, 10))]
    child = pexpect.spawnu(f'python3 {file}')
    answer_key = data_summary(reg_scores)
    child.sendline(' '.join(str(n) for n in reg_scores))
    helpers.assess(child, f'ch10_4.py Test 1', answer_key)
    
    equal_scores = [random.randint(75, 78) for each in range(10)]
    child = pexpect.spawnu(f'python3 {file}')
    answer_key = data_summary(equal_scores)
    child.sendline(' '.join(str(n) for n in equal_scores))
    helpers.assess(child, f'ch10_4.py Test 2', answer_key)
    

def ch10_5(file):
    numbers = [random.randint(0, 9) for each in range(5)]
    n = random.randint(0, 9)
    for i in range(3):
        numbers.append(n)
    n = random.randint(0, 9)
    for i in range(2):
        numbers.append(n)
    random.shuffle(numbers)
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(' '.join(str(n) for n in numbers))
    numbers.sort()
    aggregator = []
    for each in numbers:
        if each not in aggregator:
            aggregator.append(each)
    answer_key = f'the distinct numbers are {" ".join(str(each ) for each in aggregator)}\r\n'
    helpers.assess(child, f'ch10_5.py', answer_key)


def ch10_6(file):
    print('under construction')


def ch10_7(file):
    print('under construction')


def ch10_8(file):
    print('under construction')


def ch10_9(file):
    print('under construction')


def ch10_10(file):
    print('under construction')


def ch10_11(file):
    print('under construction')

