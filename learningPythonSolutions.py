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


def rockPaperScissors(file):
    def test(first, second):
        combined = first + second
        if 'PAPER' in combined and 'ROCK' in combined:
            return 'PAPER WINS'
        elif 'SCISSORS' in combined and 'PAPER' in combined:
            return 'SCISSORS WINS'
        elif 'ROCK' in combined and 'SCISSORS' in combined:
            return 'ROCK WINS'
        else:
            return "TIE"
        
        
    tests = ['ROCK', 'PAPER', 'SCISSORS']
    for i in range(3):
        child = pexpect.spawnu(f'python3 {file}')
        first = tests[i % 3]
        second =  tests[(i + 1) % 3]
        child.sendline(first)
        child.sendline(second)  
        answer_key = test(first, second)
        
        helpers.assess(child, f'rock_paper_scissors.py Case{i + 1}', answer_key)
        
            

def slices(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
        test suite for slices.py
    """
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    key = 'Be\r\nyourself\r\neveryone\r\nelse\r\nis\r\nalready\r\ntaken\r\n'
    # check the correctness of the submission
    helpers.assess(child, "slices.py", key)
    if child.isalive:
            child.kill(2)
     

def madlib(file):
        """
        :param file: the python file passed as a command line argument 
        :return None: 
        test suite for madlib.py
        """
        # words to enter
        words = ['<to>', '<adj>', '<verb1>', '<body_part>', '<num>', '<noun>', '<adverb>', '<verb2>', '<verb3>',
                '<pronouns>', '<author>']
        key = 'Dear <to>,\r\nYou are extremely <adj> and I <verb1> you.\r\n' \
                 'I want to kiss your <body_part> <num> times.\r\n' \
                 'You make my <noun> burn with desire.\r\n' \
                 'When I first saw you, I <adverb> <verb2> at you and fell in love.\r\n' \
                 'Will you <verb3> out with me?\r\n' \
                 'Don\'t let your parents discourage you, <pronouns> are just jealous.\r\n' \
                 'Yours forever, <author> :)\r\n'
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')
        # enters the words
        for each in words:
            child.sendline(each)
        helpers.assess(child, "madlib.py", key)
        if child.isalive:
            child.kill(2)


def greedy(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for greedy.py
    """
    # creates the child instance
    data_in = [3.84,  1.10, .30, .04]
    data_out = ['15 quarters, 0 dimes, 1 nickels, 4 pennies', '4 quarters, 1 dimes, 0 nickels, 0 pennies', '1 quarters, 0 dimes, 1 nickels, 0 pennies', '0 quarters, 0 dimes, 0 nickels, 4 pennies']
    
    for i, each in enumerate(data_in):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(str(each))
        helpers.assess(child, "greedy.py", key)
        if child.isalive:
                child.kill(2) 

           
def hypotenuse(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for hypotenuse.py
    """
    key = ['Enter the side length:', 'The hypotenuse is ']
    data = ['3.1', '4.1', '5.14']
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(data[0])
    child.sendline(data[1])
    # check the correctness of submission
    try:
        child.expect_exact(key[1] + data[2])
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) hypotenuse.py == passed{}'
        .format(BY, G, child.before, child.match, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}{}\n{}{}\n{}{}\n\n{}Actual output was:\n\n{}{}\n{}:( slices.py == failed{}'
        .format(BY, R, key[0], data[0], key[0], data[1], key[1], data[2], BY, R, child.before, BY, X))
    if child.isalive:
            child.kill(2)


def average(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for hypotenuse.py
    """
    grade = ['first', 'second', 'third', 'fourth']
    nums = ['78', '97', '86', '88', '87']
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(nums[0])
    child.sendline(nums[1])
    child.sendline(nums[2])
    child.sendline(nums[3])
    # check the correctness of submission
    try:
        child.expect_exact('The average is 87')
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) average.py == passed{}'
        .format(BY, G, child.before, child.match, BY, X))
    # fail
    except:
        print('{}Expected output of:{}\n'.format(BY, R))
        for i, each in enumerate(grade):
            print('Enter the {} grade: {}'.format(grade[i], nums[i]))
        print('The average is 87')
        print('\n{}Actual output was:\n\n{}{}\n{}:( average.py == failed{}'.format(BY, R, child.before, BY, X))
    if child.isalive:
            child.kill(2)


