# insert the error messagebox
from tkinter import *
from tkinter import messagebox
import speech_recognition as s
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
import socket
from threading import Thread
import random

root = Tk()
root.title("..server..")
root.geometry("960x540")
img=PhotoImage(file="voice2voice.png")
frame=Label(root,image=img)
frame.place(x=0,y=0)
lancode=""
lancode2=""


LANGUAGES = {
'afrikaans': 'af','albanian': 'sq','amharic': 'am', 'arabic': 'ar', 'armenian': 'hy','azerbaijani': 'az',
'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn','bosnian': 'bs','bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 
'chichewa': 'ny', 'chinese': 'zh-cn','corsican': 'co',
'croatian': 'hr', 'czech': 'cs','danish': 'da','dutch': 'nl', 'english': 'en','esperanto': 'eo','estonian': 'et',
'filipino': 'tl','finnish': 'fi', 'french': 'fr', 'frisian': 'fy','galician': 'gl','georgian': 'ka', 
'german': 'de', 'greek': 'el', 'gujarati': 'gu','haitian creole': 'ht','hausa': 'ha', 'hawaiian': 'haw', 
'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn','hungarian': 'hu','icelandic': 'is','igbo': 'ig','indonesian': 'id',
'irish': 'ga','italian': 'it', 'japanese': 'ja','javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 
'khmer': 'km', 'korean': 'ko','kurdish (kurmanji)': 'ku','kyrgyz': 'ky', 'lao': 'lo','latin': 'la', 
'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb','macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms',
'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn','myanmar (burmese)': 'my','nepali': 'ne', 
'norwegian': 'no', 'odia': 'or', 'pashto': 'ps','persian': 'fa', 'polish': 'pl','portuguese': 'pt','punjabi': 'pa',
'romanian': 'ro','russian': 'ru','samoan': 'sm','scots gaelic': 'gd','serbian': 'sr','sesotho': 'st',
'shona': 'sn','sindhi': 'sd', 'sinhala': 'si','slovak': 'sk','slovenian': 'sl', 'somali': 'so','spanish': 'es',
'sundanese': 'su','swahili': 'sw','swedish': 'sv','tajik': 'tg', 'tamil': 'ta', 'telugu': 'te','thai': 'th', 
'turkish': 'tr','ukrainian': 'uk','urdu': 'ur','uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi','welsh': 'cy', 
'xhosa': 'xh','yiddish': 'yi','yoruba': 'yo','zulu': 'zu'
}

s1=socket.socket()

def server():
    global con
    ser_name=entry5.get()
    ipaddress=socket.gethostbyname(socket.gethostname())
    print(ipaddress)
    s1.bind((ipaddress,1235))
    root.update()
    #label7.config(text="server is ready for connection.....")
    print("server is ready for connection...")
    s1.listen(1)
    con,addr=s1.accept()
    print(addr," has connected successfully...")
    root.update()
    ser_name=ser_name.encode()
    con.send(ser_name)
    print(ser_name)
    root.update()
    cli_name=con.recv(1024).decode()
    print(cli_name)
    label7['text']="You are now connected with : "
    label2= Label(root, text = cli_name, bg='white',font=('calibre',10,'bold'))
    label2.place(x=320,y=95)
    Thread(target=rec).start()


OPTION=['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 
'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 
'chinese', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 
'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati',
'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo',
'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean',
'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 
'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian',
'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese',
'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona',
'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 
'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 
'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']


varible_input=StringVar(root)
varible_input.set(OPTION[20])
var_inp=OptionMenu(root,varible_input,*OPTION)
var_inp.place(x=700,y=390)
def ok():
    global lancode2
    lan2=varible_input.get()
    #print ("value is:" + varible_input.get())
    print(lan2)
    if(lan2 in LANGUAGES.keys()):
        lancode2=LANGUAGES[lan2]
    else:
        print("language is not present in dictonary")   


button5 = Button(root, text="OK", command=ok)
button5.place(x=790,y=393)
# for input language
varible_output=StringVar(root)
varible_output.set(OPTION[20])
var_out=OptionMenu(root,varible_output,*OPTION)
var_out.place(x=80,y=390)

