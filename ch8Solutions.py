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
from subprocess import Popen, PIPE, STDOUT


library = ['hello', 'apparatus', 'consequence', 'missippi', 'alagash', 'illustrate', 'erradicate', 'impecible', 'american-indian', 'distillery', 'distinguished']


def ch8_1(file):
    tests = [['123456789', 'Valid SSN'], ['1234567890111213', 'Invalid SSN'],
            ['123-45-6789', 'Valid SSN'], ['123p45p6789', 'Invalid SSN'],
            ['1234567ok', 'Invalid SSN']]
    for i in range(5):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(tests[i][0])
        helpers.assess(child, f'ch8_1.py case {i + 1}', tests[i][1])


def ch8_2(file):
    words = ['hot', 'cold', 'cat', 'mouse', 'pizza', 'wet']
    
    def subPass(words):
        sub = key = random.choice(words)
        for each in words:
            key += random.choice(words)
        return sub, key
    
    def subFail(words):
        sub = random.choice(words)
        key = ''
        for each in words:
            temp = random.choice(words)
            if temp != sub:
              key += temp
        return sub, key
    
    sub, key = subPass(words)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(sub)
    child.sendline(key)
    helpers.assess(child, "ch8_2.py Case 1", 'is a substring')
    
    sub, key = subFail(words)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(sub)
    child.sendline(key)
    helpers.assess(child, "ch8_2.py Case 2", 'not a substring')
    
    
def ch8_3(file):
    
    def valid():
        password = ''
        digits = random.randint(2, 5)
        alpha = 9 - digits
        for digit in range(digits):
            password += str(random.randint(0,9))
        for char in range(alpha):
            password += chr(random.randint(97, 122))
        return password
        
    def dig_invalid():
        password = str(random.randint(0,9))
        for char in range(8):
            password += chr(random.randint(97, 122))
        return password
    
    def char_invalid():
        password = ''
        for char in range(9):
            password += chr(random.randint(33, 122))
        return password
    
    def len_invalid():
        password = ''
        digits = random.randint(2, 4)
        alpha = 7 - digits
        for digit in range(digits):
            password += str(random.randint(0,9))
        for char in range(alpha):
            password += chr(random.randint(65, 90))
        return password
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(valid())
    helpers.assess(child, "ch8_3.py Case 1", 'valid password')
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(dig_invalid())
    helpers.assess(child, "ch8_3.py Case 2", 'invalid password')
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(char_invalid())
    helpers.assess(child, "ch8_3.py Case 3", 'invalid password')
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(len_invalid())
    helpers.assess(child, "ch8_3.py Case 4", 'invalid password')
    

def ch8_4(file):
    words = [['apparatus', 'a', 3], ['missippi', 'i', 3],
            ['penelope', 'e', 3], ['sassafras', 's', 4]]
    child = pexpect.spawnu(f'python3 {file}')
    index = random.randint(0, 3)
    child.sendline(f'{words[index][0]}, {words[index][1]}')
    helpers.assess(child, "ch8_4.py", str(words[index][2]))
    

def ch8_5(file):
    print('Under Construction :(')
    
    
def ch8_6(file):
    def count_letters(s1):
        s2 = ''
        for each in s1:
            if each not in s2:
                s2 += each
        return len(s2)
    
    for i in range(4):
        child = pexpect.spawnu(f'python3 {file}')
        test = library[random.randint(0, len(library) - 1)]
        child.sendline(test)
        helpers.assess(child, f'ch8_6.py test{i + 1}', str(count_letters(test)))


def ch8_7(file):
    def get_number(letter):
        if letter in 'ABC':
            return 2
        elif letter in 'DEF':
            return 3
        elif letter in 'GHI':
            return 4
        elif letter in 'JKL':
            return 5
        elif letter in 'MNO':
            return 6
        elif letter in 'PQRS':
            return 7
        elif letter in 'TUV':
            return 8
        else:
            return 9
   
    for i in range(4):
        child = pexpect.spawnu(f'python3 {file}')
        test = chr(random.randint(65, 90))
        child.sendline(test)
        helpers.assess(child, f'ch8_7.py test{i + 1}', str(get_number(test)))
    
    
def ch8_8(file):
    print('Under Construction :(')
    

def ch8_9(file):
    print('Under Construction :(')
    
    
def ch8_10(file):
    print('Under Construciton :(')
    
    
def ch8_11(file):
    def reverse(s):
        s2 = ''
        i = len(s) - 1
        while i >= 0:
            s2 += s[i]
            i -= 1
        return s2
        
    for i in range(4):
        child = pexpect.spawnu(f'python3 {file}')
        test = library[random.randint(0, len(library) - 1)]
        child.sendline(test)
        helpers.assess(child, f'ch8_11.py test{i + 1}', str(reverse(test)))
        
    
def ch8_12(file):
    print('Under Construction :(')


def ch8_13(file):
    def prefix(s1, s2):
      prefix = ''
      if s1[0] == s2[0]:
        length = min(len(s1), len(s2))
        for i in range(length):
          if s1[i] == s2[i]:
            prefix += s1[i]
          else:
            break
      return prefix
        
    tests = ['disinfection', 'distance', 'diolate', 'dissatisfactory','dissimilarities', 'dissatisfactory', 'disable', 'disagree',
             'onynx', 'onion', 'onbaord', 'onomatopoeia', 'overboard', 'inline', 'online', 'reunion', 'satisfactory', 'violate']
    #case 1
    child = pexpect.spawnu(f'python3 {file}')
    s1 = random.choice(tests)
    while True: 
        s2 = random.choice(tests)
        if s1 != s2 and s1[0] == s2[0]:
            break
    key = prefix(s1, s2)
    child.sendline(s1)
    child.sendline(s2)
    helpers.assess(child, f'ch8_13.py case 1', key)
    
    #case 2
    child = pexpect.spawnu(f'python3 {file}')
    s1 = random.choice(tests)
    while True: 
        s2 = random.choice(tests)
        if s1 != s2 and s1[0] != s2[0]:
            break
    key = prefix(s1, s2)
    child.sendline(s1)
    child.sendline(s2)
    helpers.assess(child, f'ch8_13.py case 2', 'no matches')
