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

psets=('ch5_3.py' 'ch5_4.py' 'ch5_5.py' 'ch5_6.py' 'ch5_7.py' 'ch5_8.py' 'ch5_9.py' 'ch5_10.py'
       'ch5_11.py' 'ch5_12.py' 'ch5_13.py' 'ch5_14.py' 'ch5_15.py' 'ch5_16.py' 'ch5_17.py' 
       'ch5_18.py' 'ch5_19.py' 'ch5_20.py' 'ch5_20A.py' 'ch5_20B.py' 'ch5_20C.py' 'ch5_20D.py' '5_21.py' 'leftStack.py' 
       'rightStack.py' 'pyramidStacks.py')

echo 'updating testMe'
updateTestMe

for p in ${psets[@]}; do
    echo -e "${A}testMe"  $p ${X}
    testMe $p
done
