#!/bin/bash

sudo rm /usr/bin/updateTestMe 

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

echo -e "${Y}Collecting and removing testMe 2.0.0${X}"
sudo rm -r /usr/bin/testMe
sudo rm -r /usr/bin/updateTestMe
sudo rm -r /usr/bin/check.py


echo -e "${Y}Collecting and installing testMe 3.0.0.${X}"

sudo wget -q  wget https://raw.githubusercontent.com/pietrofesar/testMe/main/installTestMe.sh -O updateTestMe

sudo bash installTestMe.sh

rm -- "$0"