def ok2():
    global lancode
    lan=varible_output.get()
    #print ("value is:" + varible_output.get())
    print(lan)
    if(lan in LANGUAGES.keys()):
        lancode=LANGUAGES[lan]
    else:
        print("language is not present in dictonary")
button6 = Button(root, text="OK", command=ok2)
button6.place(x=170,y=393)
label10=Label(root,text="",font=("calibre",12))
label10.place(x=100,y=200)

jio=""
def rec():
    global jio
    while True:
        jio= con.recv(1024).decode()
        frame=Frame(root,bg='white',height=100,width=150)
        frame.place(x=100,y=250)
        LABEL11=Label(frame,text="Recive a Message",font=('calibre',12))
        LABEL11.place(x=10,y=10)
        root.after(1500,frame.destroy)

def translate_text():
    global lancode,con,jio
    if lancode=="":
        lancode="en"   
    root.update()
    print(jio)
    root.update()
    translator= Translator()
    lang2= translator.translate(jio, dest = lancode)
    b=lang2.text
    print(b)
    myvoice=gTTS(text=b,lang=lancode,slow=False) 
    root.update()
    num=random.randint(1,100)
    try:
        if os.path.exists(f"surya{num}.mp3"):
            print("file already exists")
            return
        else:
            myvoice.save(f"surya{num}.mp3")
            playsound(f"surya{num}.mp3")
        if os.path.exists(f"surya{num}.mp3"):
            os.remove(f"surya{num}.mp3")
        else:
            print("file not found")
    except Exception as e:
        print("The error is :",e)


def voice_record_and_text():
    global inputvoice,con,lancode2
    r=s.Recognizer()
    if lancode2=="":
        lancode2="en"
    while(1):
        try: 
            with s.Microphone() as input:
                audio = r.listen(input)
                root.update()       
                inputvoice=r.recognize_google(audio, language=lancode2)
                root.update()
                inputvoice=inputvoice.encode()
                con.send(inputvoice)
                root.update()
                print(inputvoice)
                frame=Frame(root,bg="#3E47C9",height=100,width=150)
                frame.place(x=600,y=250)
                LABEL11=Label(frame,text="Message Sent ",font=('calibre',12))
                LABEL11.place(x=23,y=10)
                root.after(1500,frame.destroy)
                break
        
        except s.RequestError as e:
            messagebox.showinfo("Error","Request Error")
            root.update()
        except s.UnknownValueError:
            messagebox.showerror("Error","Unknow value Error occured")
            root.update()
            
#for the mic used as button
micimg=PhotoImage(file="mic.png")
button=Button(root,image=micimg,bg='#3E47C9',bd=0,command = voice_record_and_text)
button.place(x=550,y=450)

# for the play button 
playimg=PhotoImage(file="listen.png")
playbtn=Button(root,image=playimg,bg='white',bd=0,command = translate_text)
playbtn.place(x=180,y=460)

#for the exit button
exitimg=PhotoImage(file="exit.png")
button2=Button(root,image=exitimg,bg='#3E47C9',bd=0,command=root.destroy)
button2.place(x=875,y=460)

#button for the start the server
label5 = Label(root, text ='Enter Name',font=('calibre',12,))
label5.place(x=640,y=105)
entry5 = Entry(root,font=("calibre",11))
entry5.place(x=740,y=105)
sub_btn5=Button(root,text = 'sumbit',font=("calibre",12), command= server)
sub_btn5.place(x=700,y=140)

#button for the label for server I/P Address
ipaddress=socket.gethostbyname(socket.gethostname())
label6=Label(root,text='server I/P Address is :',font=("calibre",12))
label6.place(x=640,y=70)
label4= Label(root, text=ipaddress,font=('calibre',12))
label4.place(x=795,y=70)

#message you are now connected
label7= Label(root, text ="", bg= 'white' ,font=('calibre',11,'bold'))
label7.place(x=100,y=95)

root.mainloop()
