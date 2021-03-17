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


def green1_18(file):
    def fourthsum(n):
        result = 0
        for i in range(1, n + 1):
            result += i**4
        return result
    
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(0, 9)
    child.sendline(str(n))
    helpers.assess(child, 'g1_2018.py', str(fourthsum(n)))


def green2_18(file):
    def test(first_symbol, second_symbol):
        if first_symbol == 'Rock':
            if second_symbol == 'Scissors' or second_symbol == 'Lizard' or second_symbol == 'Zombie':
                return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else:
                return second_symbol
        elif first_symbol == 'Paper':
            if second_symbol == 'Rock' or second_symbol == 'Spock' or second_symbol == 'LargeHadronCollider':
                return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else:
                return second_symbol
        elif first_symbol == 'Scissors':
            if second_symbol == 'Paper' or second_symbol == 'Lizard' or second_symbol == 'Zombie':
                return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else:
                return second_symbol
        elif first_symbol == 'Lizard':
            if second_symbol == 'Paper' or second_symbol == 'Spock' or second_symbol == 'LargeHadronCollider':
                 return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else: 
                return second_symbol
        elif first_symbol == 'Spock':
            if second_symbol == 'Rock' or second_symbol == 'Scissors' or second_symbol == 'Collider':
                 return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else: 
                return second_symbol
        elif first_symbol == 'Zombie':
            if second_symbol == 'Paper' or second_symbol == 'Lizard' or second_symbol == 'Spock':
                 return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else: 
                return second_symbol
        else:
            if second_symbol == 'Rock' or second_symbol == 'Scissors' or second_symbol == 'Zombie':
                 return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else: 
                return second_symbol  
    
    symbols = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock', 'Zombie', 'LargeHadronCollider']
    child = pexpect.spawnu(f'python3 {file}')
    first = symbols[random.randint(0, len(symbols) - 1)]
    while True:
        second = symbols[random.randint(0, len(symbols) - 1)]
        if first != second:
            break
    child.sendline(first)
    child.sendline(second)
    helpers.assess(child, 'g2_2018.py', test(first, second))

    
def green3_18(file):
    def get_time(current, alarm):
        if current < 720 and alarm < 720:
            if current > alarm:
                return 1440 - current + alarm
            else:
                return alarm - current
        elif current < 720 and alarm > 720:
            return alarm - current
        else:
            if alarm > current:
                return alarm - current
            else:
                return 1440 - current + alarm
        
    current_hour = random.randint(7, 23)
    current_minute = random.randint(10, 58)
    current_time = current_hour * 60 + current_minute
    alarm_hour = random.randint(7, 23)
    alarm_minute = random.randint(10, 58)
    alarm_time = alarm_hour * 60 + alarm_minute
    
    duration = get_time(current_time, alarm_time)
    hours = duration // 60
    minutes  = duration % 60
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(current_hour))
    child.sendline(str(current_minute))
    child.sendline(str(alarm_hour))
    child.sendline(str(alarm_minute))
    helpers.assess(child, 'g3_2018.py', f'{hours} {minutes}')
    
    
def green4_18(file):
    tests = ['mountains', 'altruism', 'alphanumeric', 'beautiful', 
            'parameterize', 'automobile' 'absurdism', 
            'underwear', 'organisms']
    word = tests[random.randint(0, len(tests) - 1)]
    ranges = [[0, 2], [3, 4], [5, 6], [7, 9]]
    indices = []
    n = random.randint(2, 4)
    for each in range(n):
        indices.append(random.randint(ranges[each][0], ranges[each][1]))
    
    answer_key = ''
    for i in range(len(word)):
        if i not in indices:
            answer_key += word[i]
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(word)
    child.sendline(str(n))
    for each in range(n):
        child.sendline(str(indices[each] + 1))
    helpers.assess(child, 'g4_2018.py', answer_key)
    

