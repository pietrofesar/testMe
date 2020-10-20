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


def ch1_1(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = 'Welcome to Python\r\nWelcome to Computer Science\r\nProgramming is fun\r\n'
    # check the correctness of the submission
    helpers.assess(child, "ch1_1.py", key)
    

def ch1_2(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = 'FFFF  U    U  N    N\r\nF     U    U  NN   N\r\nFFFF  U    U  N N  N\r\nF     U    U  N  N N\r\nF      UUUU   N   NN\r\n'
    # check the correctness of the submission
    helpers.assess(child, "ch1_2.py", key)
    

def ch1_3(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = ' ---------\r\n|  O   O  |\r\n|    U    |\r\n|  \___/  |\r\n|         |\r\n ---------'
    # check the correctness of the submission
    helpers.assess(child, "ch1_3.py", key)


def ch1_4(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = '{0:7s}{1:7s}{2:s}\r\n'.format('a', 'a^2', 'a^3') + '{0:<7d}{1:<7d}{2:d}\r\n'.format(1, 1, 1) +\
                '{0:<7d}{1:<7d}{2:d}\r\n'.format(2, 4, 16) + '{0:<7d}{1:<7d}{2:d}\r\n'.format(3, 9, 27) + \
                '{0:<7d}{1:<7d}{2:d}\r\n'.format(4, 16, 64)
    # check the correctness of the submission
    helpers.assess(child, "ch1_4.py", key)
    
 
def ch1_5(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = str((9.5 *4.5-2.5*3)/(45.5-3.5))
    # check the correctness of the submission
    helpers.assess(child, "ch1_5.py", key)
    

def ch1_6(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = 'area is {0:.2f}\r\nperimeter is {1:.2f}\r\n'.format(4.5 * 7.9, (2 * 4.5 + 2 * 7.9))
    # check the correctness of the submission
    helpers.assess(child, "ch1_6.py", key)