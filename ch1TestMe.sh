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

psets=('ch1_1.py' 'ch1_2.py' 'ch1_3.py' 'ch1_4.py' 'ch1_5.py' 'ch1_6.py')
echo 'updating testMe'
updateTestMe

for p in ${psets[@]}; do
    echo -e "${A}testMe"  $p ${X}
    testMe $p
done
