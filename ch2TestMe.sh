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

psets=('ch2_1.py' 'ch2_2.py' 'ch2_3.py' 'ch2_5.py' 'ch2_6.py' 'ch2_7.py' 'ch2_8.py' 'ch2_9.py'
       'ch2_10.py' 'ch2_11.py' 'ch2_13.py' 'ch2_14.py' 'ch2_15.py' 'ch2_16.py' 'ch2_17.py' 
       'ch2_18.py' 'ch2_19.py' 'ch2_20.py' 'ch2_21.py')

echo 'updating testMe'
updateTestMe

for p in ${psets[@]}; do
    echo -e "${A}testMe"  $p ${X}
    testMe $p
done
