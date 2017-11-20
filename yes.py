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
		confirmEmail.yes("Friday - " + str(friday), emailContact)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(option == "2"):
		confirmEmail.yes("Saturday - " + str(sat), emailContact)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(option == "3"):
		confirmEmail.yes("Sunday - " + str(sun), emailContact)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(option == "4"):
		print("\nWhat date is good for you?")
		yourDate = input("Enter Date: ")
		confirmEmail.yes(str(yourDate), emailContact)
		print("\nAwesome, can't wait to see you! Check your " + emailContact + " email for confirmation.\n")
	elif(option == "5"):
		exit()
	else:
		os.system("clear")
		main()

def main():
	yes(emailContact, emailContact)

if __name__ == "__main__":
	main()
