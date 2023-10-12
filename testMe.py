#!/usr/bin/env python3.6
""" check.py docstring
	This program will autocheck student problem sets for the python curriculum I've designed
	The problem sets are taken from numerous coureses and texts, I don't claim they are original.
	http://pexpect.sourceforge.net/pexpect.html - only works in Linux environment

	****notes
		* spawn instead of spawnu shows unformatted strings for debugging

	:param file: the python file passed as a command line argument 
	:return None: each routine has a side effect, it prints the output and wether or not they were successful 
Todo:
	* implement the Exception thrown by try-except so that user can see it better
	* string slicing relies on hypothetical child.before strings; look for bugs while piloting grader, could produce exceptions
	* binary_search.py(beta status)
	* validate_functions.py(alpha status)
	* validate.py(beta status)
	* troubleshoot line 60


Author: Rocco Pietofesa
Date: 1/14/20
Please credit author for any use/modification of this base program
Please send donation to pietrofesar@gmail.com via PayPal if you find this useful
"""
import pexpect
import sys
import os
import random
import math
import time
import helpers
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT

# import the solutions
from sandBoxSolutions import *
from ch1Solutions import *
from ch2Solutions import *
from ch3Solutions import *
from ch4Solutions import *
from ch5Solutions import *
from ch6Solutions import *
from ch7Solutions import *
from ch8Solutions import *
from ch10Solutions import *
from learningPythonSolutions import *
from siennaSolutions import *

# version number
VERSION = '4.0.9'

# text color constants
R = '\033[0;31m'  # red
BR = '\033[1;31m'  # bold red
G = '\033[0;32m'  # green
BG = '\033[1;32m'  # bold green
Y = '\033[0;33m'  # yellow
BY = '\033[1;33m'  # bold yellow
B = '\033[0;34m'  # blue
BB = '\033[1;34m'  # bold blue
P = '\033[0;35m'  # purple
BP = '\033[1;35m'  # bold purple
A = '\033[0;36m'  # aqua
BA = '\033[1;36m'  # bold aqua
X = '\033[0m'  # reset


def main():
    # validate arguments
    if len(sys.argv) == 1:
      print(f'{A}\nName: testMe\nVersion: {VERSION}\nSummary: testMe is a homegrown autograder\nAuthor: Rocco Pietrofesa\nAuthor-email: pietrofesar@gmail.com\nArmand Caringi helped too!{X}\n')
    # wrong number of arguments - not working
    elif len(sys.argv) != 2:
        print(f'{R}Wrong amount of arguments entered{X}')
    # incorrectly spelled
    elif helpers.findInSubdirectory(sys.argv[1]) == None:
        print(f'{R}File is mispelled or does not exist{X}')
    # solution doesn't exist

    # file is empty
    elif os.path.getsize(Path(helpers.findInSubdirectory(sys.argv[1]))) == 0:
        print(f'{R}Your file exists but is empty{X}')
    # store pset value
    else:
        studentFile = helpers.findInSubdirectory(sys.argv[1])  
        # get the pset for function call
        for i in studentFile.split('/'):
            if i.endswith('.py'):
                pset = i[:-3]
        # call the solution
        try:
            eval(pset + '(studentFile)')
        except:
            # print(e)
            print(f'{BA}Fatal Error\n{Y}Run your submission in the shell and look for exceptions\nLook in your code for highlighted errors too\n{X}')

            sys.exit()
main()