def polygon(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for average.py
    """
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline('6')
    # check the correctness of submission
    try:
        child.expect_exact('The interior angles are 120.0 degrees.')
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) polygon.py == passed{}'
        .format(BY, G, child.before, child.match, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}Enter the number of sides: 6\nThe interior angles are 120.0 degrees.\n'.format(BY, R))
        print('{}Actual output was:\n\n{}{}\n{}:( polygon.py == failed{}'.format(BY, R, child.before, BY, X))
    if child.isalive:
            child.kill(2)
            

def fahrenheit(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for fahrenheit.py
    """
    data = [['0', '0.0'], ['100', '100.0'], ['32', '32.0'], ['212', '212.0']]
    key = ['Hai! Enter the temperature in degrees Fahrenheit: ', '{} degrees Fahrenheit is childroximately {} degrees Celsius.']
    
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(data[3][0])
    # check the correctness of submission
    try:
        child.expect_exact(key[1].format(data[3][1], data[1][1]))
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) fahrenheit.py == passed{}'
        .format(BY, G, child.before, child.match, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}{}\n{}\n{}\nActual output was:\n\n{}{}{}\n:( fahrenheit.py == failed{}'
        .format(BY, R, key[0], data[3][0], key[1].format(data[3][1], data[1][1]), BY, R, child.before, BY, X))
    if child.isalive:
            child.kill(2)
            

def reportCard(file):
        """
        :param file: the python file passed as a command line argument 
        :return None: 
        test suite for fahrenheit.py
        """
        # words to enter
        data = ['Einstein', '99.8', '98.7', '95.3', '81.4', '75.0', '68.5']

        key = 'This is {}\'s report card.\r\n\r\n' \
         '6 sorted grades: [{}, {}, {}, {}, {}, {}]\r\n\r\n' \
         '{}\'s highest grade is {}.\r\n\r\n' \
         'The low grade of {} is being dropped.\r\n\r\n' \
         'Now {}\'s grades are [{}, {}, {}, {}, {}].\r\n\r\n' \
         '{}\'s average is now 90.0.\r\n\r\n'.format(data[0], data[6], data[5], data[4], data[3], data[2], data[1],
                                                     data[0], data[1], data[6], data[0], data[5],
                                                     data[4], data[3], data[2], data[1], data[0])
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')
        # enters the words
        for each in data:
            child.sendline(each)
        # check the correctness of submission
        try:
            child.expect_exact(key)
            # pass
            print('\n{}Output is correct!\n{}{}\n{}{}:) report_card.py == passed\n{}'
            .format(BY, G, child.before, child.match, BY, X))
        # fail
        except:
            print(child.before)
            print('\n{}Expected output of:\n{}{}\n{}Actual output was:\n{}{}{}:( report_card.py == failed{}'
            .format(BY, R, key, BY, R, child.before[225:], BY, X))
        if child.isalive:
            child.kill(2)
            

