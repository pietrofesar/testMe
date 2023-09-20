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
rm -r ~/testMe
mkdir ~testMe

# make folder for files
mkdir ~/testMe

# add path for scripts
export PATH=$PATH:/~/testMe

# download source files
curl --output ~/testMe/sandBoxSolutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/sandBoxSolutions.py"
curl --output ~/testMe/ch10Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch10Solutions.py"
curl --output ~/testMe/ch1Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch1Solutions.py"
curl --output ~/testMe/ch2Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch2Solutions.py"
curl --output ~/testMe/ch3Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch3Solutions.py"
curl --output ~/testMe/ch4Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch4Solutions.py"
curl --output ~/testMe/ch5Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch5Solutions.py"
curl --output ~/testMe/ch6Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch6Solutions.py"
curl --output ~/testMe/ch7Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch7Solutions.py"
curl --output ~/testMe/ch8Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch8Solutions.py"
curl --output ~/testMe/helpers.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/helpers.py"
curl --output ~/testMe/learningPythonSolutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/learningPythonSolutions.py"
curl --output ~/testMe/siennaSolutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/siennaSolutions.py"
curl --output ~/testMe/testMe.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.py"


echo -e "${Y}Installing the updateTestMe utility${X}"
curl --output ~/testMe/updateTestMe.sh "https://raw.githubusercontent.com/pietrofesar/testMe/main/updateTestMe.sh"
chmod +x ~/testMe/updateTestMe.sh
#mv ~/testMe/updateTestMe.sh ~/testMe/updateTestMe

echo -e "${Y}Installing the testMe utility${X}"
curl --output ~/testMe/testMe.sh "https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.sh" 
chmod +x ~/testMe/testMe.sh
#mv ~/testMe/testMe.sh ~/testMe/testMe

bash testMe.sh
