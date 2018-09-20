import os
import sys
import pexpect

def script_usage():
 print("Usage: " + os.path.basename(sys.argv[0]) + " <system1_ip>" + " <system2_ip> ")
 return

if len(sys.argv) < 2:
    script_usage()
    sys.exit()

system1_ip = sys.argv[1]
sys2_ip = sys.argv[2]

child = pexpect.spawn('ssh radius @192.168.51.222')
#child.expect('password:', timeout=120)
child.sendline('t35ting')
#child.expect ('prompt# ')
if os.system("ping -c 5 google.com") == 0:
   print "google is pinging"

