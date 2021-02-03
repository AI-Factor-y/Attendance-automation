###### this code is written by Abhinav -p (@_ai_factory) ######
### abhinavhariharan2001@gmail.com ###

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import timetable as tb
import datetime
import time 

# timetable information to be supplied in timetable.py file 

#personal information to be filled-----------!!

login_username="your eduserver username"
login_password="your eduserver password"

#--------------------------------------------!!

#main timetable data
arr=tb.timetable

# globals
curr_time=0   		# variable for accessing the current time
day_indx=0			# index of the day monday has index 0
length_of_day=0		# the total sessions on the day
non_working_day=False;
prev_slot="none"

# the code tries to put the attendance for some attempts if it fails at its first attempt
# this can happen if the link is unavailable or the slot is changed.
# each attempt is done after a 10second delay inorder to wait for the link

max_attempts=10      #maximum number of attempts till completion

rotate_animation =0
rot_anim='|'

def put_attendance(sub_id,sub_code):
	global max_attempts,login_username,login_password
	attendance_marked=False
	attempts=0
	while(attendance_marked==False and attempts<max_attempts):
		browser = webdriver.Chrome()

		browser.get("https://eduserver.nitc.ac.in/")

		try:
			
			username = browser.find_element_by_id("username")

			password = browser.find_element_by_id("password")
			username.send_keys(login_username)
			password.send_keys(login_password)

			browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/button').click()

			browser.get(sub_code)
	
			browser.find_element_by_partial_link_text("Submit attendance").click()

			time.sleep(2);
			x=browser.find_elements_by_xpath("//*[contains(text(), 'Present')]")

			# print(x)
			time.sleep(1)
			x[0].click()
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
			time.sleep(0.5)
			attendance_marked=True
		except:
			print("trying again..")
			time.sleep(10)
			attempts+=1
			print(f"---> attempt : {attempts} <---")

		browser.quit();
	if(attempts>=max_attempts):
		print(f"link unavailable after {max_attempts} attempts.. skipping")
		attendance_marked=True

def rotate_animation_init():

	global rotate_animation,rot_anim

	rot_anim='|'
	if(rotate_animation>50):
		rot_anim='/'
	
	if(rotate_animation>100):
		rot_anim='-'
	if(rotate_animation>150):
		rot_anim="\\"
	if(rotate_animation>200):
		rot_anim='|'
		rotate_animation=0
	rotate_animation+=3

def init_day():
	global curr_time,day_indx,length_of_day,non_working_day,rot_anim

	x = datetime.datetime.now()
	# print(x)
	curr_time=[int(x.hour),int(x.minute)]

	day=x.strftime("%A").lower();
	os.system("cls");

	# day="monday"; # change after
	rotate_animation_init()

	print("________ automation status : running "+rot_anim+"  ________\n")
	print(f'current time | {curr_time[0]} : {curr_time[1]} : {x.second}')
	print("day          | "+day)

	if(day in tb.days):
		non_working_day=False;
		day_indx=tb.days.index(day);
		length_of_day = len(arr[day_indx])
	else:
		non_working_day=True;

	




def event_driver():
	global prev_slot
	while True:
		init_day() # initialise the current day 

		if(non_working_day): #check if the day is a working day or not
			continue

		
		for i in range(1,length_of_day):

			block=arr[day_indx][i]

			hours_curr=curr_time[0]
			min_curr=curr_time[1]

			if(block[0][0]==hours_curr and block[0][1]==min_curr):
				attendance_to=block[1]
				print("\ntimetable slot found ...")
				print(f'current active slot  | {attendance_to}\n');
				print("=========================================")
				curr_slot=attendance_to
				if(curr_slot==prev_slot):
					continue

				if(attendance_to not in tb.active_classes):
					continue

				
				id_path=tb.course_web_url[attendance_to]
				
				put_attendance(attendance_to,id_path)
				
				
				prev_slot=curr_slot
			

				
	
	
# // main

event_driver()


##   sleep peacefully
## :) :) :) *-* :( :( :(