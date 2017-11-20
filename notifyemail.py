import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import systeminfo

with open('auth.txt') as f:
  credentials = [x.strip().split(':') for x in f.readlines()]

for username,password in credentials:
	userGlob = username
	passGlob = password

MY_ADDRESS = userGlob
PASSWORD = passGlob

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
	    for a_contact in contacts_file:
		    names.append(a_contact.split()[0])
	    emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
	    template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    systeminfo.systemFunc()
    names, emails = get_contacts('notifycontacts.txt') # read contacts
    message_template = read_template('notifymessage.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()

	# add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

	# setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Ask a Girl Program - Has Been Ran"

	# add in the message body
        msg.attach(MIMEText(message, 'plain'))

	# send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
	main()
