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


def ch3_1(file):
    child = pexpect.spawnu(f'python3 {file}')
    s = round(random.uniform(15, 1), 1)
    child.sendline(str(s))
    side = 2 * s * math.sin((math.pi / 5))
    area = (3 * math.sqrt(3) / 2) * math.pow(side, 2)
    key = f"The area of the pentagon is {area:.2f}"
    helpers.assess(child, "ch3_1.py", key)
      

def ch3_2(file):
    child = pexpect.spawnu(f'python3 {file}')
    data = []
    for i in range(4):
        data.append(round(random.uniform(100, -100), 1))
   
    child.sendline(f"{data[0]}, {data[1]}")
    child.sendline(f"{data[2]}, {data[3]}")
    
    for i, each in enumerate(data):
        data[i] = math.radians(data[i])
  
    d = 6371.01 * math.acos(math.sin(data[0]) * math.sin(data[2]) + math.cos(data[0]) * math.cos(data[2]) * math.cos(data[1] - data[3]))
    d = 6371.01 * math.acos(math.sin(math.radians(data[0])) * math.sin(math.radians(data[2]))) + math.cos(math.radians(data[0])) * math.cos(math.radians(data[2])) * mtah.cos(math.radians(data[1] - data[3]))


    key = f"The distance between two points is {d:.4f} km"
    helpers.assess(child, "ch3_2.py", key)
    
    
def ch3_4(file):
    child = pexpect.spawnu(f'python3 {file}')
    s = round(random.uniform(15, 1), 1)

    child.sendline(str(s))
    area = (5 * s**2) / (4 * math.tan((math.pi / 5)))

    key = f"The area of a pentagon is {area:.2f}"
    helpers.assess(child, "ch3_4.py", key)
    

def ch3_5(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = round(random.uniform(15, 1), 1)
    s = round(random.uniform(15, 1), 1)

    child.sendline(str(n))
    child.sendline(str(s))

    area = (n * s**2) / (4 * math.tan((math.pi / n)))

    key = f"The area of a pentagon is {area:.2f}"
    helpers.assess(child, "ch3_5.py", key)


def ch3_6(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(0, 127)
    child.sendline(str(n))
    key = f"The character is {chr(n)}"
    helpers.assess(child, "ch3_6.py", key)
            
            
def ch3_7(file):
    child = pexpect.spawnu(f'python3 {file}')
    child.expect(pexpect.EOF)
    if child.before.strip() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        # pass
        print(f"{BY}Output is correct!\n\n{G}{child.before}\n{BY}:) ch3_7.py == passed!{X}")
    # fail
    else:
        print(f"{BY}Expected output of:\n\n{R}{'a capital letter'}\n{BY}Actual output was:\n\n{R}{child.before}\n{BY}:( ch3_7.py == failed{X}")
            

def ch3_11(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(0, 9999)
    child.sendline(str(n))
    thousands = n // 1000
    remainder = n % 1000
    hundreds = remainder // 100
    remainder = n % 100
    tens = remainder // 10
    ones = remainder % 10
    key = f"{n} reversed is {ones}{tens}{hundreds}{thousands}"
    helpers.assess(child, "ch3_11.py", key)
