import os
import ask
import confirmEmail

emailContact = ""

def maybe(emailContact):
	os.system("clear")
	print("\nMaybe? I like these odds, but umm lets go with a yes or no this time!")
	ask.questionFun(emailContact)	
	confirmEmail.maybe(emailContact)

def main():
	maybe(emailContact)

if __name__ == "__main__":
	main()
