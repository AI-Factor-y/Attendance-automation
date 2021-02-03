
## this code is written and managed by abhinav -p (@_ai_factory) 
## abhinavhariharan2001@gmail.com

days=["monday","tuesday","wednesday","thursday","friday"];

#active classes are those classes for which you have to put attendance
#only those classes in the timetable which are in the active classes are considered by the
#automation script

#classes not in active classes are ignored by the script

active_classes=["co","math","dsa","hwl"];


#timetable data with timetable format [[hour,minute],"subject_name"]
#order of slots doesn't matter .
#give the time of slot as the time when the link for attendance comes in the eduserver 
#for that specific course

timetable=[
	["monday",     [[8,0],"free"]  ,   [[8,56],"co"] ,  [[10,10],"free"],   [[11,6],"math"],  [[13,0],"free"],  [[14,0],"env"] ],

	["tuesday",    [[8,0],"math"]  ,   [[9,0],"env"] ,[[10,15],"dsa"]   ,[[11,15],"free"],[[13,0],"free"],  [[14,0],"dsal"] ],

	["wednesday",  [[8,0],"free"]  ,   [[9,0],"free"], [[10,11],"co"]   ,[[11,15],"free"],  [[13,0],"free"],  [[14,0],"valueed"] ],

	["thursday",   [[8,0],"free"]  ,   [[20,21],"math"] ,  [[10,15],"env"] ,[[11,8],"dsa"], [[13,0],"free"], [[13,56],"hwl"] ],

	["friday",     [[7,56],"dsa"]  ,   [[9,0],"free"] ,  [[10,15],"free"] ,[[11,11],"co"],   [[13,0],"free"], [[14,0],"valueed"] ]

]

#provide the url for the course attandace page.. 
#its the address that we obtain from the address bar when we open the attendance section in
#eduserver for a course

# format ===> https://eduserver.nitc.ac.in/mod/attendance/view.php?id=$$$$$

course_web_url={
	
	"co": "https://eduserver.nitc.ac.in/mod/attendance/view.php?id=28943",

	"math": "https://eduserver.nitc.ac.in/mod/attendance/view.php?id=26861",

	"dsa" : "https://eduserver.nitc.ac.in/mod/attendance/view.php?id=28265",
	"hwl" :"https://eduserver.nitc.ac.in/mod/attendance/view.php?id=28300"
}

