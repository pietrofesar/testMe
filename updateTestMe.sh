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
rm -r /home/testMeFolder
mkdir /home/testMeFolder

# download source files
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/sandBoxSolutions.py -O /home/testMeFolder/sandBoxSolutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch10Solutions.py -O /home/testMeFolder/ch10Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch1Solutions.py -O /home/testMeFolder/ch1Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch2Solutions.py -O /home/testMeFolder/ch2Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch3Solutions.py -O /home/testMeFolder/ch3Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch4Solutions.py -O /home/testMeFolder/ch4Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch5Solutions.py -O /home/testMeFolder/ch5Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch6Solutions.py -O /home/testMeFolder/ch6Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch7Solutions.py -O /home/testMeFolder/ch7Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch8Solutions.py -O /home/testMeFolder/ch8Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/helpers.py -O /home/testMeFolder/helpers.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/learningPythonSolutions.py -O /home/testMeFolder/learningPythonSolutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/siennaSolutions.py -O /home/testMeFolder/siennaSolutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.py -O /home/testMeFolder/testMe.py


#echo -e "${Y}Installing the updateTestMe utility${X}"
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/updateTestMe.sh -O /home/testMeFolder/updateTestMe.sh; sudo chmod +x /home/testMeFolder/updateTestMe.sh
sudo mv /home/testMeFolder/updateTestMe.sh /home/testMeFolder/updateTestMe

#echo -e "${Y}Installing the testMe utility${X}"
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe -O /home/testMeFolder/testMe.sh; sudo chmod +x /home/testMeFolder/testMe.sh
sudo mv /home/testMeFolder/testMe.sh /home/testMeFolder/testMe

bash testMe.sh
