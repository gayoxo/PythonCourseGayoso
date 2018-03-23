import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host="localhost"
port=25


class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" % (amount)
        detail = {
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:  # if email != None
            email = email.lower()
            detail["email"] = email
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get("email")
                if user_email: #test None
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []

    def send_email(self):
        self.make_messages()
        if len(self.email_messages) >0:
            for detail in self.email_messages:
                user_email=detail['email']
                user_message = detail['message']

                try:
                    email_conn = smtplib.SMTP(host, port)
                    frommail = "gax@gmail.com"
                    you = [user_email]
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Billing Update!"
                    the_msg["From"] = frommail
                    the_msg["To"] = user_email

                    part_1 = MIMEText(user_message, 'plain')

                    the_msg.attach(part_1)

                # print(the_msg.as_string())

                    email_conn.sendmail(frommail, you, the_msg.as_string())
                    email_conn.quit()
                except:
                    print("Error")
            return True
        return False

obj = MessageUser()
obj.add_user("Justin", 123.32, email='Justin@teamcfe.com')
obj.add_user("jOhn", 94.23,email='jOhn@teamcfe.com')
obj.add_user("Sean", 93.23,email='Sean@teamcfe.com')
obj.add_user("Emilee", 193.23,email='Emilee@teamcfe.com')
obj.add_user("Marie", 13.23,email='Marie@teamcfe.com')
resuldeta=obj.get_details()

for resuldetauni in resuldeta:
    print(resuldetauni);

obj.send_email()
#
# results=obj.make_messages()
#
# for resuluni in results:
#     print(resuluni);

def some_rando():
    print("Algo Random")