def green5_18(file):
    tests = [['Elvis', 'Lives!'], ['Astronomer', 'moon starers'],
            ['clothes pins', 'so let\'s pinch'], 
            ['Slot machines', 'Cash lost in \'em'],
            ['A registrant\'s friend', 'Transfinder is great!!!']]
    
    def sterilize(word):
        # removes any chars other than alpha
        word = word.strip()
        word = word.lower()
        sterilized = ''
        for each in word:
            if each.isalpha():
                sterilized += each
        return sterilized
    
    
    def uniqe_letters(sterilized):
        # collects a copy of each uniqe letter in sorted order
        letters = []
        for each in sterilized:
            if each not in letters:
                letters.append('each')
        letters.sort()
        return letters
        
    
    def compare_lists(list1, list2):
        if list1 == list2:
            return True
        else:
            return False
    
    for i in range(4):
        first = tests[i][0]
        second = tests[i][1]
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(first)
        child.sendline(second)
        
        first = sterilize(first)
        first = uniqe_letters(first)
        
        second = sterilize(second)
        second = uniqe_letters(second)
    
        if compare_lists(first, second):
            answer_key = 'YES'
        else:
            answer_key = 'NO'
            
        helpers.assess(child, f'g5_2018.py Case{i + 1}', answer_key)
        

def green6_18(file):
    
    def primary(N):
        answer_key = ''
        for base in range(2, 11):
            max_exponent = find_exponent(N, base)
            converted = converted_base(N, base, max_exponent)
            if is_mono_digit(converted):
                answer_key += f'{N} Base {base}: {converted}\r\n'
        return answer_key
        
        
    def find_exponent(N, base):    
        # finds the greatest base quantity in the number N
        exponent = 0
        while N >= base**exponent:
            exponent += 1
        return exponent - 1
       
    
    def converted_base(N, base, exponent):
        # returns N in converted to a new base as a string
        number = ''
        while exponent >= 0:
            number += str(N // base**exponent) 
            N %= base**exponent
            exponent -= 1
        return number
        
    
    def is_mono_digit(number):
        for each in number:
            if each == number[0]:
                continue
            else:
                return False
        return True
    
    
    child = pexpect.spawnu(f'python3 {file}')
    while True:
        N = random.randint(4, 1000)
        answer_key = primary(N)
        if answer_key != '':
            break
    child.sendline(str(N))
    helpers.assess(child, f'green6_18.py', answer_key)
    
    
def green7_18(file):
    
    def get_sets(cards):
        sets = []
        if '1DSR' in cards and '1OSV' in cards and '1PSG' in cards:
            sets.append('1DSR 1OSV 1PSG')
        if '1DSR' in cards and '2DHV' in cards and '3DLG' in cards:
            sets.append('1DSR 2HDV 3DLG')
        if '1OHG' in cards and '2OLV' in cards and '3OSR' in cards:
            sets.append('1OHG 2OLV 3OSR')
        if '1PSR' in cards and '2DSR' in cards and '3OSR' in cards:
            sets.append('1PSR 2DSR 3OSR')
        if '2DSR' in cards and '2OLV' in cards and '2PHG' in cards:
            sets.append('2DSR 2OLV 2PHG')
        if '3DLG' in cards and '3OSR' in cards and '3PHV' in cards:
            sets.append('3DLG 3OSR 3PHV')
        sets.sort()
        return sets
        
    def generate_test_cards():
        while True:
            num_of_cards = random.randint(3, 12)
            list_of_cards = ['1DSR', '3OSR', '2PHG', '3PHV', '1PSR', '2DHV', 
                            '3DLG', '1PSG', '2DSR', '1OSV', '1OHG', '2OLV']
            test_cards = []
            for n in range(num_of_cards):
                while True:
                    i = random.randint(0, len(list_of_cards) - 1)
                    if list_of_cards[i] not in  test_cards:
                        test_cards.append(list_of_cards[i])
                        break
            if len(get_sets(test_cards)) != 0:
                break
        return num_of_cards, test_cards   
        
    n, test_cards = generate_test_cards()
    sets = get_sets(test_cards)
    answer_key = ''
    for each in sets:
        answer_key += f'{each}\r\n'
       
        
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(n))
    for each in test_cards:
        child.sendline(each)
    helpers.assess(child, f'green7_18.py', answer_key)
    

def green1_19(file):
    
    dividend = random.randint(2, 50)
    divisor = random.randint(2, 9)
    key = f'{dividend} {divisor} {dividend // divisor} {dividend % divisor}'
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f'{dividend}')
    child.sendline(f'{divisor}')
    helpers.assess(child, f'green1_19.py', key)

