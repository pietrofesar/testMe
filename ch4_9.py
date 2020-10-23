weight1, price1 = eval(input('Enter the weight and price for package 1: '))
weight2, price2 = eval(input('Enter the weight and price for package 2: '))

unitCost1 = price1 / weight1
unitCost2 = price2 / weight2

print(f'package 1: ${unitCost1:.2f}')
print(f'package 2: ${unitCost2:.2f}')

if unitCost1 < unitCost2:
    print('Package 1 has a better price.')
elif unitCost1 > unitCost2:
    print('Package 2 has a better price.')
else:
    print('They are the same price.')
    
