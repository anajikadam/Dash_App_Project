import os
import smtplib
import imghdr
from email.message import EmailMessage
import time

import glob
import os



def sendEmail():
    EMAIL_ADDRESS = "##########@gmail.com"
    EMAIL_PASSWORD = "*********"

    # for multile contact and multiple attachment
    msg = EmailMessage()
    msg['Subject'] = 'Today\'s Covid Report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = '***#########@gmail.com'

    msg.set_content('Hello,  This is an electronically generated email, please do not reply. Covid Report Auto Generated PDF file')
    path = "assets/Img/img_email.jpg"
    with open(path,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
        file_name = file_name.split('/')[2]
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    list_of_files = glob.glob('assets/pdf/*') 
    latest_file = max(list_of_files, key=os.path.getctime)
    file0 = "assets/pdf/"+latest_file.split('\\')[1]
    files = [file0]
    for file in files:
        with open(file,'rb') as f:
            file_data = f.read()
            #file_type = imghdr.what(f.name)  # for pdf file type is application and subtype='octet-stream'
            file_name = f.name
            file_name = file_name.split('/')[2]
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print('Email Sent....!')
        
# sendEmail()   