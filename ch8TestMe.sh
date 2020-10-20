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

psets=('ch8_1.py' 'ch8_2.py' 'ch8_3.py' 'ch8_4.py' 'ch8_5.py' 'ch8_6.py' 'ch8_7.py' 'ch8_8.py'
       'ch8_11.py' 'ch8_12.py' 'ch8_13.py' 'checkPalindrome.py' 'rockPapersScissors.py')

echo 'updating testMe'
updateTestMe

for p in ${psets[@]}; do
    echo -e "${A}testMe"  $p ${X}
    testMe $p
done
