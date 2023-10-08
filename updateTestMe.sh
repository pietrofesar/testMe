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

# location of grader files
filePath=$PWD/testMe
# echo $filePath

# remove all previous files
rm -r $filePath/*

# create directory for new files
# mkdir $filePath

# add path for scripts
# export PATH=$PATH:/$filePath

# download source files
curl --output $filePath/sandBoxSolutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/sandBoxSolutions.py"
curl --output $filePath/ch10Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch10Solutions.py"
curl --output $filePath/ch1Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch1Solutions.py"
curl --output $filePath/ch2Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch2Solutions.py"
curl --output $filePath/ch3Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch3Solutions.py"
curl --output $filePath/ch4Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch4Solutions.py"
curl --output $filePath/ch5Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch5Solutions.py"
curl --output $filePath/ch6Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch6Solutions.py"
curl --output $filePath/ch7Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch7Solutions.py"
curl --output $filePath/ch8Solutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/ch8Solutions.py"
curl --output $filePath/helpers.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/helpers.py"
curl --output $filePath/learningPythonSolutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/learningPythonSolutions.py"
curl --output $filePath/siennaSolutions.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/siennaSolutions.py"
curl --output $filePath/testMe.py "https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.py"


echo -e "${Y}Installing the updateTestMe utility${X}"
curl --output $filePath/updateTestMe.sh "https://raw.githubusercontent.com/pietrofesar/testMe/main/updateTestMe.sh"
chmod +x $filePath/updateTestMe.sh
mv $filePath/updateTestMe.sh $filePath/updateTestMe

echo -e "${Y}Installing the testMe utility${X}"
curl --output $filePath/testMe.sh "https://raw.githubusercontent.com/pietrofesar/testMe/main/testMe.sh" 
chmod +x $filePath/testMe.sh
mv $filePath/testMe.sh $filePath/testMe

testMe
