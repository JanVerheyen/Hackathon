import os 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEBase import MIMEBase
from email import Encoders

def mail():
    #Set up crap for the attachments
    files = "Doormen/"
    filenames = [os.path.join(files, f) for f in os.listdir(files)]
    filenames = filenames[-5:]
    #print filenames
        
        
    #Set up users for email
    gmail_user = "raspberry.doorcamera@gmail.com"
    gmail_pwd = "Intuition"
    recipients = ['jan.verheyen97@gmail.com','midasgossye@hotmail.com']
        
    #Create Module
    
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = 'Doorcam'
    
    msg.attach(MIMEText('Test'))
    
    #get all the attachments
    for file in filenames:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
        msg.attach(part)
    
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, recipients, msg.as_string())
    mailServer.close()
