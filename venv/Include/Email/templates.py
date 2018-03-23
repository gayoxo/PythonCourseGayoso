import os


# open("templates\email_message.txt").read()

def get_template_path(path):
    file_path = os.path.join(os.getcwd(),path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid template Path %s"%(file_path) )
    return file_path

def get_template(path):
    file_path= get_template_path(path)
    return open(file_path).read()

def render_context(template_string,context):
    return template_string.format(**context)

file_='templates\email_message.txt'
file_html='templates\email_message.html'
context = {
    "name":'justin',
    "date":'abc',
    "total":22
}
# outS=get_template(file_)
template=get_template(file_)
template_html=get_template(file_html)
outS=render_context(template,context)
outS2=render_context(template_html,context)
print(outS)
print(outS2)