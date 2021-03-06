#!/bin/sh

# text color constants
R='\033[0;31m'    # red
BR='\033[1;31m'   # bold red
G='\033[0;32m'    # green
BG='\033[1;32m'   # bold green
Y='\033[0;33m'    # yellow
BY='\033[1;33m'   # bold yellow
B='\033[0;34m'    # blue
BB='\033[1;34m'   # bold blue
P='\033[0;35m'    # purple
BP='\033[1;35m'   # bold purple
A='\033[0;36m'    # aqua
BA='\033[1;36m'   # bold aqua
X='\033[0m'       # reset

psets=('whileLoop1.py' 'whileLoop2.py' 'whileLoop3.py' 'whileLoop4.py' 'whileLoop5.py' 'whileLoop6.py' 'ch5_20A.py' 'ch5_20B.py' 'ch5_20C.py' 'leftStack.py' 
       'rightStack.py' 'pyramidStacks.py' 'forLoop1.py' 'forLoop2.py' 'forLoop3.py' 'forLoop4.py' 'forLoop5.py' 'forLoop6.py' 'forLoop7.py')

echo 'updating testMe'
updateTestMe

for p in ${psets[@]}; do
    echo -e "${A}testMe"  $p ${X}
    testMe $p
done
