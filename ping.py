import os

if os.system("ping -c 5 google.com") == 0:
   print "google is pinging"
