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


def ch2_1(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = '24 Celsius is 75.2 Fahrenheit'
    child.sendline('24')
    # check the correctness of the submission
    helpers.assess(child, "ch2_1.py", key)
    

def ch2_2(file):
    child = pexpect.spawnu(f'python3 {file}')
    PI = 3.14159
    radius = round(random.uniform(8, 1), 1)
    length = round(random.uniform(15, 1), 1)
    child.sendline('{}, {}'.format(radius, length))
    key = 'The area is {}\r\nThe volume is {}'.format(PI * radius**2, PI * radius**2 * length)
    helpers.assess(child, "ch2_2.py", key)
    
 
def ch2_3(file):
    child = pexpect.spawnu(f'python3 {file}')
    feet = round(random.uniform(30, 1), 2)
    child.sendline(str(feet))
    key = '{} feet is {} meters'.format(feet, feet * .305)
    helpers.assess(child, "ch2_3.py", key)
    
            
def ch2_4(file):
    child = pexpect.spawnu(f'python3 {file}')
    pounds = round(random.uniform(200, 1), 2)
    child.sendline(str(pounds))
    key = '{} pounds is {} kilograms'.format(pounds, pounds * .454)
    helpers.assess(child, "ch2_4.py", key)


def ch2_5(file):
    child = pexpect.spawnu(f'python3 {file}')
    subtotal = round(random.uniform(80, 1), 2)
    rate = round(random.uniform(20, 10))
    child.sendline('{}, {}'.format(subtotal, rate))
    key = 'The gratuity is {0:.2f} and the total is {1:.2f}'.format(subtotal * (rate/100), subtotal * (1 + (rate/100)))
    helpers.assess(child, "ch2_5.py", key)
            
            
def ch2_6(file):
    child = pexpect.spawnu(f'python3 {file}')
    num = random.randint(0, 1000)
    child.sendline(str(num))
    key = 'The sum of the digits is {}'.format((num % 10) + ((num // 10) % 10) + ((num // 100) % 10))
    # check the correctness of the submission
    helpers.assess(child, "ch2_6.py", key)
            

def ch2_7(file):
    child = pexpect.spawnu(f'python3 {file}')
    minutes = random.randint(0, 1000000000)
    child.sendline(str(minutes))
    key = '{} minutes is approximately {} years and {} days'.format(minutes, minutes // 525600, (minutes % 525600) // 1440)
    helpers.assess(child, "ch2_7.py", key)


def ch2_8(file):
    child = pexpect.spawnu(f'python3 {file}')
    data = [round(random.uniform(100,20), 1), round(random.uniform(20,1), 1), round(random.uniform(20,1), 1)]
    for each in data:
        child.sendline(str(each))
    key = 'The energy needed is {:.1f}'.format(data[0] * (data[2] - data[1]) * 4184)
    helpers.assess(child, "ch2_8.py", key)
            
            
def ch2_9(file):
    child = pexpect.spawnu(f'python3 {file}')
    t = round(random.uniform(41, -58), 1)
    v = random.randint(2, 80)
    child.sendline(str(t))
    child.sendline(str(v))
    key = 'The wind chill index is {:.5f}'.format(35.74 + 0.621 * t - 35.75 * v**0.16 + 0.4275 * t * v**0.16)
    helpers.assess(child, "ch2_9.py", key)


def ch2_10(file):
    child = pexpect.spawnu(f'python3 {file}')
    v = round(random.uniform(210, 80), 1)
    a = round(random.uniform(10, 3), 1)
    child.sendline('{}, {}'.format(v, a))
    key = 'The minimum runway length for this airplane is {:.3f} meters'.format((v**2)/(2*a))
    helpers.assess(child, "ch2_10.py", key)
    

def ch2_13(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(1111, 9999)
    F = 1000
    child.sendline(str(n))
    data =[]
    data.append(n // 1000)
    n %= 1000
    data.append(n // 100)
    n %= 100
    data.append(n // 10)
    n%= 10
    data.append(n)
    key = '{}\r\n{}\r\n{}\r\n{}'.format(data[0], data[1], data[2], data[3])
    helpers.assess(child, "ch2_13.py", key)
    
    
def ch2_14(file):
    child = pexpect.spawnu(f'python3 {file}')
    data = []
    for each in range(6):
        data.append(round(random.uniform(10,-10), 1))
    child.sendline('{}, {}, {}, {}, {}, {}'.format(data[0], data[1], data[2], data[3], data[4], data[5]))
    key = '{}\r\n{}\r\n{}\r\n{}'.format(data[0], data[1], data[2], data[3])
    s1 = ((data[0] - data[2])**2 + (data[1] - data[3])**2)**.5
    s2 = ((data[2] - data[4])**2 + (data[3] - data[5])**2)**.5
    s3 = ((data[4] - data[0])**2 + (data[5] - data[1])**2)**.5
    s = (s1 + s2 + s3) / 2
    area = (s * (s - s1) * (s - s2) * (s - s3))**.5
    key = 'The area of the triangle is {:.1f}'.format(area)
    helpers.assess(child, "ch2_14.py", key)
            

def ch2_15(file):
    child = pexpect.spawnu(f'python3 {file}')
    s = round(random.uniform(15, 5), 1)
    child.sendline(str(s))
    key = 'The area of the hexagon is {0:.2f}'.format(((3*3**.5) / 2) * s**2)
    helpers.assess(child, "ch2_15.py", key)


def ch2_18(file):
    child = pexpect.spawnu(f'python3 {file}')
    offset = random.randint(-10, -3)
    child.sendline(str(offset))

    currentTime = time.time()# get current time
    # obtain the total seconds since midnight Jan 1, 1970 
    totalSeconds = int(currentTime)
    # get the current second
    currentSecond = totalSeconds % 60
    # get the total minutes
    totalMinutes = totalSeconds // 60
    # compute the current minute in the hour
    currentMinute = totalMinutes % 60
    # obtain the total hours
    totalHours = totalMinutes // 60
    # compute the current hour
    currentHour = totalHours % 24
   
    key = f"Current time is {currentHour + offset}:{currentMinute}:{currentSecond}"
    
    helpers.assess(child, 'ch2_18.py', key)


def ch2_19(file):
    investmentAmount = random.randint(1200, 50000)
    annualInterestRate = round(random.uniform(1, 7), 2)
    years = random.randint(1, 10)

    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(investmentAmount))
    child.sendline(str(annualInterestRate))
    child.sendline(str(years))

    annualInterestRate /= 100
    monthlyInterestRate = annualInterestRate / 12
    numberOfMonths = years * 12
    futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths
    key = f"Accumulated value is ${futureInvestmentAmount:.2f}"
    helpers.assess(child, 'ch2_19.py', key)


def ch2_20(file):
    balance = random.randint(1200, 50000)
    rate = round(random.uniform(1, 7), 2)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{balance}, {rate}")
    interest = balance * (rate / 1200)
    key = f"The interest is ${interest:.2f}"
    helpers.assess(child, 'ch2_20.py', key)


def ch2_21(file):
    
    principal = random.randint(100, 1000)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(principal))
    m1 = principal * (1 + .00417)
    for i in range(5):
        m1 = (principal + m1) * (1 + .00417)
    key = f"After the sixth month, the account value is ${m1:.2f}"
    helpers.assess(child, 'ch2_21.py', key)