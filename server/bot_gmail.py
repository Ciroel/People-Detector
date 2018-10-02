# Import smtplib for the actual sending function
import smtplib
import os
# import subprocess

# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Lost people detected'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = 'people.detector.bot@gmail.com'
msg['To'] = COMMASPACE.join(['people.detector.bot@gmail.com'])
msg.preamble = 'People detected!'

# Assume we know that the image files are all in PNG format
for file in ['predictions.jpg']:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
    fp = open(file, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)

# subprocess.call("cp /Users/asm/darknet/predictions.jpg /Users/asm/Projects/Django/mysite/polls/static/polls/predictions2.jpg")
os.system("cp /Users/asm/darknet/predictions.jpg /Users/asm/Projects/Django/mysite/polls/static/polls/predictions_0.jpeg")
# Send the email via our own SMTP server.
# s = smtplib.SMTP('')
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("people.detector.bot@gmail.com", "PeopleDetector111")
server.sendmail([msg['From']], [msg['To']], msg.as_string())
server.quit()
