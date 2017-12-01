import os
import splash
import yes, no, maybe
import notifyemail
import confirmEmail

emailContact = ""

def questionFun(emailContact):
	emailContact = emailContact
	print("""
	  _  _                _                   _                    _     _              _   
	 | || |_____ __ __   | |_ ___     __ _ __| |__   __ _     __ _(_)_ _| |    ___ _  _| |_ 
	 | __ / _ \ V  V /   |  _/ _ \   / _` (_-< / /  / _` |   / _` | | '_| |   / _ \ || |  _|
	 |_||_\___/\_/\_/     \__\___/   \__,_/__/_\_\  \__,_|   \__, |_|_| |_|   \___/\_,_|\__|
	                                                         |___/                          
	""")

	answer = input("Will you go on a date? \n(yes, no, maybe): ")
	
	answer = answer.lower()
	if answer == "yes" or answer == "y":
		yes.yes(emailContact)
	elif answer == "no" or answer == "n":
		no.no(emailContact)
	elif answer == "maybe" or answer == "m":
		maybe.maybe(emailContact)
	else:	
		confirmEmail.ians(emailContact)
		os.system("clear")
		print('Not a valid answer, please try again')
		questionFun(emailContact)

def main(emailContact):
	emailContact = emailContact
	print("Checking Dependencies... One Minute Please")
	notifyemail.main()
	os.system("clear")
	splash.splashScreen()
	questionFun(emailContact)

if __name__ == "__main__":
    main(emailContact)
