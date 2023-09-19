#!/bin/bash
# Author: Rocco Pietrofesa
# Date: 9/5/19
# python autograder installer script

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

echo -e "${Y}This will update the current Amazon Linux OS${X}"
sudo yum update -y

echo -e "${G}Current version of Python:"
python3 --version
echo -e "${X}"

echo -e "${Y}Installing pip${X}"
curl -O https://bootstrap.pypa.io/get-pip.py # Get the install script.
python3 get-pip.py --user                       # Install pip.
rm get-pip.py                                # Delete the install script.

export PATH=$PATH:/usr/local/bin

echo -e "${G}Current version of pip:"
pip3 --version
echo -e "${X}"


echo -e "${Y}Installing the pexpect package${X}"
pip3 install pexpect --user
echo -e "${G}Current version of pexpect:"
pip3 show pexpect
echo -e "${X}"

echo -e "${Y}Installing the numpy package${X}"
pip3 install numpy --user
echo -e "${G}Current version of numpy:"
pip3 show numpy
echo -e "${X}"


echo -e "${Y}Installing the Python autograder testMe source file${X}"
# make folder for files
sudo mkdir /usr/bin/testMeFolder
# download source files
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/sandBoxSolutions.py -O /usr/bin/testMeFolder/sandBoxSolutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch10Solutions.py -O /usr/bin/testMeFolder/ch10Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch1Solutions.py -O /usr/bin/testMeFolder/ch1Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch2Solutions.py -O /usr/bin/testMeFolder/ch2Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch3Solutions.py -O /usr/bin/testMeFolder/ch3Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch4Solutions.py -O /usr/bin/testMeFolder/ch4Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch5Solutions.py -O /usr/bin/testMeFolder/ch5Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch6Solutions.py -O /usr/bin/testMeFolder/ch6Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch7Solutions.py -O /usr/bin/testMeFolder/ch7Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/ch8Solutions.py -O /usr/bin/testMeFolder/ch8Solutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/helpers.py -O /usr/bin/testMeFolder/helpers.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/learningPythonSolutions.py -O /usr/bin/testMeFolder/learningPythonSolutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/siennaSolutions.py -O /usr/bin/testMeFolder/siennaSolutions.py
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.py -O /usr/bin/testMeFolder/testMe.py

echo -e "${Y}Installing the updateTestMe utility${X}"
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/updateTestMe -O /usr/bin/updateTestMe; sudo chmod +x /usr/bin/updateTestMe 

echo -e "${Y}Installing the testMe utility${X}"
sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe -O /usr/bin/testMe; sudo chmod +x /usr/bin/testMe

testMe

echo -e "${Y}Removing installTestMe script${X}"

rm -- "$0"
