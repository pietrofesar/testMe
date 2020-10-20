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

from subprocess import Popen, PIPE, STDOUT

from ch1Solutions import *
from ch2Solutions import *
from ch3Solutions import *
from ch4Solutions import *
from ch5Solutions import *
from ch6Solutions import *
from ch7Solutions import *
from learningPythonSolutions import *
from siennaSolutions import *


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

problemSets = {# chapter 1 Y. Liang
               'ch1_1.py' : ch1_1, 'ch1_2.py' : ch1_2, 'ch1_3.py' : ch1_3, 'ch1_4.py' : ch1_4, 'ch1_5.py' : ch1_5, 
               'ch1_6.py' : ch1_6,
               # chapter 2 Y. Liang
               'ch2_1.py' : ch2_1, 'ch2_2.py' : ch2_2, 'ch2_3.py' : ch2_3, 'ch2_4.py' : ch2_4, 'ch2_5.py' : ch2_5,
               'ch2_6.py' : ch2_6, 'ch2_7.py' : ch2_7, 'ch2_8.py' : ch2_8, 'ch2_9.py' : ch2_9, 'ch2_10.py' : ch2_10,
               'ch2_13.py' : ch2_13, 'ch2_14.py' : ch2_14, 'ch2_15.py' : ch2_15, 'ch2_18' : ch2_18,
               'ch2_19.py' : ch2_19, 'ch2_20.py' : ch2_20, 'ch2_21.py' : ch2_21,
               # chapter 3 Y. Liang
               'ch3_1.py' : ch3_1, 'ch3_2.py' : ch3_2, 'ch3_4.py' : ch3_4, 'ch3_5.py' : ch3_5, 'ch3_6.py' : ch3_6,
               'ch3_7.py' : ch3_7, 'ch3_11.py' : ch3_11,
               # chapter 4 Y. Liang
               'ch4_1.py' : ch4_1, 'ch4_2.py' : ch4_2, 'ch4_3.py' : ch4_3, 'ch4_5.py' : ch4_5, 'ch4_6.py' : ch4_6,
               'ch4_7.py' : ch4_7, 'ch4_8.py' : ch4_8, 'ch4_9.py' : ch4_9, 'ch4_10.py' : ch4_10, 'ch4_12.py' : ch4_12,
               'ch4_16.py' : ch4_16, 'ch4_17.py' : ch4_17, 'ch4_24.py' : ch4_24,
               # chapter 5 Y. Liang
               'ch5_1.py' : ch5_1, 'ch5_2.py' : ch5_2, 'ch5_3.py' : ch5_3, 'ch5_4.py' : ch5_4, 'ch5_6.py' : ch5_6,
               'ch5_7.py' : ch5_7, 'ch_8.py' : ch5_8, 'ch5_11.py' : ch5_11, 'ch5_12.py' : ch5_12, 'ch5_13.py' : ch5_13,
               'ch5_17.py' : ch5_17, 'ch5_20A.py' : ch5_20A, 'ch5_20B.py' : ch5_20B, 'ch5_21.py' : ch5_21,
               # chapter 6 Y. Liang
               'ch6_2.py' : ch6_2, 'ch6_3.py' : ch6_3, 'ch6_4.py' : ch6_4, 'ch6_5.py' : ch6_5, 'ch6_6.py' : ch6_6,
               'ch6_7.py' : ch6_7, 'ch6_8.py' : ch6_8, 'ch6_9.py' : ch6_9, 'ch6_12.py' : ch6_12, 'ch6_13.py' : ch6_13,
               # chapter 8 Y. Liang
               'ch8_2.py' : ch8_2, 'ch8_3.py' : ch8_3, 'ch8_4.py' : ch8_4, 'ch8_5.py' : ch8_5,
               'ch8_6.py' : ch8_6, 'ch8_7.py' : ch8_7, 'ch8_8.py' : ch8_8, 'ch8_9.py' : ch8_9, 'ch8_10.py' : ch8_10,
               'ch8_11.py' : ch8_11, 'ch8_12.py' : ch8_12, 'ch8_13.py' : ch8_13,
               # chapter 10 Y. Liang
               'ch10_1.py' : ch10_1, 'ch10_2.py' : ch10_2, 'ch10_3.py' : ch10_3, 'ch10_4.py' : ch10_4, 
               'ch10_5.py' : ch10_5, 'ch10_6.py' : ch10_6, 'ch10_7.py' : ch10_7, 'ch10_8.py' : ch10_8,
               'ch10_9.py' : ch10_9, 'ch10_10.py' : ch10_10,
               # Sienna Programming Contest
               'green1_18.py' : green1_18, 'green2_18.py' : green2_18, 'green3_18.py' : green3_18, 'green4_18.py' : green4_18,
               'green5_18.py' : green5_18, 'green6_18.py' : green6_18, 'green7_18.py' : green7_18,
               # Learning Python and CS50
               'average.py' : average, 'binary_search.py' : binary_search, 'birthMonth.py' :  birthMonth, 
               'evenOdd.py' : evenOdd, 'fahrenheit.py' : fahrenheit, 'rockPaperScissors.py' : rockPaperScissors, 
               'slices.py' : slices, 'madlib.py' : madlib, 'hypotenuse.py' : hypotenuse, 'polygon.py' : polygon,
               'reportCard.py' : reportCard, 'greedy.py' : greedy, 'gradeBook.py' : gradeBook, 'temperature.py' : temperature,
               'initials.py' : initials, 'leftStack.py' : leftStack, 'rightStack.py' :  rightStack,
               'pyramidStacks.py' : pyramidStacks, 'lottery.py' : lottery, 'validate.py' : validate}
    
    
def main():
    # validate arguments
    if len(sys.argv) == 1:
        print('testMe version 3.0.0\nAuthor: Rocco Pietrofesa\nDate: 10/10/2020')
    elif len(sys.argv) == 2:
        try:
            # find and store the file
            studentFile = helpers.findInSubdirectory(sys.argv[1])
            for i in studentFile.split('/'):
                if i.endswith('.py'):
                    pset = i
            problemSets[pset](studentFile)
           
           
        except IOError as e:
            print(f'{BR}ERROR\n{Y}{sys.argv[1]}{X} doesn\'t exist or is incorrectly named')
            
    else:
       print('wrong amount of arguments given')
        
if __name__ == "__main__":
    main()
