from tkinter import *
import tkinter as t
from tkinter import ttk,messagebox
import tkinter.messagebox
from PIL import Image,ImageTk
from csv import DictWriter,writer
import csv,os,webbrowser
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Frame
import time
#----------------------Voucher menu shortcut---------------------------------------
def voucher_sc(en,window1):
    root=Toplevel()
    filexists_3=os.path.isfile("vouchers_data.csv")
    if not filexists_3:
        messagebox.showerror(parent=window1,title="Error",message="Vouchers File Not Found")
        window1.destroy()
        root.destroy()
    root.title("Vouchers no | Date | Amount | Party Name")
    select=[]
    date=[]
    voucher=[]
    amount=[]
    cost_name=[]
    with open("vouchers_data.csv","r") as f:
        csv_reader=csv.reader(f)
        for i in csv_reader :
            voucher.append(i[2])
            date.append(i[1])
            cost_name.append(i[0])
            amount.append(i[5])
    voucher.remove("Particulars")
    date.remove("Date")
    cost_name.remove("party_name")
    amount.remove("Credit")
    root.geometry("575x300+175+230")
    def CurSelet(event):
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        select.append(picked.split("  |  ")[0])
    def lb_bind(event):
        en.insert(END,select[-1])
        root.destroy()
    listbox = Listbox(root,width=62,height=40,selectbackground="blue",background="light blue",font=('times',13)) 
    listbox.bind('<<ListboxSelect>>',CurSelet)
    root.bind("<Return>",lb_bind)
    listbox.pack(side = LEFT, fill = BOTH) 
    scrollbar = Scrollbar(root) 
    scrollbar.pack(side = RIGHT, fill = BOTH)
    c=0
    for i in range(len(voucher)):
        listbox.insert(END,f"{voucher[c]}  |  {date[c]}  |  {amount[c]}  |  {cost_name[c]}")
        c+=1
    def esc(event):
        root.destroy()
    listbox.focus_force() 
    listbox.config(yscrollcommand = scrollbar.set) 
    scrollbar.config(command = listbox.yview) 
    root.bind("<Escape>",esc)
    root.resizable(0,0)
#--------------------------Invoice menu shortcut-------------------------------------------------
def inv_n(en,file1,tit,window1):
    root = Toplevel()
    filexists_3=os.path.isfile("invoice_data.csv")
    if not filexists_3:
        messagebox.showerror(parent=window1,title="Error",message="Invoice File Not Found")
        window1.destroy()
        root.destroy()
    root.title(tit)
    select=[]
    date=[]
    inv=[]
    cost_name=[]
    with open("invoice_data.csv","r") as f:
        csv_reader=csv.reader(f)
        for i in csv_reader :
            inv.append(i[0])
            date.append(i[1])
            cost_name.append(i[2])
    inv.remove("invoice_no")
    date.remove("date")
    cost_name.remove("costumer")
    root.geometry("575x300+115+230")
    def CurSelet(event):
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        select.append(picked.split("  |  ")[0])
    def lb_bind(event):
        en.insert(END,select[-1])
        root.destroy()
    listbox = Listbox(root,width=62,height=40,selectbackground="blue",background="light blue",font=('times',13)) 
    listbox.bind('<<ListboxSelect>>',CurSelet)
    root.bind("<Return>",lb_bind)
    listbox.pack(side = LEFT, fill = BOTH) 
    scrollbar = Scrollbar(root) 
    scrollbar.pack(side = RIGHT, fill = BOTH)
    c,d,e=0,0,0
    for i in range(len(inv)):
        listbox.insert(END,f"{inv[c]}  |  {date[d]}  |  {cost_name[e]}")
        c+=1
        d+=1
        e+=1
    def esc(event):
        root.destroy()
    listbox.focus_force() 
    listbox.config(yscrollcommand = scrollbar.set) 
    scrollbar.config(command = listbox.yview) 
    root.bind("<Escape>",esc)
    root.resizable(0,0)
#---------------------Costumer menu shortcut-------------------------------
def cost_n(en,file1,tit,headers,x1,y1,window,background,foreground):
    root = Toplevel()
    filexist=os.path.isfile(file1)
    st=file1.split(".")[0]
    if not filexist:
        messagebox.showerror(parent=window,title="Error",message=f"{st} file not found")
        window.destroy()
        root.destroy()
    root.title(tit)
    select=[]
    with open(file1,"r") as f:
        csv_reader_=csv.reader(f)
        data=[line for line in  csv_reader_]
        data.remove(headers)
        data.sort(key=lambda x: x[0])
    root.geometry("575x300+115+230")
    def CurSelet(event):
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        select.append(picked.split("  |  ")[2])
    def lb_bind(event):
        en.insert(END,select[-1])
        root.destroy()
    listbox = Listbox(root,width=62,height=40,selectbackground=foreground,background=background,font=('times',13)) 
    listbox.bind('<<ListboxSelect>>',CurSelet)
    root.bind("<Return>",lb_bind)
    listbox.pack(side = LEFT, fill = BOTH) 
    scrollbar = Scrollbar(root) 
    scrollbar.pack(side = RIGHT, fill = BOTH)
    sno=1
    for i in data:
        listbox.insert(END,f" {str(sno).zfill(4)}  |  {i[x1]}  |  {i[y1]}")
        sno+=1
    def esc(event):
        root.destroy()
    listbox.focus_force() 
    listbox.config(yscrollcommand = scrollbar.set) 
    scrollbar.config(command = listbox.yview) 
    root.bind("<Escape>",esc)
    root.resizable(0,0)
    root.attributes('-toolwindow', True)
