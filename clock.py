
#the user will interact with the program here.
time_now = int(input("Please enter the current hour: "))
wake_time = int(input("Please enter how many hours you wish to wake from now: "))

#Bam! Here the program does the work
while (wake_time >= 24):
   wake_time -= 24

time_now += wake_time

if (time_now > 13):
   print("You will wake up at", time_now-12, "PM.")
else:
   print("You will wake up at", time_now, "AM.")
   
#comments get turned red
int #notice how the keywords change color in the program
"int" # green usually represents a form of string.
'A' # green also represents characters
var_name # black text commonly represents variables
def #orange can also represent a keyword

