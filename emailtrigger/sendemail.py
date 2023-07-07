# import base64
# from email.mime.text import MIMEText
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from requests import HTTPError

# SCOPES = [
#         "https://www.googleapis.com/auth/gmail.send"
#     ]
# flow = InstalledAppFlow.from_client_secrets_file('client_secret_258019741435-oum001ave5ag18uvouedh9hoc5v4fvcl.apps.googleusercontent.com.json', SCOPES)
# creds = flow.run_local_server(port=0)

# service = build('gmail', 'v1', credentials=creds)
# message = MIMEText('This is the body of the email')
# message['to'] = 'jjagadeeshgouda1996@gmail.com'
# message['subject'] = 'Email Subject'
# create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

# try:
#     message = (service.users().messages().send(userId="me", body=create_message).execute())
#     print(F'sent message to {message} Message Id: {message["id"]}')
# except HTTPError as error:
#     print(F'An error occurred: {error}')
#     message = None

import smtplib
from email.mime.text import MIMEText
from requests import HTTPError
from datetime import date
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from emailbot.settings import ATTFILEPATH
import os

def sendemailfun(emailcontent, evidencefile,natureofcomplaint):
    try:
        print("======= Sending Email ======")
        sender_email = "jjagadeeshgouda1996@gmail.com"
        sender_password = "smzdyihkjjxictyp"
        recipient_email = "jjagadeeshgouda1996@gmail.com"
        natureof = ' '.join(map(str, natureofcomplaint.values()))
        subject = "Complaint against poll violence in panchayat elections of " + emailcontent['panchayat'] + " under " + emailcontent['arepollingboth']
        if evidencefile.name:
            attachmentstatus = "PFA the evidence justifying our claim aforementioned"
        else:
            attachmentstatus = ""

        body = """
        <html>
        <body>
            
            <p>To,<br>
            The <b>"""+ emailcontent['totext'] +"""</b>, <b>"""+ emailcontent['toemail'] +"""</b>
            <br>CC: <b>"""+ emailcontent['cctext'] +""", """+ emailcontent['ccemail']+"""</b></p>

            <p>Dear Sir/Madam,<br><br><br>

            I am writing this letter to bring to your notice the poll violence that is taking/took place during the ongoing panchayat elections in my constituency.
            <br>We are getting legitimate reports of: <b>"""+ natureof +"""</b> From <b>"""+ emailcontent['panchayat'] +"""</b> and <b>"""+ emailcontent['arepollingboth']+"""</b>
            <br><b>"""+attachmentstatus+"""</b>
            <br>Based on our initial assessment of the situation, it is likely being caused by: <b>"""+ emailcontent['nameofaccused']+"""</b> 
            <br>I would like to request you to take immediate action against the perpetrators of this violators and ensure immediate corrective actions by the powers vestowed to you by the constitution of India. Delay in intervening & taking action to the complaint above might result in loss of life, livelihod & property damage & might snowball into chaos which may result in widespread unrest.
            <br>Enforcing quick & decisive acions can avert the aforementioned & promote safe democratic practices & voting rights.
            <br>I urge you to take strict action against the trouble makers and ensure that they are brought to justice.</p>

            <br>Thank you for your attention to this matter.

            <br><br>Sincerely,
            <br><b>"""+emailcontent['fromemail']+""", """+emailcontent['fromccemail'] +"""
            <br>"""+emailcontent['fromtext']+""", """+emailcontent['fromcctext']+"""</b>
        </body>
        </html>
        """

        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = recipient_email

        html_message = MIMEText(body, 'html')
        # html_message['Subject'] = subject
        # html_message['From'] = sender_email
        # html_message['To'] = recipient_email
        print(evidencefile)
        print(os.path.join(ATTFILEPATH,evidencefile.name))

        with open(os.path.join(ATTFILEPATH,evidencefile.name), 'rb') as f:
            image_part = MIMEImage(f.read())

        image_part.add_header('Content-Disposition', "attachment; filename= %s" % evidencefile.name)
        message.attach(html_message)
        message.attach(image_part)

        

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("======= Email Sent Successfully ======")
        return True
    except HTTPError as error:
        print(F'An error occurred: {error}')
        return str(error)
#     message = None
    