def green2_19(file):
    mathTable = [3, 16, 2, 2, 4]
    measurementTable = ['TEASPOONS', 'TABLESPOONS', 'CUPS', 'PINTS', 'QUARTS', 'GALLONS']
    quantity = random.randint(1, 50000)
    print(quantity)
    startUnit = random.choice(measurementTable)
    print(startUnit)
    endUnit = ''
    while True:
        endUnit = random.choice(measurementTable)
        if endUnit != startUnit:
            break
    print(endUnit)
    
    child = pexpect.spawnu(f'python3 {file}')
    print(f'{quantity} {startUnit} {endUnit}')
    child.sendline(f'{quantity} {startUnit} {endUnit}')
    
    if measurementTable.index(startUnit) > measurementTable.index(endUnit):
        test = True
        table = [endUnit, startUnit]
    else:
        test = False
        table = [startUnit, endUnit]
    
    start, end = table[0], table[1]
    
    index = measurementTable.index(start)
    
    if measurementTable.index(start) < measurementTable.index(end):
        while index != measurementTable.index(end):
            if test:
                quantity *= mathTable[index]
            else:
                quantity //= mathTable[index]
            index += 1
    print(quantity)
    helpers.assess(child, f'green2_19.py', str(quantity))
    

def green3_19(file):
    integer = random.randint(15, 99)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(integer))
    key = ''
    remainders = []
    while integer != 0:
        remainders.insert(0, str(integer % 2))
        key += f'{integer // 2} {integer % 2}\r\n'
        integer //= 2
    key += ''.join(remainders)
    helpers.assess(child, f'green3_19.py', key)

    
def green4_19(file): 
    child = pexpect.spawnu(f'python3 {file}')
    integer = random.randint(1, 1000000)
    child.sendline(str(integer))
    steps = 0
    while 1 != integer != 89:
        length = len(str(integer))
        total = 0
        for i in range(length):
            total += ((integer % 10) ** 2)
            integer //= 10
        integer = total
        steps += 1
    key = f'{integer} {steps}'
    helpers.assess(child, 'green4_19.py', key)
    
    
def green5_19(file):
    def checkBalanced(word, start1, end1, start2, end2):
        if leftCount > rightCount:
            return 'LEFT UNBALANCED'
        elif leftCount < rightCount:
            return 'RIGHT UNBALANCED'
        else:
            for each in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if word[start1 : end1].count(each) != word[start2 : end2].count(each):
                    return 'BALANCED'
        return 'PERFECTLY BALANCED'
    
    
    # generate keys
    keys = []
    alpha = [alpha for alpha in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    
    random.shuffle(alpha)
    mul1 = random.randint(1, 4)
    mul2 = random.randint(1, 4)
    
    # even perfectly balanced
    keys.append((alpha[0] * mul1 + alpha[1] * mul2) * 2)
    # odd perfectly balanced
    random.shuffle(alpha)
    keys.append(alpha[0] * mul1 + alpha[1] * mul2 + alpha[2] + alpha[0] * mul1 + alpha[1] * mul2)
    # even balanced
    random.shuffle(alpha)
    keys.append(alpha[0] * mul1 + alpha[1] * mul2 + alpha[2] * mul2 + alpha[3] * mul1)
    # odd balanced
    random.shuffle(alpha)
    keys.append(alpha[0] * mul1 + alpha[1] * mul2 + alpha[2] + alpha[3] * mul2 + alpha[4] * mul1)
    # left unbalanced
    random.shuffle(alpha)
    keys.append(alpha[0] + alpha[1] * 3 + alpha[2] + alpha[3] * 3 + alpha[1] * 4 + alpha[4] * 4)
    # right unbalanced
    random.shuffle(alpha)
    keys.append(alpha[0] * 2 + alpha[1] * 5 + alpha[2] + alpha[3] * 3 + alpha[1] * 2 + alpha[4])
    
    for each in keys:
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(each)
        word = each
        start1 = 0
        end1 = len(word) // 2
        end2 = len(word)
        if len(word) % 2 == 0:
            start2 = len(word) // 2
        else:
            start2 = len(word) // 2 + 1
        leftCount, rightCount = 0, 0
        for each in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if word[start1 : end1].count(each) > word[start2 : end2].count(each):
                leftCount += 1
            if word[start1 : end1].count(each) < word[start2 : end2].count(each):
                rightCount += 1
        key = checkBalanced(word, start1, end1, start2, end2)
        helpers.assess(child, 'green5_19.py', key)
    
