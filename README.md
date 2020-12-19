# INST326_Group313
## By Jake Stark, Rahele Eshete, and Henry Chau

# Repository
INST326_Group313.py : Main python file containing the project
test_cal.py : Test file for our program\
schedbeta.py : Python script we used to test various aspects of the program while we were writing the program\
SCHDULE_CSV.csv : An example of a schedule formated to be parsed by our code. This can be edited for your own schedule or you can create your own file from this format\
# **Program**
Our program is a calendar program that uses a CSV file to give you your schedule and help you edit, add, and remove events.\
\
In order to run the program just type **python INST326_Group313.py "filename.csv"**. This will give you a prompt to input commands. The commands are listed in the help function but are here as well:\
\
schedule: Schedule will give you events for a day\
add: Add will alow for you to add an event to you calendar\
edit: Edit allows for you to edit an already existing event\
remove: Remove will let you remove an event\
exit: Will exit the program\
\
Based on the command, you will be asked for certain inputs in order to complete the task. The inputs will have prompts explaining exactly what to input. The program will keep taking commands until "exit" is typed to exit the program. At that point the program will update your csv to reflect the changes made and end.
