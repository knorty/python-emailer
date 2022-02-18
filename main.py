import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from pip import main


root = Tk()
root.title('Norty Mailer')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

email = EmailMessage()
email['from'] = 'Kyle Norton'
html = None


def sendEmail(*args):
    email['to'] = email_address.get()
    email['subject'] = email_subject.get()
    email.set_content(html.substitute(name=recipient_name.get()), 'html')
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('kylebnorty@gmail.com', 'Nugwife2014')
        smtp.send_message(email)
        print('All systems a go!')


def uploadFile():
    global html
    filename = filedialog.askopenfilename(title="Upload A File", filetypes=(
        ('html files', '*.html'), ('text', '*.txt')))
    html = Template(Path(filename).read_text())


email_address = StringVar()
email_entry = ttk.Entry(mainframe, width=20, textvariable=email_address)
email_entry.grid(column=2, row=1, sticky=(W, E))

recipient_name = StringVar()
recipient_entry = ttk.Entry(mainframe, width=10, textvariable=recipient_name)
recipient_entry.grid(column=2, row=2, sticky=(W, E))

email_subject = StringVar()
subject_entry = ttk.Entry(mainframe, width=50, textvariable=email_subject)
subject_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Upload File", command=uploadFile).grid(
    column=2, row=4, sticky=W)
ttk.Button(mainframe, text="Send", command=sendEmail).grid(
    column=2, row=4, sticky=E)

ttk.Label(mainframe, text='Recipient\'s Email Address: ').grid(
    column=1, row=1, sticky=E)
ttk.Label(mainframe, text='Recipient\'s Name: ').grid(
    column=1, row=2, sticky=E)
ttk.Label(mainframe, text='Email Subject: ').grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

email_entry.focus()
root.bind("<Return>", sendEmail)

root.mainloop()
