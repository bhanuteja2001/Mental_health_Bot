import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Response



class GMailClient:
    def sendEmail(self,contact_email):
        #EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        #EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        EMAIL_ADDRESS = 'bhanutejakurakula@gmail.com'

        #contacts = ['dineshraturi22@gmail.com']

        msg = MIMEMultipart()
        msg['Subject'] = 'Info:'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = contact_email

        msg['Subject'] = "This will contain attachment"

        body = "Open this File"

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "projects.txt"
        attachment = open(filename, "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(EMAIL_ADDRESS, "gzhjgilojmajmkij")

        # Converts the Multipart msg into a string
        text = msg.as_string()
        # sending the mail
        s.sendmail(EMAIL_ADDRESS, msg['To'], text)



        # terminating the session
        s.quit()

        return Response("Email Sent !!!")

    def __init__(self):
        pass