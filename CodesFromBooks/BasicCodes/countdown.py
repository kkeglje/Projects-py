#!/usr/bin/python3
# countdown.py- Simple countdown script

import time,subprocess

timeLeft = 60
while timeLeft>0:
    print(timeLeft,end='')
    time.sleep(1)
    timeLeft-=1

subprocess.Popen(['start','alarm.wav'],shell=True)
