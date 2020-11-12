import pexpect
import sys
import os
import random
import math
import time

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


library = ['hello', 'apparatus', 'consequence', 'missippi', 'alagash', 'illustrate', 'erradicate', 'impecible', 'american-indian', 'distillery', 'distinguished']

# searches for a file in the tree
def findInSubdirectory(filename, subdirectory=''):
    if subdirectory:
        path = subdirectory
    else:
        path = os.getcwd()
    for root, dirs, names in os.walk(path):
        if filename in names:
            return os.path.join(root, filename)
    #raise 'File not found'
    
def find_nth(haystack, needle, n):
    """
    substring helper 
    :param haystack: string to be searched
    :param needle:   substring to find
    :param n:        desired occurence location of substring  
    :return i:       the index of the nth substring occurence 
    """
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)
    

def b_sanitize(before):
    """
    substring helper
    :param before:  child.before->string type
    :return parts:  a list of the lines or an empty list if error occured
    """
    parts = []
    try:
        parts = str(before).strip("b'").split('\r\n')
    except:
        pass
    return parts

def assess(child, pset, answerKey, read=""):
    """
    assesses the output of the calling function for correctness, reports the output
    """
    # check the correctness of the submission
    try:
        child.expect_exact(answerKey)
        # pass
        print(f'{BY}Output is correct!')
        print(f'\n{G}{read}{child.before}')
        print(f'{answerKey}')
        print(f'\n{BY}:) {pset} == passed!{X}')
        child.terminate
    # fail
    except:
        print(f'{BY}Expected output of:\n\n{R}{answerKey}')
        print(f'\n{BY}Actual output was:\n\n{R}{read}{child.before}')
        print(f'\n{BY}Actual output was:\n\n{A}{read}{child.after}')
        print(f'{BY}:( {pset} == failed{X}')
        child.terminate


def getOperands(theString): 
    #print(f'in getOperands {Y}{theString}{X}')
    while len(theString) != 0 and not theString[0].isdigit():
        theString = theString[1:]
    while len(theString) != 0 and not theString[-1].isdigit():
        theString = theString[:-1]
        print()
    operands = [int(i) for i in theString.split() if i.isdigit()]
    return operands
    
def functionTester(_studentFile):
    testMePath = os.getcwd()
    studentFile = findInSubdirectory(_studentFile)
    studentModule = studentFile[:studentFile.find('.')]
    i = studentFile.rfind('/')
    studentPath = studentFile[:i]
    return testMePath, studentPath, studentModule