def evenOdd(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for even_odd.py
    """
    ok = 0
    test_data = [['2', 'even'], ['3', 'odd'], ['-1', 'odd'], ['-2', 'even']]
    for i in range(4):
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline('{}'.format(test_data[i][0]))
        # check the correctness of submission
        try:
            child.expect_exact('{} is an {} number.'.format(test_data[i][0], test_data[i][1]))
            # pass
            print('{}{}'.format(G, child.match))
            ok += 1
        # fail
        except:
            print('\n{}Expected output of:\n{}{} is an {} number.\n{}Actual output was:\n{}{}{}'
            .format(BY, R, test_data[i][0], test_data[i][1], BY, R, child.before[19:], X))
        if child.isalive:
            child.kill(2)
    if ok == 4:
        print('{}:) even_odd.py == passed{}'.format(BY, X))
    else:
        print('{} even_odd.py == failed{}'.format(BY, X))


def birthMonth(file):
    """ birth_month.py autograder """
    samples = random.randint(2, 6)
    birthMonths = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    
    for sample in range(samples):
        child = pexpect.spawnu(f'python3 {file}')   
        birthMonth = random.choice(list(birthMonths))
        child.sendline(str(birthMonth))
        
        key = f'You were born in {birthMonths[birthMonth]}'
        helpers.assess(child, f'{file} case {sample + 1}', key)
        

def gradeBook(file):
    """ gradeBook.py autograder """
  
    grades = [['92', 'A'], ['84', 'B'], ['76', 'C'], ['65', 'D'], ['64', 'F']]
    for i in range(len(grades)):
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')     
        child.sendline('{}'.format(grades[i][0]))
        # check the correctness of submission
        key = f'{grades[i][1]} is your letter grade.'
        helpers.assess(child, f'gradeBook.py case{i + 1}', key)
        
def temperature(file): 
    """ temperature.py autograder """
    # check conversion to Fahrenheit
    tempC = random.randint(0, 100)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline('F')
    child.sendline(str(tempC))
    key = f'{tempC * (9/5) + 32:.1f}'
    helpers.assess(child, 'temperature.py case: 1', key)
    # check conversion to Celsius
    tempF = random.randint(32, 212)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline('C')
    child.sendline(str(tempF))
    key = f'{(tempF - 32) * (5/9):.1f}'
    helpers.assess(child, 'temperature.py case: 2', key)
    

def initials(file): # updated
    """initials.py autograder """
    ok = 0
    checks = 3
    data = [['albert percival wulfric brian dumbledore', 'APWBD'], ['ben franklin', 'BF'], ['broomhilda von shaft', 'BVS']]
    for i in range(checks):
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')     
        child.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            child.expect_exact('{}'.format(data[i][1]))
            # pass
            print('{}{}{}{}'.format(child.before, G, child.match, X))
            ok += 1
        # fail
        except:
            index = str(child.before.encode('utf-8')).index(chr(92)) # finds first \r in child.before for slice
            print('{}'.format(child.before[:index-1]))
            print('{}Expected output of:\n{}{}{}'.format(BY, R, data[i][1], X))
            print('{}Actual output was:\n{}{}{}'.format(BY, R, child.before[index:len(child.before)-2], X))
        if child.isalive:
            child.kill(2)
    if ok == checks:
        print('{}:) {} == passed{}'.format(BY, file, X))
    else:
        print('{}:( {} == failed{}'.format(BY, file, X))


def leftStack(file):
    height = random.randint(3, 8)
    key = ''
    for row in range(1, height + 1):
        key += row * '#' + '\r\n'
    child = pexpect.spawnu(f'python3 {file}')     
    child.sendline(str(height))
    helpers.assess(child, f'leftStack.py', key)
    

def rightStack(file):
    height = random.randint(3, 8)
    spaces = height - 1
    key = ''
    for row in range(1, height + 1):
        for space in range(spaces):
            key += ' '
        spaces -= 1    
        key += row * '#' + '\r\n'
    child = pexpect.spawnu(f'python3 {file}')     
    child.sendline(str(height))
    helpers.assess(child, f'rightStacks.py', key)
    
    
def pyramidStacks(file):
    key, height, hashes, spaces = '', random.randint(3, 8), 1, height -1
    for row in range(1, height + 1):
        for space in range(spaces):
            key += ' '
        for hash in range(hashes):
            key += '#'
        spaces -= 1
        hashes += 2
        key += '\r\n'
    
def validate(file):
    """validate.py autograder 
    this needs to be gone over with test cases, still in beta
    """
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')  
    ok = 0
    data = [3, -6, - 8.9, '$', '\r', 'pickles', 'C']
    for i, each in enumerate(data):
        child.sendline(str(data[i]))
        # checking alpha validation
        if each == 'C':
            # alpha passed
            print('{}{}{}{}'.format(child.match, BG, each, X))
            print('{}Alpha validation passed!\n{}'.format(G, X))
            data.reverse()
            # checking for numeric validation
            for i, each in enumerate(data):
                child.sendline(str(data[i]))
                if type(each) != str and 0 < each < 10:
                    #numeric passed
                    print('{}{}{}{}'.format(child.match, BG, each, X))
                    print('{}Numeric validation passed!\n{}'.format(G, X))
                    print('{}:) {} == passed!{}'.format(BY, file, X))
                # cycle numeric data test   
                else:
                    try:
                        child.expect_exact('Enter a positive number: ', timeout=1.5)
                        # pass
                        print('{}{}'.format(child.match, data[i]))
                    #fail
                    except Exception as e:
                        print('{}Numeric Validation Error\n\n{}{}{}'.format(BR, R, e, X))
                        print('{}:( {} == failed!{}'.format(BY, file, X))
                        break    
        # cycle alpha data test
        else:
            try:
                child.expect_exact('Enter a letter: ', timeout=1.5)
                # pass
                print('{}{}'.format(child.match, data[i]))
            # fail
            except:
                print('{}Alpha Validation Error\n\n{}{}{}'.format(BR, R, child.before, X))
                print('{}:( {} == failed!{}'.format(BY, file, X))
                break
    if child.isalive:
            child.kill(2)
            
            
def validate_functions(file):
    """validate_functions.py autograder """
    # creates the child instance
    child = pexpect.spawn('python3')
    child.sendline('from validate_functions import *')
    child.sendline('temp = test()')
    child.sendline('print(temp)')
    try:
        child.expect('test printed')
        print('yes the test has passed')
    except Exception as e:
        print(e)
    # print(child.before.decode("utf-8")) 
    print(child.after.decode("utf-8"))           
    '''
    pexpect.run('python3', timeout=3, events={'(?i)Python 3.4.3 (default, Nov 17 2016, 01:08:31)\n[GCC 4.8.4] on linux\nType "help",\
                                    "copyright", "credits" or "license" for more information.':'quit()'})
    '''

def binary_search(file):
    """ binary_search.py autograder """
    ok = 0
    checks = 4
    for i in range(checks):
        start = 0
        end = 1000
        middle = 500
        # creates the child instance
        child = pexpect.spawnu('python3 {}'.format(file), timeout=5) 
        print('Test run number {}\nGuess a number between 1 and 1000: 500'.format(i + 1))
        while True:
            child.sendline(str(middle))
            # check the correctness of submission
            # print(start, end, middle)
            index = child.expect_exact(['too low, try again; guess-->', 'too high, try again; guess-->',
                                    'You guessed it, the secret number was {}'.format(middle), pexpect.EOF, pexpect.TIMEOUT])
            # too low
            if index == 0:
                start = middle + 1
                # factored form, orginal -->int((end - start) / 2) + start
                middle = int(end / 2 + .5 * start) 
                print('too low, try again; guess-->{}'.format(middle))
            # too high
            elif index == 1:
                end = middle - 1
                middle = int(end / 2 + .5 * start) 
                print('too high, try again; guess-->{}'.format(middle))
            # number has been guessed                
            elif index == 2:
                ok += 1
                print('{}{}{}\n'.format(G, child.match, X))
                break 
            # exception raised
            elif index == 3 or 4:
                print('{}errors in your code{}'.format(R, X))
                break
            else:
                print('{}error in code{}'.format(R, X))
                break
            
    if ok == checks:
        print('{}:) {} == passed{}'.format(BY, file, X))
    else:
        print('{}:( {} == failed{}'.format(BY, file, X))


def lottery(file):

    def createTest(file):
        child = pexpect.spawnu(f'python3 {file}')
        secret = int(child.read_nonblocking(size=2, timeout=-1).strip())
        secret1 = secret // 10 # isolate first digit
        secret2 = secret % 10 # isolate second digit
        return [child, secret, secret1, secret2]
    
    
    def case1(data):
        data[0].sendline(str(data[1]))
        key = 'You won $10000'
        print(f'Secret is {data[1]}')
        helpers.assess(data[0], "lottery.py Case 1", key)
    
            
    def case2(data):
        data[0].sendline(f'{data[3]}{data[2]}')
        key = 'You won $3000'
        print(f'Secret is {data[1]}')
        helpers.assess(data[0], "lottery.py Case 2", key)
    
    
    def case3(data):
        while True:
            noMatch = random.randint(1,9)
            if noMatch != data[2] and noMatch != data[3]:
                break
            else:
                continue
        data[0].sendline(f'{data[3]}{noMatch}')
        key = 'You won $1000'
        print(f'Secret is {data[1]}')
        helpers.assess(data[0], "lottery.py Case 3", key)
    
    
    def case4(data):
        while True:
            noMatch = random.randint(1,9)
            if noMatch != data[2] and noMatch != data[3]:
                break
            else:
                continue
        data[0].sendline(f'{noMatch}{noMatch}')
        key = 'You won $0'
        print(f'Secret is {data[1]}')
        helpers.assess(data[0], "lottery.py Case 4", key)

    
    case1(createTest(file))
    case2(createTest(file))
    case3(createTest(file))
    case4(createTest(file))
