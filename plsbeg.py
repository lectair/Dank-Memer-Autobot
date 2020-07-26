import time as t
import pyautogui as p
import datetime
from colorama import init, Fore, Back, Style
init()

def getTime():
    now = datetime.datetime.now()
    if now.hour < 10:
        hours = '0'+str(now.hour)
    else:
        hours = now.hour
    if now.minute < 10:
        minutes = '0'+str(now.minute)
    else:
        minutes = now.minute
    if now.second < 10:
        seconds = '0'+str(now.second)
    else:
        seconds = now.second
    time = Fore.YELLOW+'['+str(hours)+':'+str(minutes)+':'+str(seconds)+']'+Style.RESET_ALL
    return time

no = 1
print(f'{getTime()} Started!\nWaiting 5 seconds...\n')
t.sleep(5)
while True:
	if no == 3:
		p.write("pls beg")
		p.press("enter")
		print(f'{getTime()} Pls beg!')
		for i in range(3):
			p.write("pls bet 150")
			p.press("enter")
			print(f'{getTime()} Pls bet!')
			t.sleep(10.15)
		t.sleep(10)
		no = 1
	else:
		p.write("pls beg")
		p.press("enter")
		print(f'{getTime()} Pls beg!')
		t.sleep(40.15)
	no += 1
