#!/bin/bash

: '
 Author: Rocco Pietrofesa
 Date: 9/2/19
 updateTestMe script
 This script will fetch and overwrite the latest version of the python autograder
 
 need to create a version checker for the autograder
'

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
echo -e "${Y}Collecting and overwriting testMe Python autograder utility.${X}"
rm -r testMe
mkdir testMe
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/sandBoxSolutions.py -O testMe/sandBoxSolutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch10Solutions.py -O testMe/ch10Solutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch1Solutions.py -O testMe/ch1Solutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch2Solutions.py -O testMe/ch2Solutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch3Solutions.py -O testMe/ch3Solutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch4Solutions.py -O testMe/ch4Solutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch5Solutions.py -O testMe/ch5Solutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch6Solutions.py -O testMe/ch6Solutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch7Solutions.py -O testMe/ch7Solutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch8Solutions.py -O testMe/ch8Solutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/helpers.py -O testMe/helpers.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/learningPythonSolutions.py -O testMe/learningPythonSolutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/siennaSolutions.py -O testMe/siennaSolutions.py
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.py -O testMe/testMe.py

rm updateTestMe.sh 
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/updateTestMe.sh -O updateTestMe.sh
rm testMe.sh 
wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.sh -O testMe.sh

bash testMe.sh
