import time as t
import pyautogui as p
import datetime
from colorama import init, Fore, Back, Style
init()

no = 0

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

def plsbal():
	p.write("pls bal")
	p.press("enter")
	print(f'{getTime() + Style.BRIGHT + Fore.GREEN} Pls balance!{Style.RESET_ALL}')

def plsbeg():
	p.write("pls beg")
	p.press("enter")
	print(f'{getTime() + Style.BRIGHT + Fore.GREEN} Pls beg!{Style.RESET_ALL}')

def plsbet():
	p.write("pls bet 150") # Modify this number according to the risk that you want for bets.
	p.press("enter")
	print(f'{getTime() + Style.BRIGHT + Fore.MAGENTA} Pls bet!{Style.RESET_ALL}')

def plsdeposit():
	p.write("pls dep 500")
	p.press("enter")
	print(f'{getTime() + Style.BRIGHT + Fore.GREEN} Trying to deposit 500 coins!{Style.RESET_ALL}')

def plsdaily():
	p.write("pls daily")
	p.press("enter")
	print(f'{getTime() + Fore.BLUE} Trying to pick daily bonus...{Style.RESET_ALL}')

def plslottery():
	p.write("pls lottery")
	p.press("enter")
	t.sleep(2)
	p.write("yes")
	p.press("enter")
	print(f'{getTime() + Fore.BLUE} Trying to enter lottery...{Style.RESET_ALL}')

def plswork():
	t.sleep(2)
	p.write("pls work")
	p.press("enter")
	print(f'{getTime() + Fore.BLUE} Trying to work...{Style.RESET_ALL}')

print(f'{getTime() + Style.BRIGHT + Fore.CYAN} Started!\nWaiting 5 seconds...\n{Style.RESET_ALL}')
t.sleep(5)
plsbal()
plsdaily()

# You can change this as you want!
while True:
	plslottery()
	plswork()
	for i in range(30):
		for i in range(3):
			if no == 8: # Increase or decrease this number in order to change the frequency of bets [Higher number = Less bets].
				plsbeg()
				for i in range(3):
					plsbet()
					t.sleep(10.4)
				t.sleep(10)
				no = 0
			else:
				plsbeg()
				t.sleep(40.4)
			no += 1
		plsdeposit()
