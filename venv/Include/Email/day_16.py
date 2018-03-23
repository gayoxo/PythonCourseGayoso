import csv
import os
import shutil
import datetime
from tempfile import NamedTemporaryFile


# def get_length(filepath):
#     file_path = os.path.join(os.getcwd(), filepath)
#     if not os.path.isfile(file_path):
#         with open(filepath, "w+", newline='') as csvfile:
#             writer = csv.writer(csvfile)
#
#     with open(filepath, "r", newline='') as csvfile:
#         reader= csv.reader(csvfile)
#         reader_list = list(reader)
#         print(reader_list)
#         return len(reader_list)
#
# def append_data(file_path,name,email):
#     fieldnamesw = ['id','name','email']
#     next_id=get_length(file_path)
#     with open(file_path, "a", newline='') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnamesw)
#         if (next_id == 0):
#             writer.writeheader()
#             next_id+=1
#
#
#         writer.writerow({
#             "id":next_id,
#             "name":name,
#             "email":email,
#         })
#
# file_path="cvs\data3.csv"
# append_data(file_path,"Justin", email='Justin@teamcfe.com')
# append_data(file_path,"jOhn",email='jOhn@teamcfe.com')
# append_data(file_path,"Sean",email='Sean@teamcfe.com')
# append_data(file_path,"Emilee",email='Emilee@teamcfe.com')
# append_data(file_path,"Marie", email='Marie@teamcfe.com')


# filename="cvs\data3.csv"
# filenamed="cvs\data4.csv"
# temp_file= NamedTemporaryFile(mode='w+',delete=False, newline='')
#
# with open(filename,"r", newline='') as csvfile,temp_file:
#     reader = csv.DictReader(csvfile)
#     fieldname = ['id','name', 'email', 'amount', 'sent', 'date']
#     writer = csv.DictWriter(temp_file, fieldnames=fieldname)
#     writer.writeheader()
#     print(temp_file.name)
#     for row in reader:
#         row["sent"]=""
#         if (int(row["id"])==4):
#             row["sent"]=True
#             print(row)
#         writer.writerow({
#             "id": row["id"],
#             "name": row["name"][0].upper()+row["name"][1:].lower(),
#             "email": row["email"].lower(),
#             "amount": "1293.23",
#             "sent": row["sent"],
#             "date": datetime.datetime.now()
#         })
#
# shutil.move(temp_file.name,filenamed)

def edit_data(edit_id=None,email=None,amount=None, sent=None):
    filename = "cvs\data4.csv"
    temp_file = NamedTemporaryFile(mode='w+', delete=False, newline='')

    with open(filename, "r", newline='') as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldname = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldname)
        writer.writeheader()
        # print(temp_file.name)
        for row in reader:
            if edit_id is not None:
                if (int(row["id"]) == int(edit_id)):
                    row["amount"] = amount
                    row["sent"] = sent
            elif email is not None:
                if (str(row["email"]) == str(email)):
                    row["amount"] = amount
                    row["sent"] = sent
            else:
                pass
            writer.writerow(row)


    shutil.move(temp_file.name, filename)
    return True


edit_data(edit_id=5,amount=0.099,sent=True)

edit_data(email="sean@teamcfe.com",amount=99.666,sent=True)