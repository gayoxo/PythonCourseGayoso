import smtplib

host="localhost"
port=25

email_conn = smtplib.SMTP(host,port)
print(email_conn.ehlo())

frommail="gax@gmail.com"
you=["otro@gmail.com"]

email_conn.sendmail(frommail,you,"mola")
email_conn.quit()

