from Email2 import MessageUser, some_rando
#he importado el MessageUser del Email2.py y una funcion suelta del mismo

obj = MessageUser()
obj.add_user("Justin", 123.32, email='hello@teamcfe.com')
obj.add_user("jOhn", 94.23)
obj.add_user("Sean", 93.23)
obj.add_user("Emilee", 193.23)
obj.add_user("Marie", 13.23)
resuldeta=obj.get_details()

for resuldetauni in resuldeta:
    print(resuldetauni);

results=obj.make_messages()

for resuluni in results:
    print(resuluni);

some_rando()