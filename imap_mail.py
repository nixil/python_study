__author__ = 'xinli'

import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('alexleebiti@gmail.com', 'nixilgmail112358')
mail_list = mail.list()

mail.select('inbox')

result, data = mail.search(None, "ALL")

ids = data[0]

id_list = ids.split()
print "Now you have " + str(len(id_list)) + " emails."
latest_email_id = id_list[-1]

result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]

print raw_email
