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


def sandbox(file):
    testMePath, studentPath, studentModule = helpers.functionTester(file)
    # print(testMePath, studentPath, studentModule)
    child = pexpect.spawnu(f'python3')
    n = random.randint(0, 10)
    m = random.randint(0, 10)
    child.sendline(f'import {studentModule}')
    child.sendline(f'print(studentTestModule.testFunction(n, m))')
    answerKey = f'{n + m}'
    try:
        child.expect_exact(answerKey)
        # pass
        print(f'{BY}Output is correct!')
        print(f'\n{G}{child.before}')
        print(f'{answerKey}')
        print(f'\n{BY}:)  == passed!{X}')
        child.terminate
    # fail
    except:
        print(f'{BY}Expected output of:\n\n{R}{answerKey}')
        print(f'\n{BY}Actual output was:\n\n{R}{child.before}')
        print(f'\n{BY}Actual output was:\n\n{A}{child.after}')
        print(f'{BY}:(  == failed{X}')
        child.terminate
    '''
    child.sendline(str(n))
    total = 0
    while n > 10:
        total += n % 10
        n //= 10
    total += n
    key = f'The sum of the numbers is {total}'
    helpers.assess(child, "ch6_2.py", key)
    '''
