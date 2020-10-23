import random

a = random.randint(0, 20)
b = random.randint(0, 20)


answer = eval(input(f'What is {a} x {b}? '))

if answer == a * b:
    print(f'{a} x {b} = {answer} is correct')
    
else:
    print(f'{a} x {b} = {answer} is incorrect')
