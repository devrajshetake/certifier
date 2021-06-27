from tkinter.constants import COMMAND
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import smtplib
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import random
import email, smtplib, ssl
from tkinter import filedialog as fd 

   
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def show_frame(frame):
    frame.tkraise()
window=tk.Tk()
window.title('CERTIFICATE GENERATOR')
window.state('zoomed')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
frame1= tk.Frame(window, bg='#11282E')
frame2= tk.Frame(window, bg='#11282E')

for frame in (frame1, frame2):
    frame.grid(row=0,column=0,sticky='nsew')

#########################

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "xenia.event2021@gmail.com"

#############################################################33


def certi1():
    
    name = fd.askopenfilename() 
    print(name)
    
    df = pd.read_csv(name)
    font = ImageFont.truetype('arial.ttf', 60)
    for index,j in df.iterrows():
        img = Image.open('certificate.jpg')
        draw = ImageDraw.Draw(img)
        draw.text(xy=(450, 300), text='{}'.format(j['name']), fill=(0,0,0), font=font)
        img.save('pictures/{}.jpeg'.format(j['name']))
        img1 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw1 = ImageDraw.Draw(img1)
        draw1.text(xy=(380, 570), text='{}'.format(j['course']), fill=(0,0,0), font=font)
        img1.save('pictures/{}.jpeg'.format(j['name']))
        img2 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw2 = ImageDraw.Draw(img2)
        draw2.text(xy=(630, 570), text='{}'.format(j['college']), fill=(0,0,0), font=font)
        img2.save('pictures/{}.jpeg'.format(j['name']))
        img3 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw3 = ImageDraw.Draw(img3)
        draw3.text(xy=(210, 740), text='S.K.S', fill=(0,0,0), font=font)
        img3.save('pictures/{}.jpeg'.format(j['name']))
        img4 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw4 = ImageDraw.Draw(img4)
        draw4.text(xy=(650, 740), text='26-06-2021', fill=(0,0,0), font=font)
        img4.save('pictures/{}.jpeg'.format(j['name']))
    
        receiver_email = '{}'.format(j['email'])
        password = "xeniaevent"

# Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = "xenia.event2021@gmail.com"
        message["To"] = '{}'.format(j['email'])

# Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = 'pictures/{}.jpeg'.format(j['name'])

# Open PDF file in binary mode
        with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

# Add header as key/value pair to attachment part
        part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

# Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

def certi2():
    name = fd.askopenfilename() 
    print(name)    
    df = pd.read_csv(name)
    font = ImageFont.truetype('arial.ttf', 60)
    for index,j in df.iterrows():
        img = Image.open('Certificate of PARTICIPATION.jpg')
        draw = ImageDraw.Draw(img)
        draw.text(xy=(950, 650), text='{}'.format(j['name']), fill=(255,255,255), font=font)
        img.save('pictures/{}.jpeg'.format(j['name']))
        img1 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw1 = ImageDraw.Draw(img1)
        draw1.text(xy=(1375, 830), text='{}'.format(j['course']), fill=(255,255,255), font=font)
        img1.save('pictures/{}.jpeg'.format(j['name']))
        img2 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw2 = ImageDraw.Draw(img2)
        draw2.text(xy=(860, 830), text='{}'.format(j['college']), fill=(255,255,255), font=font)
        img2.save('pictures/{}.jpeg'.format(j['name']))
        img3 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw3 = ImageDraw.Draw(img3)
        draw3.text(xy=(1345, 970), text='S.K.S', fill=(255,255,255), font=font)
        img3.save('pictures/{}.jpeg'.format(j['name']))
        img4 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw4 = ImageDraw.Draw(img4)
        draw4.text(xy=(435, 970), text='26-06-2021', fill=(255,255,255), font=font)
        img4.save('pictures/{}.jpeg'.format(j['name']))
    
        receiver_email = '{}'.format(j['email'])
        password = "xeniaevent"

# Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = "xenia.event2021@gmail.com"
        message["To"] = '{}'.format(j['email'])

# Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = 'pictures/{}.jpeg'.format(j['name'])

# Open PDF file in binary mode
        with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

# Add header as key/value pair to attachment part
        part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

# Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

def certi3():
    name = fd.askopenfilename() 
    print(name)    
    df = pd.read_csv(name)
    font = ImageFont.truetype('arial.ttf', 60)
    for index,j in df.iterrows():
        img = Image.open('Art Deco Appreciation Certificate.jpg')
        draw = ImageDraw.Draw(img)
        draw.text(xy=(950, 650), text='{}'.format(j['name']), fill=(255,255,255), font=font)
        img.save('pictures/{}.jpeg'.format(j['name']))
        img1 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw1 = ImageDraw.Draw(img1)
        draw1.text(xy=(1275, 930), text='{}'.format(j['course']), fill=(255,255,255), font=font)
        img1.save('pictures/{}.jpeg'.format(j['name']))
        img2 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw2 = ImageDraw.Draw(img2)
        draw2.text(xy=(600, 930), text='{}'.format(j['college']), fill=(255,255,255), font=font)
        img2.save('pictures/{}.jpeg'.format(j['name']))
        img4 = Image.open('pictures/{}.jpeg'.format(j['name']))
        draw4 = ImageDraw.Draw(img4)
        draw4.text(xy=(870, 1100), text='26-06-2021', fill=(255,255,255), font=font)
        img4.save('pictures/{}.jpeg'.format(j['name']))
    
        receiver_email = '{}'.format(j['email'])
        password = "xeniaevent"

# Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = "xenia.event2021@gmail.com"
        message["To"] = '{}'.format(j['email'])

# Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = 'pictures/{}.jpeg'.format(j['name'])

# Open PDF file in binary mode
        with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

# Add header as key/value pair to attachment part
        part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

# Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

my_canvas2=tk.Canvas(frame1, width=800, height=500, bd=0, highlightthickness=0)
my_canvas2.pack(fill="both", expand=True)
my_canvas6=tk.Canvas(frame1, width=800, height=500)
my_canvas6.pack(fill="both", expand=True)
myimage1= ImageTk.PhotoImage(Image.open("certificate1.jpg")) 
myimage2= ImageTk.PhotoImage(Image.open("Certificate of PARTICIPATION1.jpg")) 
myimage3= ImageTk.PhotoImage(Image.open("Art Deco Appreciation Certificate1.jpg")) 
my_button1= tk.Button(frame1, image=myimage1, command = certi1 )
my_button2= tk.Button(frame1, image=myimage2, command = certi2 )
my_button3= tk.Button(frame1, image=myimage3, command = certi3 )
my_canvas6.create_window(250, -95, window=my_button1 )
my_canvas6.create_window(763, -95, window=my_button2)
my_canvas6.create_window(1275, -95, window=my_button3 )
show_frame(frame1)
window.mainloop()    



