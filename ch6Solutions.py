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


def ch6_2(file):
    testMePath, studentPath, studentModule = helpers.functionTester(file)
    print(testMePath, studentPath, studentModule)
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(0, 9999)
    
    child.sendline(str(n))
    total = 0
    while n > 10:
        total += n % 10
        n //= 10
    total += n
    key = f'The sum of the numbers is {total}'
    helpers.assess(child, "ch6_2.py", key)

def ch6_3(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(1111, 9999)
    
    child.sendline(str(n))
    thousands = n // 1000
    remainder = n % 1000
    hundreds = remainder // 100
    remainder = n % 100
    tens = remainder // 10
    ones = remainder % 10
    key = f'{n} reversed is {ones}{tens}{hundreds}{thousands}'
    helpers.assess(child, "ch6_3.py", key)


def ch6_4(file):
    # Test case 1 no palindrome
    child = pexpect.spawnu(f'python3 {file}')
    notPalindrome = ''
    for i in range(4):
        while True:
            digit = str(random.randint(0,9))
            if digit not in notPalindrome:
                break
        notPalindrome += digit
    child.sendline(notPalindrome)
    key = f'No {notPalindrome} is not a palindrome'
    helpers.assess(child, 'ch6_4.py Case 1', key)
    
    # Test case 2 palindrome
    child = pexpect.spawnu(f'python3 {file}')
    outers = str(random.randint(1, 9))
    inners = str(random.randint(1, 9))
    palindrome = outers + inners * 2 + outers
    child.sendline(palindrome)
    key = f'Yes {palindrome} is a palindrome'
    helpers.assess(child, 'ch6_4.py Case 2', key)
    
        
def ch6_5(file):
    child = pexpect.spawnu(f'python3 {file}')
    numbers = [random.randint(50, 300), random.randint(-100, 30), random.randint(-200, 200)]
    child.sendline(f'{numbers[0]}, {numbers[1]}, {numbers[2]}')
    numbers.sort()
    key = f'The sorted numbers are {numbers[0]}, {numbers[1]}, {numbers[2]}'
    helpers.assess(child, 'ch6_5.py', key)
    

def ch6_6(file):
    child = pexpect.spawnu(f'python3 {file}')
    rows = random.randint(0, 9)
    child.sendline(str(rows))
    spaces = rows - 1
    key = ''
    for row in range(rows):
        for spaces in range(spaces):
            key += '  '
        digits = row + 1
        for nums in range(row + 1):
            key += f'{digits} '
            digits -= 1
        key += '\r\n'
    helpers.assess(child, 'ch6_6.py', key)
            

def ch6_7(file):
   
    def futureValue(principle, annualRate, years):
        # Computes the return on an investment
        annualRate /= 100
        monthlyRate = annualRate / 12
        months = years * 12
        futureAmount = principle * (1 + monthlyRate) ** months
        return futureAmount


    def createTable(principle, annualRate, years):
        # Creates a printable table of the loan data
        table = f'{"Years":7}{"Future Value":12}\r\n'
        for year in range(1, years + 1):
            table += f'{year:<7}${futureValue(principle, annualRate, year):<12.2f}\r\n'
        return table
    
    
    child = pexpect.spawnu(f'python3 {file}')
    principle = random.randint(1000, 80000)
    rate = random.randint(3, 6)
    years = random.randint(4, 15)
    child.sendline(str(principle))
    child.sendline(str(rate))
    child.sendline(str(years))
    table = f'{createTable(principle, rate, years)}\r\n'
    
    helpers.assess(child, 'ch6_7.py', table)
    

def ch6_8(file):
    def celsiusToFahreneit(celsius):
        # Converts from Celsius to Fahrenheit
        return (9 / 5) * celsius + 32

    def fahrenheitToCelsius(fahrenheit):
        # Converts from Fahrenheit to Celsius
        return (5 / 9) * (fahrenheit - 32)
    
    child = pexpect.spawnu(f'python3 {file}')
    fahrenheit = 120.0
    table = ''
    table +=f'{"Celsius":<10}{"Fahrenheit":<12}|  {"Fahrenheit":<12}{"Celsius":<10}\r\n'
    for row in range(40, 30, -1):
        fTemp = celsiusToFahreneit(float(row))
        cTemp = fahrenheitToCelsius(fahrenheit)
        table += f'{float(row):<10.1f}{fTemp:<12.1f}|  {fahrenheit:<12.1f}{cTemp:<10.2f}\r\n'
        fahrenheit -= 10
    helpers.assess(child, 'ch6_8.py', table)
    
    
def ch6_9(file):
    def feetToMeter(foot):
        # Converts from feet to meters
        return 0.305 * foot


    def meterToFeet(meter):
        # Converts from meters to feet
        return meter / 0.305
        
    child = pexpect.spawnu(f'python3 {file}')
    meter = 20.0
    key = ''
    key += f'{"Feet":<10}{"Meters":<8}|  {"Meters":<10}{"Feet":<10}\r\n'
    for foot in range(1, 11):
        toMeter = feetToMeter(foot)
        toFoot = meterToFeet(meter)
        key += f'{float(foot):<10.1f}{toMeter:<8.3f}|  {meter:<10.1f}{toFoot:<10.3f}\r\n'
        meter += 6
    helpers.assess(child, 'ch6_9.py', key)


def ch6_10(file):
    def isPrime(number):
        # Check wether a number is prime
        divisor = 2
        while divisor <= number / 2:
            if number % divisor == 0:
                # If true, number is not prime
                return False
            divisor += 1
        return True


    maxLimit = random.randint(1000, 10000)
    primes = 0
    for n in range(1, maxLimit):
        if isPrime(n):
            primes += 1
    key = f'There are {primes} primes in {maxLimit}\r\n'
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(maxLimit))
    helpers.assess(child, 'ch6_10.py', key)


def ch6_12(file):
    
    def printChars(ch1, ch2, charsPerLine):
        start = ord(ch1)
        theString = ''
        while start <= ord(ch2):
            for i in range(charsPerLine):
                theString += chr(start)
                start += 1
                if start > ord(ch2):
                    break
            theString += '\r\n'
        return theString
    
    ch1 = chr(random.randint(33, 80))
    ch2 = chr(random.randint(81, 133))
    numberPerLine = random.randint(5, 15)
    key = printChars(ch1, ch2, numberPerLine)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(ch1)
    child.sendline(ch2)
    child.sendline(str(numberPerLine))
    helpers.assess(child, 'ch6_12.py', key)


def ch6_13(file):
   
    def sumSeries(i):
        # Computes the sum of a series
        total = 0
        for j in range(1, i + 1):
            total += j / (j + 1)
        return total
    maxLimit = random.randint(16, 30)
    key = f'{"i":10}{"m(i)":10}\r\n'
    for i in range(1, maxLimit + 1):
        total = sumSeries(i)
        key += f'{i:<10}{total:<10.4f}\r\n'
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(maxLimit))
    helpers.assess(child, 'ch6_13.py', key)
