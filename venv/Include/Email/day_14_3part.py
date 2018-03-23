import csv
import os


def get_length(filepath):
    file_path = os.path.join(os.getcwd(), filepath)
    if not os.path.isfile(file_path):
        with open(filepath, "w+", newline='') as csvfile:
            writer = csv.writer(csvfile)

    with open(filepath, "r", newline='') as csvfile:
        reader= csv.reader(csvfile)
        reader_list = list(reader)
        print(reader_list)
        return len(reader_list)

def append_data(file_path,name,email):
    fieldnamesw = ['id','name','email']
    next_id=get_length(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnamesw)
        if (next_id == 0):
            writer.writeheader()
            next_id+=1


        writer.writerow({
            "id":next_id,
            "name":name,
            "email":email,
        })

file_path="cvs\data3.csv"
append_data(file_path,"Justin", email='Justin@teamcfe.com')
append_data(file_path,"jOhn",email='jOhn@teamcfe.com')
append_data(file_path,"Sean",email='Sean@teamcfe.com')
append_data(file_path,"Emilee",email='Emilee@teamcfe.com')
append_data(file_path,"Marie", email='Marie@teamcfe.com')