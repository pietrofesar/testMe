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


def helloWorld(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = 'Hello World!\r\nWelcome to Computer Science\r\nProgramming is fun\r\n'
    # check the correctness of the submission
    helpers.assess(child, "helloWorld.py", key)
    

def fun(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = 'FFFF  U    U  N    N\r\nF     U    U  NN   N\r\nFFFF  U    U  N N  N\r\nF     U    U  N  N N\r\nF      UUUU   N   NN\r\n'
    helpers.assess(child, "fun.py", key)
    
 
def smileyFace(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = ' ---------\r\n|  O   O  |\r\n|    U    |\r\n|  \\___/  |\r\n|         |\r\n ---------\r\n'
    helpers.assess(child, "smileyFace.py", key)
    
            
def ch1_4(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = 'a      a^2    a^3\r\n1      1      1\r\n2      4      16\r\n3      9      27\r\n4      16     64\r\n'
    helpers.assess(child, "ch1_4.py", key)


def ch1_5(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = f'{(9.5*4.5-2.5*3)/(45.5-3.5)}\r\n'
    helpers.assess(child, "ch1_5.py", key)
            
            
def ch1_6(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = f'area is {4.5 * 7.9}\r\nperimeter is {4.5 * 2 + 7.9 * 2}\r\n'
    # check the correctness of the submission
    helpers.assess(child, "ch1_6.py", key)
            

