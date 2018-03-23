import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host="localhost"
port=25

email_conn = smtplib.SMTP(host,port)
print(email_conn.ehlo())

frommail="gax@gmail.com"
you=["otro@gmail.com"]



the_msg= MIMEMultipart("alternative")
the_msg['Subject'] = "Hello There!"
the_msg["From"] = frommail
the_msg["To"] = you[0]

plaint_text= "Texting Message"
html_text="""\
<html>
    <head></head>
    <body>
        <p>Hey!</br>
            Testingo this email <b>message</b>. Made by <a href='clavy.fdi.ucm.es'>Team Clavy</a>
        </p>
    </body>
</html>
"""

part_1 = MIMEText(plaint_text, 'plain')
part_2 = MIMEText(html_text,"html")

the_msg.attach(part_1)
the_msg.attach(part_2)

#print(the_msg.as_string())

email_conn.sendmail(frommail,you,the_msg.as_string())
email_conn.quit()