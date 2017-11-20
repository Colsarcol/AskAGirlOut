import datetime
import socket
import subprocess

def systemFunc():

	curTime = datetime.datetime.now()

	writeTime = curTime.strftime("%Y-%m-%d %H:%M") #Current date and time
	writeHostName = socket.gethostname() #Hostname of machine
	writeInIp = socket.gethostbyname(socket.gethostname()) #Internal Network IP
	writeWhoAmI = str(subprocess.check_output(['whoami']))
	writeWhoAmI = writeWhoAmI.replace("b", "")
	writeWhoAmI = writeWhoAmI.replace("'", "")

	f = open('notifymessage.txt', 'w')
	f.write("""
	System Information:

	Current Time: """  +  writeTime + """
	Internal IP: """ + writeInIp + """
	Hostname: """ + writeHostName + """
	Who am I: """ + writeWhoAmI + """

	""")  # python will convert \n to os.linesep
	f.close() 

if __name__ == '__main__':
	systemFunc()
