import os

loop = 1
while loop == 1:
   ip = "10.26.0.159"
   os.system("ping "+ str(ip) + " -t -l 65500")
