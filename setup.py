import os
import ask
import sys

def smtpInstall():
	try:
		import smtplib
		print("smtplib already installed")
	except ImportError:
		print("Installing smtplib")
		os.system("pip install smtplib")

def subprocessInstall():
	try:
		import subprocess
		print("subprocess already installed")
	except ImportError:
		print("Installing subprocess")
		os.system("pip install subprocess")
		

def socketInstall():
	try:
		import socket
		print("socket already installed")
	except ImportError:
		print("Installing socket")
		os.system("pip install socket")

def datetimeInstall():
	try:
		import datetime
		print("datetime already installed")
	except ImportError:
		print("Installing datetime")
		os.system("pip install datetime")

def main():

	total = len(sys.argv)
	if total != 2:
		print("Error need two command line arguments")
		print("Usage: python setup.py [your email address]")
		exit()
	
	emailContact = str(sys.argv[1])

	smtpInstall()
	subprocessInstall()
	socketInstall()
	datetimeInstall()

	os.system("clear")

	ask.main(emailContact)

if __name__ == "__main__":
	main()
	








