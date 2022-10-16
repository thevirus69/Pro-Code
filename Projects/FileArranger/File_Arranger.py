from tkinter import *
import subprocess
import os
import shutil
from tkinter import messagebox
def file_manage():
    f=open("path.txt","r+")
    get_path=f.read().rstrip() 
    f.close() 
    pdf_files=[]
    text_files=[]
    images=[]
    miscs=[]
    others=[]
    managing_path=get_path 
    f=open("output.txt","a+")
    
    for files in os.listdir(managing_path):
        if not(os.path.isdir(managing_path+"\\"+files)): 
            if files.endswith('.pdf'):
                pdf_files.append(files)
                                
            elif files.endswith('.jpg') or files.endswith('.png'):
                images.append(files) 
            elif files.endswith('.txt') or files.endswith('.html') or files.endswith('.c') or files.endswith('.py') or files.endswith('.docx'):
                text_files.append(files) 
            elif files.endswith('.mp4') or files.endswith('.mkv') or files.endswith('.mp3'):
                miscs.append(files)
            else:
                others.append(files) 
    path_folders=[os.path.join(managing_path,"pdf_files"),os.path.join(managing_path,"text_files"),os.path.join(managing_path,"images"),os.path.join(managing_path,"miscs"),os.path.join(managing_path,"others")]
   
    for i in path_folders:
        os.makedirs(i) 
    current_location=managing_path 
    for i in pdf_files:
        source=current_location+'\\'+i 
        destination=os.path.join(managing_path,"pdf_files") 
        shutil.move(source,destination)
        t="MOVED- "+i+"\n" 
        f.write(t) 
    for i in text_files: 
        source=current_location+'\\'+i
        destination=os.path.join(managing_path,"text_files")
        shutil.move(source,destination)
        t="MOVED- "+i+"\n"
        f.write(t)
    for i in images:
        source=current_location+'\\'+i
        destination=os.path.join(managing_path,"images")
        shutil.move(source,destination)
        t="MOVED- "+i+"\n"
        f.write(t)
    for i in miscs: 
        source=current_location+'\\'+i
        destination=os.path.join(managing_path,"miscs")
        shutil.move(source,destination)
        t="MOVED- "+i+"\n"
        f.write(t)
    for i in others: 
        source=current_location+'\\'+i
        destination=os.path.join(managing_path,"others")
        shutil.move(source,destination)
        t="MOVED- "+i+"\n"
        f.write(t)
    f.write("Process Completed") 
    f.close()  
def read_data(): 
    w=open("output.txt","r+")  
    data=w.read() 
    w.close() 
    return(data)
def menu(): 
    def hello(): 
        messagebox.showinfo("MENU", "Do nothing!") 
    def kill():
        exit()   
    def en_data():
        f=open("path.txt","w+") 
        inp=e1.get() 
        f.write(inp)
        f.close()
    top = Tk() 
    top.geometry("1500x1500")
    var = StringVar()
    label = Message(top, textvariable=var, relief=RAISED)
    var.set("DESTINING")  
    label.configure(width='500',justify=CENTER,bg='lightblue',font='Algerian 18 bold',bd='8px',padx='10',pady='20',fg='black')
    label.pack()
    labelframe = LabelFrame(top, text="MENU")
    labelframe.configure(bg='light blue',font='Arial 15 bold',fg='green',bd='5px')
    file_ent = Label(labelframe, text="Enter the path where File management will be Active:-")
    file_ent.configure(bg='white',font='Arial 14 bold',bd='4px',padx='3',pady='3',fg='black')
    file_ent.place(x=30,y=120)
    e1 = Entry(top,width=60)
    e1.place(x=560,y=243)
    B1 = Button(top, text = "Instructions", command = hello)
    B1.configure(bg='brown',fg='white',font='Arial 15 bold')
    B1.place(x = 35,y = 180)
    B2 = Button(top, text = "Manage", command = file_manage)
    B2.configure(bg='white',fg='black',font='Arial 10 bold')
    B2.place(x = 500,y = 300)
    
    text1 = Label(text="OUTPUT")
    text1.place(x=60, y=330)
    output = Text(top)
    dat=read_data()
    output.insert(INSERT,dat)
    output.place(x=50,y=350)
    B3 = Button(top, text = "Confirm", command =lambda: en_data())
    B3.configure(bg='white',fg='black',font='Arial 10 bold')
    B3.place(x = 900,y = 240)
    labelframe.pack(fill="both", expand="yes")
    top.mainloop()
menu()
