# homework3_hri TERMINAL DIRECTIONS
======================================================================================================
IN TERMINAL 1:

cd ~/hri_course_ws
source devel/setup.bash
roslaunch homework3 homework3.launch
======================================================================================================
IN TERMINAL 2:

cd ~/hri_course_ws
source devel/setup.bash
rostopic list

(HIT ENTER)
======================================================================================================



PROMTS:
======================================================================================================
======================================================================================================
"ADD TASK" PROMPT (PASTE IN TERMINAL 2):

(CHANGE "ASSIGNMENT" to other names: "QUIZ 3," "PROJECT 5," "FINAL EXAM," etc.)

rostopic pub -1 /dialogflow_client/requests/string_msg std_msgs/String "data: 'add ASSIGNMENT'"
======================================================================================================
"SHOW TASKS" PROMPT (PASTE IN TERMINAL 2):

(CHANGE "show my tasks" to other names: "what do i have to do?," "to do," etc.)

rostopic pub -1 /dialogflow_client/requests/string_msg std_msgs/String "data: 'show my tasks'"
======================================================================================================
"DELET TASK" PROMPT (PASTE IN TERMINAL 2):

(CHANGE "delete homework 3" to other names: "remove QUIZ 3," "delete PROJECT 5," etc.)

rostopic pub -1 /dialogflow_client/requests/string_msg std_msgs/String "data: 'delete homework 3'"
======================================================================================================
======================================================================================================
