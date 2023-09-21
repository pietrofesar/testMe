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

# constant for destination folder
HOME=$PWD/testMe

# make folder for files
mkdir $HOME

#echo -e "${Y}This will update the current Amazon Linux OS${X}"
#sudo yum update -y

echo -e "${G}Current version of Python:"
python3 --version
echo -e "${X}"

echo -e "${Y}Installing pip${X}"
curl -O https://bootstrap.pypa.io/get-pip.py # Get the install script.
python3 get-pip.py --user                       # Install pip.
rm get-pip.py                                # Delete the install script.

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

# add path for scripts - need to update global path
export PATH=$PATH:$HOME

# download source files
curl --output $HOME/sandBoxSolutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/sandBoxSolutions.py"
curl --output $HOME/ch10Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch10Solutions.py"
curl --output $HOME/ch1Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch1Solutions.py"
curl --output $HOME/ch2Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch2Solutions.py"
curl --output $HOME/ch3Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch3Solutions.py"
curl --output $HOME/ch4Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch4Solutions.py"
curl --output $HOME/ch5Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch5Solutions.py"
curl --output $HOME/ch6Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch6Solutions.py"
curl --output $HOME/ch7Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch7Solutions.py"
curl --output $HOME/ch8Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch8Solutions.py"
curl --output $HOME/helpers.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/helpers.py"
curl --output $HOME/learningPythonSolutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/learningPythonSolutions.py"
curl --output $HOME/siennaSolutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/siennaSolutions.py"
curl --output $HOME/testMe.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.py"


echo -e "${Y}Installing the updateTestMe utility${X}"
curl --output $HOME/updateTestMe.sh "https://raw.githubusercontent.com/pietrofesar/testMe/main/updateTestMe.sh"
chmod +x $HOME/updateTestMe.sh
#mv $HOME/updateTestMe.sh $HOME/updateTestMe

echo -e "${Y}Installing the testMe utility${X}"
curl --output $HOME/testMe.sh "https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.sh" 
chmod +x $HOME/testMe.sh
#mv $HOME/testMe.sh $HOME/testMe


echo -e "${Y}Removing installTestMe script${X}"

#rm -- "$0"
