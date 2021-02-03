# Attendance-automation
A python script for attendance automation in the eduserver for nitc


External libraries used
-----------------------
1: selenium

how to install selenium
-----------------------
pip install selenium

how to run script
-----------------
python auto.py

important information regarding selenium
----------------------------------------
the code uses the chrome driver for automating the web browser . 
make sure you have chrome installed and running on your pc
install a chrome driver from https://chromedriver.chromium.org/downloads

whats inside
-------------
1. timetable.py

contains data for timetable and links
timetable data with timetable format [[hour,minute],"subject_name"]
order of slots doesn't matter .
give the time of slot as the time when the link for attendance comes in the eduserver 

2. auto.py

main script file
provide user details here
you can change the working of the script from here

important parameters in auto.py
------------------------------
1:login_username 

2:login_password

3:max_attempts : max number of retry 


about this script
-----------------
this code is written by abhinav -p . It is still under development so proceed at your own risk.

licensed under [![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/AI-Factor-y/Attendance-automation/blob/main/LICENSE)

any contribution to this code will be helpfull please feel free to commit
