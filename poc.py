#Required modules

import sys
import urllib.request
import os

#url for testing  = http://testphp.vulnweb.com/listproducts.php?cat=1

url = ""

#Script usage function

try:

	if len(sys.argv) != 2 :
		print(" [+] usage : python poc.py <username>")
		print(" [+] Help : poc.py --help or -h")
	elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
		print(" [+] This script is created by Xro0T ")
		print(" [+] This script was written in Python")
		print(" [+] This script helps you to find SQL vulnerability in website")
	else:
		url = sys.argv[1]
except:
	print("")

#Generating SQL error 

NewURL = url+"\'"
report = ''
#Checking that a website is vulnerable or not

try :
	x = str(urllib.request.urlopen(NewURL).read())
	if x.find('You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near') != -1:
		print(' [+] SQL injection found')
		report='YES'
	else:
		print(' [+] Not vulnerable')
		report='NO'
except:
	print("")

if report == 'YES':
	
	f = open('report.txt', 'w')
	f.write(' [+] SQL injection : YES [+] ')

else:
    
	f = open('report.txt', 'w')
	f.write(' [+] SQL injection : NO [+] ')