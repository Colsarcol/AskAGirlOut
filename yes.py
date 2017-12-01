import os
import confirmEmail
import datetime

today = datetime.date.today()
friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
sat = today + datetime.timedelta((5-today.weekday()) % 7)
sun = today + datetime.timedelta((6-today.weekday()) % 7)
emailContact = ""

def yes(emailContact):
	emailContact = emailContact
	print("")
	print("When is best for you!")
	print("")
	print("1) Friday " + str(friday))
	print("2) Saturday " + str(sat))
	print("3) Sunday " + str(sun))
	print("4) Another date is better!")
	print("5) Exit")
	print("")
	option = input("Option (1, 2, 3, 4 or 5): ")
	option = str(option)
	if(option == "1"):
		dateStr = "Friday - " + str(friday)
		time(emailContact, dateStr)
	elif(option == "2"):
		dateStr = "Saturday - " + str(sat)
		time(emailContact, dateStr)
	elif(option == "3"):
		dateStr = "Sunday - " + str(sun)
		time(emailContact, dateStr)
	elif(option == "4"):
		print("\nWhat date is good for you?")
		yourDate = input("Enter Date: ")
		dateStr = str(yourDate)
		time(emailContact, dateStr)
	elif(option == "5"):
		exit()
	else:
		os.system("clear")
		main()

def time(emailContact, dateStr):
	dateStr = dateStr
	emailContact = emailContact
	print("\nWhat time is best to meet on " + dateStr + "\n")
	print("1) 5 pm")
	print("2) 6 pm")
	print("3) 7 pm")
	print("4) 8 pm")
	print("5) 9 pm")
	print("6) 10 pm")
	print("7) Exit")
	optionTime = input("\nOption (1, 2, 3, 4, 5, 6 or 7): ")
	optionTime = str(optionTime)
	
	if(optionTime == "1"):
		timeVar = "5 PM"
		confirmEmail.yes(dateStr, emailContact, timeVar)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(optionTime == "2"):
		timeVar = "6 PM"
		confirmEmail.yes(dateStr, emailContact, timeVar)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(optionTime == "3"):
		timeVar = "7 PM"
		confirmEmail.yes(dateStr, emailContact, timeVar)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(optionTime == "4"):
		timeVar = "8 PM"
		confirmEmail.yes(dateStr, emailContact, timeVar)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(optionTime == "5"):
		timeVar = "9 PM"
		confirmEmail.yes(dateStr, emailContact, timeVar)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(optionTime == "6"):
		timeVar = "10 PM"
		confirmEmail.yes(dateStr, emailContact, timeVar)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(optionTime == "7"):
		exit()
	else:
		print("Invalid command, please restart the program")
		exit()

def main():
	yes(emailContact)

if __name__ == "__main__":
	main()
