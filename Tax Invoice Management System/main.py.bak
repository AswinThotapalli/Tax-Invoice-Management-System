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
import Reports
import Shortcuts_menu   
import side_menu
#*****Input validation as Integer value*****************************************
def correct(inp):

    if inp.isdigit():
        return True
    elif inp =="":
        return True
    else:
        return False 
class Main:
    '''This Class Represents the Main Window of Application which include primary Buttons and side menu '''
    def __init__(self,master):
        self.root=master
        self.root.title("Caerulean Bytechains Pvt Ltd 2021")
        self.root.config(menu=side_menu.side(self.root),bg="black")
        self.root.geometry("1350x750")
        self.root.state('zoomed')
        self.load=Image.open("icons\\q1.jpg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=Label(self.root,image=self.render)
        self.img.place(x=0,y=0)
        self.Lbl_btn=LabelFrame(self.root,bd=2,bg="white")
        self.Lbl_btn.grid(row=2,column=2,padx=180,pady=280)
    #*********************Buttons Icon**************************
        self.costumer_icon=PhotoImage(file="icons\\costumer.png")
        self.inv_icon=PhotoImage(file="icons\\invoice.png")
        self.item_icon=PhotoImage(file="icons\\items.png")
        self.report_icon=PhotoImage(file="icons\\report.png")
        self.acc_icon=PhotoImage(file="icons\\account.png")
        self.bil_icon=PhotoImage(file="icons\\billing.png")
        self.purchase_icon=PhotoImage(file="icons\\purchase.png")
    #*******************************************************************************************************
        self.lblcostumer=Button(self.Lbl_btn,text="costumer",image=self.costumer_icon,font="Forte 20",bg="white",fg="black",command=Costumer)
        self.lblcostumer.grid(row=0,column=0)
        self.lblcostumer.focus()
        self.lblitem=Button(self.Lbl_btn,text="item_icon",image=self.item_icon,font="Forte 20",bg="white",fg="black",command=Item)
        self.lblitem.grid(row=0,column=1)
        self.lblinv=Button(self.Lbl_btn,text="inv_icon",image=self.inv_icon,font="Forte 20",bg="white",fg="black",command=Invoice)
        self.lblinv.grid(row=0,column=2)
        self.lblrep=Button(self.Lbl_btn,text="report_icon",image=self.report_icon,font="Forte 20",bg="white",fg="black",command=Report)
        self.lblrep.grid(row=0,column=3) 
        self.lblacc=Button(self.Lbl_btn,text="acc_icon",image=self.acc_icon,font="Forte 20",bg="white",fg="black",command=Account)
        self.lblacc.grid(row=0,column=4)
        self.lblbil=Button(self.Lbl_btn,text="bil_icon",command=Billing,image=self.bil_icon,font="Forte 20",bg="white",fg="black")
        self.lblbil.grid(row=0,column=5)
        self.lblpur=Button(self.Lbl_btn,text="purchase_icon",command=Purchase,image=self.purchase_icon,font="Forte 20",bg="white",fg="black")
        self.lblpur.grid(row=0,column=6)
        self.root.bind("<q>",lambda event:Costumer())
        self.root.bind("<w>",lambda event:Item()) 
        self.root.bind("<e>",lambda event:Invoice())
        self.root.bind("<r>",lambda event:Report())
        self.root.bind("<t>",lambda event:Account())   
        self.root.bind("<y>",lambda event:Billing()) 
        self.root.bind("<u>",lambda event:Purchase())
        self.root.protocol('WM_DELETE_WINDOW',self.disabled) 
        self.root.resizable(0,0)
        self.root.bind("<Escape>",self.exit__) 
        if '2021-09-20'.split("-")[0]<=str(date.today()).split("-")[0]:
            if '2021-09-20'.split("-")[1]<=str(date.today()).split("-")[1]:
                if '2021-09-20'.split("-")[2]<=str(date.today()).split("-")[2]:
                    if messagebox.showerror("invalid","please update your software"):
                        self.root.destroy()
        self.root.mainloop()
    def exit__(self,event):
        if messagebox.askyesno(parent=self.root,title="Exit",message="Are You Sure?"):
            self.root.quit()
            
    def disabled(self):
        pass   
#*****************************COSTUMER******************************************
class Costumer:
    def __init__(self):
        self.costumer_window=Toplevel()
        self.costumer_window.geometry("700x900+0+0")
        self.costumer_window.config(bg="light blue")
        self.lbl=Label(self.costumer_window,text="Customer Data Handling Menu",width=29,font="Times 30 bold",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=20)
        self.label_frame=t.LabelFrame(self.costumer_window,foreground="white",background="light blue",bd=5)
        self.label_frame.grid(row=1,column=0,pady=10)         
        self.lbladd=Button(self.label_frame,text="Add",font="consolas 20 bold",bg="white",fg="black",command=self.add)
        self.lbladd.grid(row=0,column=0,pady=10,padx=100)
        self.lbladd.focus()
        self.lbladd.bind("<Return>",self.add_b)
        self.lbladd.bind("<Down>",lambda event: self.lblupdate.focus())
        self.lbladd.bind("<Up>",lambda event: self.lblrect.focus())
        self.lblupdate=Button(self.label_frame,text="Update/Delete",font="consolas 20 bold",bg="white",fg="black",command=self.update)
        self.lblupdate.grid(row=1,column=0,pady=10)
        self.lblupdate.bind("<Return>",self.update_b)
        self.lblupdate.bind("<Down>",lambda event: self.lblview.focus())
        self.lblupdate.bind("<Up>",lambda event: self.lbladd.focus())
        self.lblview=Button(self.label_frame,text="View",font="consolas 20 bold",command=self.view ,bg="white",fg="black")
        self.lblview.grid(row=2,column=0,pady=10)
        self.lblview.bind("<Return>",self.view_b)
        self.lblview.bind("<Down>",lambda event: self.lblrect.focus())
        self.lblview.bind("<Up>",lambda event: self.lblupdate.focus())
        self.lblrect=Button(self.label_frame,text="Back(Esc)",font="consolas 20 bold",bg="white",command=self.costumer_window.destroy,fg="black")
        self.lblrect.grid(row=3,column=0,pady=10)
        self.lblrect.bind("<Return>",self.exit)
        self.lblrect.bind("<Down>",lambda event: self.lbladd.focus())
        self.lblrect.bind("<Up>",lambda event: self.lblview.focus())
        self.costumer_window.focus_force()
        self.costumer_window.overrideredirect(True)
        self.costumer_window.bind("<Escape>",self.exit)
    def add(self):
        Add('light blue','blue')
    def add_b(self,event):
        self.add()
    def update(self):
        Update()
    def update_b(self,event):
        self.update()
    def view(self):
        fileexist_c=os.path.isfile("costumers.csv")
        if not fileexist_c:
            messagebox.showerror(parent=self.costumer_window,title="Error",message="Customer's File Not Found")
            self.costumer_window.destroy()
        else:
            webbrowser.open_new("costumers.csv")
    def view_b(self,event):
        self.view()
    def exit(self,event):
        self.costumer_window.destroy()
class Add:        
    def __init__(self,bgf,bgh):
        self.bgf=bgf
        self.bgh=bgh
        self.add_window=Toplevel()
        self.add_window.geometry("700x900+0+0")
        self.add_window.config(bg=self.bgf)
        self.lbl=Label(self.add_window,text="Customer Master",width=29,font="Times 30 bold",fg="white",bg=self.bgh,bd=10)
        self.lbl.grid(row=0,column=0,pady=20)
        self.l_frame=LabelFrame(self.add_window,foreground="white",background=self.bgf,bd=0)
        self.l_frame.grid(row=1,column=0)
        self.labels=["Customer Name:","Corresponding\n Address:","State:","TIN No/GST No:","Transport:","Phone (s):","G.S.T:"]
        for i in range(len(self.labels)):
            self.cur_label="label"+str(i)
            self.cur_label=t.Label(self.l_frame,text=self.labels[i],bg=self.bgh,fg="white",font="consolas 16",width=15)
            self.cur_label.grid(row=i,column=0,sticky=t.W,pady=10)
        self.na_entrybox=Entry(self.l_frame,width=15,font="consolas 16",bd=0)
        self.na_entrybox.grid(row=0,column=1,padx=20)
        self.na_entrybox.focus_set()
        self.na_entrybox.bind("<Return>",self.go1) 
        self.add_entrybox=Entry(self.l_frame,width=15,font="consolas 16",bd=0)
        self.add_entrybox.grid(row=1,column=1,padx=20)
        self.add_entrybox.bind("<Return>",self.go2)
        self.add_entryboxs=Entry(self.l_frame,width=15,font="consolas 16",bd=0)
        self.add_entryboxs.grid(row=2,column=1,padx=20)
        self.add_entryboxs.bind("<Return>",self.go22)   
        self.tin_entrybox=Entry(self.l_frame,width=15,font="consolas 16",bd=0)
        self.tin_entrybox.grid(row=3,column=1,padx=20)
        self.tin_entrybox.bind("<Return>",self.go3)   
        self.tran_entrybox=Entry(self.l_frame,width=15,font="consolas 16",bd=0)
        self.tran_entrybox.grid(row=4,column=1,padx=20)
        self.tran_entrybox.bind("<Return>",self.go4)
        self.phone_entrybox=Entry(self.l_frame,width=15,font="consolas 16",bd=0)
        self.phone_entrybox.grid(row=5,column=1,padx=20)
        self.reg=self.phone_entrybox.register(correct)
        self.phone_entrybox.config(validate="key",validatecommand=(self.reg,"%P"))
        self.phone_entrybox.bind("<Return>",self.go5)
        self.gst_combobox=ttk.Combobox(self.l_frame,width=15,font="consolas 16",state="readonly" )
        self.gst_combobox["values"]=('INTERSTATE','LOCAL') 
        self.gst_combobox.grid(row=6,column=1,pady=20) 
        self.gst_combobox.current(0)
        self.gst_combobox.bind("<Return>",self.go6)
        self.save_button=t.Button(self.l_frame,width= 10,text="Save",command=self.submit,background=self.bgh,foreground="white",font="consolas 14 ",bd=4)
        self.save_button.grid(row=8,column=0,padx=40,pady=10)
        self.back_button=t.Button(self.l_frame,width= 10,text="Back",command=self.add_window.destroy,background=self.bgh,foreground="white",font="consolas 14 ",bd=4)
        self.back_button.grid(row=8,column=1,pady=10)
        self.add_window.focus_force()
        self.add_window.overrideredirect(True)
        self.add_window.bind("<Escape>",self.exit_bind)
    def submit(self):
        if (self.na_entrybox.get()).upper() =="":
            messagebox.showwarning(parent=self.add_window,title="Warning",message="You save blank Entries\nAccount not Saved!!!")
            self.na_entrybox.focus()
        else:
            filename="costumers.csv"
            file_exists=os.path.isfile(filename)
            with open("costumers.csv","a",newline="") as f:
                csv_writer=DictWriter(f,fieldnames=["Customer Name","Address","State","TIN/GST no","Transport","Phone","GST","Date"])
                if not file_exists:
                    csv_writer.writeheader()
                with open("costumers.csv","r") as rd:
                    cs=csv.reader(rd)
                    c_name=[n[0] for n in cs]
                if self.na_entrybox.get().upper() in c_name:
                    messagebox.showerror(parent=self.add_window,title="Error",message="Name Already Exists")
                else:
                    csv_writer.writerow({
                    "Customer Name":(self.na_entrybox.get()).upper(),
                    "Address":str((self.add_entrybox.get()).upper()),
                    "State":self.add_entryboxs.get().upper(),
                    "TIN/GST no":str((self.tin_entrybox.get()).upper()),
                    "Transport":(self.tran_entrybox.get()).upper(),
                    "Phone":str(self.phone_entrybox.get().upper()),
                    "GST":self.gst_combobox.get(),
                    "Date":date.today().strftime('%d/%m/%y')

                    })
                    messagebox.showinfo(parent=self.add_window,title="Succesful",message="Account Saved Successfully")
                    self.na_entrybox.delete(0,END)
                    self.add_entrybox.delete(0,END)
                    self.add_entryboxs.delete(0,END)
                    self.tin_entrybox.delete(0,END)
                    self.tran_entrybox.delete(0,END)
                    self.phone_entrybox.delete(0,END)
                    self.na_entrybox.focus()
    def exit_bind(self,event):
        self.add_window.destroy()
    def go1(self,event):
        self.add_entrybox.focus()
    def go2(self,event):
        self.add_entryboxs.focus()
    def go22(self,event):
        self.tin_entrybox.focus()
    def go3(self,event):
        self.tran_entrybox.focus()
    def go4(self,event):
        self.phone_entrybox.focus()
    def go5(self,event):
        self.gst_combobox.focus()
    def go6(self,event):
        self.submit()
class Update(Add):
    def __init__(self):
        self.update_window=Toplevel()
        self.update_window.geometry("700x900+0+0")
        self.update_window.config(bg="light blue")
        self.lbl=Label(self.update_window,text="Enter The Details of Account",font="Times 30 bold ",fg="white",bg="blue",bd=10,width=29)
        self.lbl.grid(row=2,column=0,pady=20)
        self.lab_frame=LabelFrame(self.update_window,foreground="white",background="light blue",bd=0)
        self.lab_frame.grid(row=3,column=0)
        self.name_label=Label(self.lab_frame,text="Customer Name:",bg="blue",fg="white",font="consolas 15 ",width=15)
        self.name_label.grid(row=0,column=0,padx=10,pady=10,sticky=t.W)
        self.name_entry=Entry(self.lab_frame,width=15,font="consolas 15",bd=0)
        self.name_entry.grid(row=0,column=1,pady=10,padx=10)
        self.name_entry.focus()
        self.name_entry.bind("<Return>",self.go)
        self.update_button=t.Button(self.lab_frame,width= 10,text="Update",command=self.choice,background="blue",foreground="white",font="consolas 13",bd=3)
        self.update_button.grid(row=4,column=0,pady=20)
        self.del_button=t.Button(self.lab_frame,width= 10,text="Delete",command=self.delete,background="blue",foreground="white",font="consolas 13",bd=3)
        self.del_button.grid(row=4,column=1,padx=40,pady=20)
        self.back_button=t.Button(self.lab_frame,width= 10,text="Back",command=self.update_window.destroy,background="blue",foreground="white",font="consolas 13",bd=3)
        self.back_button.grid(row=4,column=2,padx=40,pady=20)
        self.update_window.bind("<Escape>",self.exit_b)
        self.update_window.overrideredirect(True)
        self.update_window.focus_force()
    def choice(self):
        if messagebox.askyesno(parent=self.update_window,title="Update Account",message="Are You Sure?"):
            name=(self.name_entry.get()).upper()
            flag=False
            with open("costumers.csv","r") as f:
                csv_reader=csv.reader(f)
                full_data=[]
                for line in csv_reader:
                    full_data.append(line)
                    if name in line:
                        upd=line
                        full_data.remove(line)
                        flag=True
                with open("costumers.csv","w",newline="") as f1:
                    wo=csv.writer(f1)
                    for line in full_data:
                        wo.writerow(line)
                if flag==True:
                    self.update_window.destroy()
                    super().__init__('lightblue','blue')
                    self.na_entrybox.insert(0,upd[0])
                    self.add_entrybox.insert(0,upd[1])
                    self.add_entryboxs.insert(0,upd[2])
                    self.tin_entrybox.insert(0,upd[3])
                    self.tran_entrybox.insert(0,upd[4])
                    self.phone_entrybox.insert(0,upd[5])
                else:
                    messagebox.showerror(parent=self.update_window,title="Error",message="Not Found")
                    self.name_entry.delete(0,END)
    def delete(self):
        if messagebox.askyesno(parent=self.update_window,title="Delete Account",message="Are You Sure?"):
            name=(self.name_entry.get()).upper()
            flag=False
            with open("costumers.csv","r") as f:
                csv_reader=csv.reader(f)
                full_data=[]
                for line in csv_reader:
                    full_data.append(line)
                    if name in line:
                        full_data.remove(line)
                        flag=True
            with open("costumers.csv","w",newline="") as f1:
                wo=csv.writer(f1)
                for line in full_data:
                    wo.writerow(line)
            if flag==True:
                messagebox.showinfo(parent=self.update_window,title="Success",message="Account Deleted Successfully")
                self.update_window.destroy()
            else:
                messagebox.showerror(parent=self.update_window,title="Error",message="Not Found")
                self.name_entry.delete(0,END)
    def exit_b(self,event):
        self.update_window.destroy()
    def go(self,event):
        if self.name_entry.get()=="":
            Shortcuts_menu.cost_n(self.name_entry,"costumers.csv","View All Costumers Name            Esc->Exit",["Customer Name","Address","State","TIN/GST no","Transport","Phone","GST","Date"],7,0,self.update_window,'lightgreen','green')
        else:
            self.choice()
#**********************************************************ITEM*************************
class Item:
    def __init__(self):
        self.item_window=Toplevel()
        self.item_window.geometry("700x900+0+0")
        self.item_window.config(bg="light blue")
        self.lbl=Label(self.item_window,text="Item Master",width=29,font="Times 30 bold",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=20)
        self.label_frame=t.LabelFrame(self.item_window,foreground="white",background="light blue",bd=5)
        self.label_frame.grid(row=1,column=0)
        self.lbladd=Button(self.label_frame,text="Add Item",font="consolas 20 bold",bg="white",fg="black",command=self.add)
        self.lbladd.grid(row=0,column=0,pady=10,padx=100)
        self.lbladd.focus()
        self.lbladd.bind("<Return>",self.add_b)
        self.lbladd.bind("<Up>",lambda event:self.lblrect.focus())
        self.lbladd.bind("<Down>",lambda event:self.lblupdate.focus())
        self.lblupdate=Button(self.label_frame,text="Update/Delete",command=self.update,font="consolas 20 bold",bg="white",fg="black")
        self.lblupdate.grid(row=1,column=0,pady=10)
        self.lblupdate.bind("<Return>",self.update_b)
        self.lblupdate.bind("<Up>",lambda event:self.lbladd.focus())
        self.lblupdate.bind("<Down>",lambda event:self.lblgenerate.focus())
        self.lblgenerate=Button(self.label_frame,text="View",command=self.view,font="consolas 20 bold",bg="white",fg="black")
        self.lblgenerate.grid(row=3,column=0,pady=10)
        self.lblgenerate.bind("<Return>",self.view_b)
        self.lblgenerate.bind("<Up>",lambda event:self.lblupdate.focus())
        self.lblgenerate.bind("<Down>",lambda event:self.lblrect.focus())
        self.lblrect=Button(self.label_frame,text="Back(Esc)",command=self.item_window.destroy,font="consolas 20 bold",bg="white",fg="black")
        self.lblrect.grid(row=5,column=0,pady=10)
        self.lblrect.bind("<Return>",lambda event:self.item_window.destroy())
        self.lblrect.bind("<Up>",lambda event:self.lblgenerate.focus())
        self.lblrect.bind("<Down>",lambda event:self.lbladd.focus())
        self.item_window.focus_force()
        self.item_window.resizable(0,0)
        self.item_window.bind("<Escape>",self.exit)
        self.item_window.focus_force()
        self.item_window.overrideredirect(True)
    def add(self):
        Add_Item()
    def add_b(self,event):
        self.add()
    def update(self):
        Update_item()
    def update_b(self,event):
        self.update()
    def view(self):
        fileexist=os.path.isfile("items.csv")
        if not fileexist:
            messagebox.showerror(parent=self.item_window,title="Error",message="Items File Not Found")
            self.item_window.destroy()
        else:
            webbrowser.open_new("items.csv")
    def view_b(self,event):
        self.view()
    def exit(self,event):
        self.item_window.destroy()
class Add_Item:
    def __init__(self):
        self.add_item_window=Toplevel()
        self.add_item_window.geometry("700x900+0+0")
        self.add_item_window.config(bg="light blue")
        self.lbl=Label(self.add_item_window,text="Add Item Details Here",width=29,font="Times 30 bold",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=20)
        self.frame1=LabelFrame(self.add_item_window,foreground="white",background="light blue",bd=0)
        self.frame1.grid(row=1,column=0,pady=5)
        self.labels=["Description","Size","Net Rate","M.R.P","Quantity","Type","Discount %"]
        for i in range(len(self.labels)):
            self.cur_label="label"+str(i)
            self.cur_label=t.Label(self.frame1,text=self.labels[i],bg="blue",fg="white",font="consolas 16",width=15)
            self.cur_label.grid(row=i,column=0,sticky=t.W,pady=10)
        self.disc=Entry(self.frame1,width=15,font="consolas 16",bd=0)
        self.disc.grid(row=0,column=1,padx=10)
        self.disc.focus()
        self.disc.bind("<Return>",self.go1)
        self.size=Entry(self.frame1,width=15,font="consolas 16",bd=0)
        self.size.grid(row=1,column=1,padx=20)
        self.size.bind("<Return>",self.go2)
        self.net=Entry(self.frame1,width=15,font="consolas 16",bd=0)
        self.net.grid(row=2,column=1,padx=20)
        self.reg1=self.net.register(correct)
        self.net.config(validate="key",validatecommand=(self.reg1,"%P"))
        self.net.bind("<Return>",self.go3)
        self.mrp=Entry(self.frame1,width=15,font="consolas 16",bd=0)
        self.mrp.grid(row=3,column=1,padx=20)
        self.reg2=self.mrp.register(correct)
        self.mrp.config(validate="key",validatecommand=(self.reg2,"%P"))
        self.mrp.bind("<Return>",self.go4)
        self.quant=Entry(self.frame1,width=15,font="consolas 16",bd=0)
        self.quant.grid(row=4,column=1,padx=20)
        self.reg3=self.quant.register(correct)
        self.quant.config(validate="key",validatecommand=(self.reg3,"%P"))
        self.quant.bind("<Return>",self.go5)
        self.typ=Entry(self.frame1,width=15,font="consolas 16",bd=0)
        self.typ.grid(row=5,column=1,padx=20)
        self.typ.bind("<Return>",self.go6)
        self.discount=Entry(self.frame1,width=15,font="consolas 16",bd=0)
        self.discount.grid(row=6,column=1,padx=20)
        self.discount.bind("<Return>",self.go7)
        self.save_=Button(self.frame1,text="Save",width=10,bd=4,command=self.save,font="consolas 14 bold",bg="blue",fg="white")
        self.save_.grid(row=8,column=0,pady=10)
        self.back=Button(self.frame1,text="Back",width=10,command=self.add_item_window.destroy,bd=4,font="consolas 14 bold",bg="blue",fg="white")
        self.back.grid(row=8,column=1,pady=10)
        self.add_item_window.bind("<Escape>",self.esc)
        self.add_item_window.focus_force()
        self.add_item_window.overrideredirect(True)
    def save(self):
        if (self.disc.get()).upper() =="":
            messagebox.showwarning(parent=self.add_item_window,title="Warning",message="You save blank Entries\nItem not Saved!!!")
        else:
            filename="items.csv"
            file_exists=os.path.isfile(filename)
            with open("items.csv","a",newline="") as f:
                csv_writer=DictWriter(f,fieldnames=["Description","Size","Net Rate","M.R.P","Quantity","Type","Discount","Date of item saved"])
                if not file_exists:
                    csv_writer.writeheader()
                with open("items.csv","r") as id:
                    c_s=csv.reader(id)
                    i_name=[n[0] for n in c_s]
                if (self.disc.get()).upper() in i_name:
                    messagebox.showerror(parent=self.add_item_window,title="Error",message="Item Already Exists")
                else:
                    csv_writer.writerow({
                    "Description":(self.disc.get()).upper(),
                    "Size":str((self.size.get()).upper()),
                    "Net Rate":str(self.net.get()),
                    "M.R.P":str(self.mrp.get()),
                    "Quantity":str(self.quant.get()).zfill(4),
                    "Type":self.typ.get().upper(),
                    "Discount":str(self.discount.get()),
                    "Date of item saved":date.today().strftime('%d/%m/%y')
                    })
                    messagebox.showinfo(parent=self.add_item_window,title="Successful",message="item Saved")
                    self.disc.delete(0,END)
                    self.size.delete(0,END)
                    self.net.delete(0,END)
                    self.mrp.delete(0,END)
                    self.quant.delete(0,END)
                    self.typ.delete(0,END)
                    self.discount.delete(0,END)
                    self.disc.focus()   
    def esc(self,event):
        self.add_item_window.destroy()
    def go1(self,event):
        self.size.focus()
    def go2(self,event):
        self.net.focus()
    def go3(self,event):
        self.mrp.focus()
    def go4(self,event):
        self.quant.focus()
    def go5(self,event):
        self.typ.focus()
    def go6(self,event):
        self.discount.focus()
    def go7(self,event):
        self.save()
class Update_item(Add_Item):
    def __init__(self):
        self.update_item_window=Toplevel()
        self.update_item_window.geometry("700x900+0+0")
        self.update_item_window.config(bg="light blue")
        self.lbl=Label(self.update_item_window,text="Enter The Details of Item",width=29,font="Times 30 bold ",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=2,column=0,pady=20)
        self.lab_frame=LabelFrame(self.update_item_window,foreground="white",background="light blue",bd=0)
        self.lab_frame.grid(row=3,column=0)
        self.name_label=Label(self.lab_frame,text="Item Name:",bg="blue",fg="white",font="consolas 15 ",width=15)
        self.name_label.grid(row=0,column=0,padx=10,pady=10,sticky=t.W)
        self.name_entry=Entry(self.lab_frame,width=15,font="consolas 15",bd=0)
        self.name_entry.grid(row=0,column=1,pady=10,padx=10)
        self.name_entry.focus()
        self.name_entry.bind("<Return>",self.go)
        self.update_button=t.Button(self.lab_frame,width= 10,text="Update",command=self.choice,background="blue",foreground="white",font="consolas 13",bd=2)
        self.update_button.grid(row=4,column=0,pady=10)
        self.del_button=t.Button(self.lab_frame,width= 10,text="Delete",command=self.delete,background="blue",foreground="white",font="consolas 13",bd=2)
        self.del_button.grid(row=4,column=1,padx=40,pady=10)
        self.back_button=t.Button(self.lab_frame,width= 10,text="Back",command=self.update_item_window.destroy,background="blue",foreground="white",font="consolas 13",bd=2)
        self.back_button.grid(row=4,column=2,padx=40,pady=10)
        self.update_item_window.bind("<Escape>",self.exit_b)
        self.update_item_window.overrideredirect(True)
        self.update_item_window.focus_force()
    def choice(self):
        if messagebox.askyesno(parent=self.update_item_window,title="Update Item",message="Are you Sure!"):
            name=(self.name_entry.get()).upper()
            flag=False
            with open("items.csv","r") as f:
                csv_reader=csv.reader(f)
                full_data=[]
                data_=[]
                for line in csv_reader:
                    full_data.append(line)
                    if name == line[0]:
                        data_.append(line)
                        full_data.remove(line)
                        flag=True
                with open("items.csv","w",newline="") as f1:
                    wo=csv.writer(f1)
                    for line in full_data:
                        wo.writerow(line)
                if flag==True:
                    self.update_item_window.destroy()
                    super().__init__()
                    self.disc.insert(0,data_[0][0])
                    self.size.insert(0,data_[0][1])
                    self.net.insert(0,data_[0][2])
                    self.mrp.insert(0,data_[0][3])
                    self.quant.insert(0,data_[0][4])
                    self.typ.insert(0,data_[0][5])
                    self.discount.insert(0,data_[0][6])
                else:
                    messagebox.showerror(parent=self.update_item_window,title="Error",message="Not Found")
                    self.name_entry.delete(0,END)
    def delete(self):
        if messagebox.askyesno(parent=self.update_item_window,title="Delete Item",message="Are you Sure!"):
            name=(self.name_entry.get()).upper()
            flag=False
            with open("items.csv","r") as f:
                csv_reader=csv.reader(f)
                full_data=[]
                for line in csv_reader:
                    full_data.append(line)
                    if name==line[0]:
                        full_data.remove(line)
                        flag=True
            with open("items.csv","w",newline="") as f1:
                wo=csv.writer(f1)
                for line in full_data:
                    wo.writerow(line)
            if flag==True:
                messagebox.showinfo(parent=self.update_item_window,title="Success",message="Item Deleted")
                self.name_entry.delete(0,END)
            else:
                messagebox.showerror(parent=self.update_item_window,title="Error",message="Not Found")
                self.name_entry.delete(0,END)
    def exit_b(self,event):
        self.update_item_window.destroy()
    def go(self,event):
        if self.name_entry.get()=="":
            Shortcuts_menu.cost_n(self.name_entry,"items.csv","View All Items Name            Esc->Exit",["Description","Size","Net Rate","M.R.P","Quantity","Type","Discount","Date of item saved"],4,0,self.update_item_window,'coral','brown')
        else:
            self.choice()
#**************************************INVOICE**************************
            
class Invoice:
    def __init__(self):
        self.invoice_window=Toplevel()
        self.invoice_window.geometry("700x900+0+0")
        self.invoice_window.config(bg="light blue")
        self.lbl=Label(self.invoice_window,text="Invoice Data Handling Menu",font="Times 30 bold",width=29,fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.label_frame=t.LabelFrame(self.invoice_window,foreground="white",background="light blue",bd=5)
        self.label_frame.grid(row=1,column=0,pady=10)
        self.add_b=Button(self.label_frame,text="Add",command=self.add_invo,font="consolas 20 bold",bg="white",fg="black",)
        self.add_b.grid(row=0,column=0,pady=10,padx=10)
        self.add_b.focus()
        self.add_b.bind("<Return>",self.invoice_bind)
        self.add_b.bind("<Up>",lambda event: self.back.focus())
        self.add_b.bind("<Down>",lambda event: self.update_b.focus())
        self.update_b=Button(self.label_frame,text="Delete Invoice",command=self.delete,font="consolas 20 bold",bg="white",fg="black")
        self.update_b.grid(row=1,column=0,pady=10)
        self.update_b.bind("<Return>",self.delete_bind)
        self.update_b.bind("<Up>",lambda event: self.add_b.focus())
        self.update_b.bind("<Down>",lambda event: self.day_register_b.focus())
        self.day_register_b=Button(self.label_frame,text="Day Register",command=self.register,font="consolas 20 bold",bg="white",fg="black")
        self.day_register_b.grid(row=3,column=0,pady=10)
        self.day_register_b.bind("<Return>",self.register_bind)
        self.day_register_b.bind("<Up>",lambda event: self.update_b.focus())
        self.day_register_b.bind("<Down>",lambda event: self.print_b.focus())
        self.print_b=Button(self.label_frame,text="Invoice(Print/View)",command=self.print,font="consolas 20 bold",bg="white",fg="black")
        self.print_b.grid(row=4,column=0,pady=10)
        self.print_b.bind("<Return>",self.print_bind)
        self.print_b.bind("<Up>",lambda event: self.day_register_b.focus())
        self.print_b.bind("<Down>",lambda event: self.summary_b.focus())
        self.summary_b=Button(self.label_frame,text="Summary of Invoices",command=self.summary,font="consolas 20 bold",bg="white",fg="black")
        self.summary_b.grid(row=5,column=0,pady=10,padx=15)
        self.summary_b.bind("<Return>",self.summary_bind)
        self.summary_b.bind("<Up>",lambda event: self.print_b.focus())
        self.summary_b.bind("<Down>",lambda event: self.back.focus())
        self.back=Button(self.label_frame,text="Back(Esc)",command=self.invoice_window.destroy,font="consolas 20 bold",bg="white",fg="black")
        self.back.grid(row=6,column=0,pady=10)
        self.back.bind("<Return>",self.exit)
        self.back.bind("<Up>",lambda event: self.summary_b.focus())
        self.back.bind("<Down>",lambda event: self.add_b.focus())
        self.invoice_window.focus_force()
        self.invoice_window.bind("<Escape>",self.exit)
        self.invoice_window.focus_force()
        self.invoice_window.overrideredirect(True)
    def add_invo(self):
        Invoice_Add()
    def invoice_bind(self,event):
        self.add_invo()
    def delete(self):
        Invoice_Delete()
    def delete_bind(self,event):
        self.delete()
    def print(self):
        Invoice_Print('light blue','blue')
    def print_bind(self,event):
        self.print()
    def summary(self):
        Invoice_summary('light blue','blue')
    def summary_bind(self,event):
        self.summary()
    def register(self):
        Day_Register('light blue','blue')
    def register_bind(self,event):
        self.register()
    def exit(self,event):
        self.invoice_window.destroy()
class Invoice_Add:
    def __init__(self):
        self.add_inv=Toplevel()
        self.add_inv.geometry("1350x750")
        self.add_inv.state('zoomed')
        self.add_inv.title('Invoice Bills')
        self.add_inv.config(bg="light blue")
        self.lab=Label(self.add_inv,text="Invoice Bills ",font="Times 30 bold",bg="blue",fg="white",bd=1)
        self.lab.grid(row=0,column=0,pady=10)
        self.inv_frame1=LabelFrame(self.add_inv,bg="light blue",bd=0)
        self.inv_frame1.grid(row=1,column=0)
        self.inv_no=Label(self.inv_frame1,text="Invoice no",bg="blue",fg="white",width=10,font="consolas 13")
        self.inv_no.grid(row=0,column=0,pady=5,padx=20)
        filename="invoice_data.csv"
        file_exists=os.path.isfile(filename)
        if not file_exists:
            self.invoice_no=1
            self.invoice_no=str(self.invoice_no).zfill(4)
        else:
            with open(filename,"r") as iv:
                data=csv.reader(iv)
                in_no=list(data)
                self.invoice_no=int(in_no[len(in_no)-1][0])+1
                self.invoice_no=str(self.invoice_no).zfill(4)
        self.inv_ent=Entry(self.inv_frame1,width=10,fg="black",font="consolas 15",bd=0,bg="white")
        self.inv_ent.insert(END,self.invoice_no)
        self.inv_ent.configure(state="readonly")
        self.inv_ent.grid(row=0,column=1,padx=20)
        self.date=Label(self.inv_frame1,text="Date",bg="blue",fg="white",width=10,font="consolas 13")
        self.date.grid(row=1,column=0,pady=5,padx=10)
        self.date_ent=Entry(self.inv_frame1,width=10,fg="black",font="consolas 15",bd=0,bg="light blue")
        self.date_ent.insert(END,date.today().strftime('%d/%m/%y'))
        self.date_ent.grid(row=1,column=1,pady=10)
        self.date_ent.bind("<Return>",self.go1)
        self.cost=Label(self.inv_frame1,text="Customer",bg="blue",fg="white",width=10,font="consolas 13")
        self.cost.grid(row=2,column=0,pady=5,padx=10)
        self.cost_ent=Entry(self.inv_frame1,width=15,fg="black",font="consolas 15",bd=0,bg="light blue")
        self.cost_ent.grid(row=2,column=1,pady=10)
        self.cost_ent.focus_force()
        self.cost_ent.bind("<Return>",self.go2)
        self.view=Button(self.inv_frame1,text="View All Customers Name",font="consolas 12",command=self.view_name,bg="blue",fg="white",bd=0)
        self.view.grid(row=2,column=2,pady=10,padx=20)
        self.inv_frame2=LabelFrame(self.add_inv,bg="light blue",bd=0)
        self.inv_frame2.grid(row=3,column=0,padx=10)
        self.labels=["Item Description","Quantity","Rate","Amount"]
        for i in range(len(self.labels)):
            self.cur_label="label"+str(i)
            self.cur_label=t.Label(self.inv_frame2,text=self.labels[i],bg="blue",fg="white",font="consolas 13",width=15)
            self.cur_label.grid(row=0,column=i)
        self.itm=Entry(self.inv_frame2,width=15,font="consolas 15 bold",bg="light blue",bd=0)
        self.itm.grid(row=1,column=0)
        self.itm.bind("<Return>",self.go3)
        self.itm.bind("<Down>",self.fini)
        self.quant=Entry(self.inv_frame2,width=10,font="consolas 13",bg="light blue",bd=0)
        self.quant.grid(row=1,column=1,padx=10)
        self.reg=self.quant.register(correct)
        self.quant.config(validate="key",validatecommand=(self.reg,"%P"))
        self.quant.bind("<Return>",self.go4)
        self.rate=Entry(self.inv_frame2,width=10,font="consolas 13",bg="light blue",bd=0)
        self.rate.grid(row=1,column=2,padx=10)
        self.reg1=self.rate.register(correct)
        self.rate.config(validate="key",validatecommand=(self.reg1,"%P"))
        self.rate.bind("<Return>",self.go5)    
        self.amount=Entry(self.inv_frame2,width=10,font="consolas 13",bg="light blue",bd=0)
        self.amount.grid(row=1,column=3,padx=10)
        self.viewitm=Button(self.inv_frame2,text="View All Items Name",font="consolas 11",command=self.view_item,bg="blue",fg="white",bd=0)
        self.viewitm.grid(row=0,column=4,pady=20,padx=20)
        self.done=Button(self.inv_frame2,text="Add to Cart",width=17,command=self.done_itm,font="consolas 12",bg="blue",fg="white",bd=0)
        self.done.grid(row=1,column=4,padx=10)
        self.done.bind("<Return>",self.go6)
        self.inv_frame3=LabelFrame(self.add_inv,width=750,height=220,bg="light blue",bd=1)
        self.inv_frame3.grid(row=4,column=0,padx=5,pady=10)
        self.lab=Label(self.inv_frame3,text="Cart",width=80,font="consolas 13",bg="blue",fg="white")
        self.lab.grid(row=0,column=0)
        self.lab2=Label(self.inv_frame3,text="Max Size 5 items",width=80,font="consolas 13",bg="blue",fg="white")
        self.lab2.grid(row=6,column=0)
        self.inv_frame4=LabelFrame(self.add_inv,bg="light blue",bd=0)
        self.inv_frame4.grid(row=5,column=0,padx=5,pady=10)
        self.total_amount=0
        self.total_quantity=0
        self.cart_list=[]
        self.sno=1   
        self.temp_cart=[]
        self.add_inv.bind("<Escape>",self.exit)
        self.add_inv.focus_force()
        self.add_inv.resizable(0,0)
    def done_itm(self):
        if self.itm.get().upper() == "":
            messagebox.showerror(parent=self.add_inv,title="Error",message="Please Add Item description")
            self.itm.focus_force()
        else:
            self.local_tax=format(self.am *0.025,".2f")
            self.inter_tax=format(float(self.local_tax)*2,".2f")
            self.data=[self.itm.get().upper(),self.quant.get(),self.rate.get(),self.am,self.local_tax,self.inter_tax]
            with open("items.csv","r") as f2:
                csv_reader=csv.reader(f2)
                items_name=[line[0] for line in csv_reader]
            if self.data[0] not in items_name:
                messagebox.showerror(parent=self.add_inv,title="Error",message="Item Not Found")
                self.itm.focus_set()
            else:
                if self.sno==6:
                    messagebox.showerror(parent=self.add_inv,title="Error",message="Cart Size is Full")
                    self.itm.delete(0,END)
                    self.quant.delete(0,END)
                    self.rate.delete(0,END)
                    self.amount.configure(state="normal")
                    self.amount.delete(0,END)
                    self.finish()
                    self.pcen.focus_force()  
                else:
                    self.temp_cart.append([self.itm.get().upper(),self.quant.get(),self.rate.get(),self.am])
                    self.total_amount+=self.am
                    self.total_quantity+=int(self.quant.get())
                    self.itm.focus_force()
                    self.la=Label(self.inv_frame3,text=f"{self.sno}. {self.data[0]}         {self.data[1]}       {self.data[2]}       {self.data[3]}",bg="blue",fg="white",font="consolas 12")
                    self.la.grid(row=self.sno,column=0,sticky=W)
                    self.tot=Label(self.inv_frame4,text="Total",bg="blue",width=10,fg="white",bd=0,font="consolas 13")
                    self.tot.grid(row=0,column=0)
                    self.tot_q=Entry(self.inv_frame4,fg="black",width=10,font="consolas 13 bold",bd=0,bg="light blue")
                    self.tot_q.insert(END,self.total_quantity)
                    self.tot_q.configure(state="readonly")
                    self.tot_q.grid(row=0,column=1,padx=10)
                    self.tot_a=Entry(self.inv_frame4,fg="black",width=12,font="consolas 13 bold",bd=0,bg="light blue")
                    self.tot_a.insert(END,self.total_amount)
                    self.tot_a.configure(state="readonly")
                    self.tot_a.grid(row=0,column=2,padx=10)
                    self.fin=Button(self.inv_frame4,text="Finish",bd=0,command=self.finish,font="consolas 13",bg="blue",fg="white")
                    self.fin.grid(row=0,column=3)
                    self.fin.bind("<Return>",self.go13) 
                    self.sno+=1
                    self.itm.delete(0,END)
                    self.quant.delete(0,END)
                    self.rate.delete(0,END)
                    self.amount.configure(state="normal")
                    self.amount.delete(0,END)
                    self.itm.focus_force()
                    self.cart_list.append(self.data)
    def finish(self):
        self.fin_w=Label(self.inv_frame4,bd=0,bg="light blue",width=12,height=2)
        self.fin_w.grid(row=0,column=3)
        self.pc=Label(self.inv_frame4,text="Pack/Frt",font="consolas 13",width=10,bg="blue",fg="white",bd=0)
        self.pc.grid(row=1,column=0,pady=5)
        self.pcen=Entry(self.inv_frame4,fg="black",bg="white",width=10,font="consolas 13",bd=0)
        self.pcen.grid(row=1,column=1,pady=5,padx=10)
        self.pcen.insert(END,0)
        self.pcen.focus_force()
        self.reg5=self.pcen.register(correct)
        self.pcen.config(validate="key",validatecommand=(self.reg5,"%P"))
        self.pcen.bind("<Return>",self.go7)
        self.tax=Label(self.inv_frame4,text="Tax",font="consolas 13",width=10,bg="blue",fg="white",bd=0)
        self.tax.grid(row=1,column=2,pady=5,padx=5)
        self.tax_combobox=ttk.Combobox(self.inv_frame4,width=12,font="consolas 13",state="readonly" )
        self.tax_combobox["values"]=('GST  5%','GST 12%','GST 18%','GST 28%','GST  0%') 
        self.tax_combobox.grid(row=1,column=3,pady=12,padx=5) 
        self.tax_combobox.current(0)
        self.tax_combobox.bind("<Return>",self.go8)
        self.trans=Label(self.inv_frame4,text="Transport",font="consolas 13",width=10,bg="blue",fg="white",bd=0)
        self.trans.grid(row=2,column=0,pady=5)
        self.transen=Entry(self.inv_frame4,fg="black",bg="white",width=10,font="consolas 13",bd=0)
        self.transen.grid(row=2,column=1,pady=5,padx=10)
        self.transen.bind("<Return>",self.go9)
        self.way=Label(self.inv_frame4,text="Way Bill",font="consolas 13",width=10,bg="blue",fg="white",bd=0)
        self.way.grid(row=2,column=2,pady=5,padx=5)
        self.wayen=Entry(self.inv_frame4,fg="black",bg="white",width=14,font="consolas 13",bd=0)
        self.wayen.grid(row=2,column=3,pady=5,padx=20)
        self.reg3=self.wayen.register(correct)
        self.wayen.config(validate="key",validatecommand=(self.reg3,"%P"))
        self.wayen.bind("<Return>",self.go10)
        self.order=Label(self.inv_frame4,text="Order No",font="consolas 13",width=10,bg="blue",fg="white",bd=0)
        self.order.grid(row=2,column=4,pady=5,padx=20)
        self.orderen=Entry(self.inv_frame4,fg="black",bg="white",width=14,font="consolas 13",bd=0)
        self.orderen.grid(row=2,column=5,pady=5,padx=10)
        self.reg4=self.orderen.register(correct)
        self.orderen.config(validate="key",validatecommand=(self.reg4,"%P"))
        self.orderen.bind("<Return>",self.go11)
    def fini(self,event):
        self.fin.focus_force()
    def go13(self,event):
        self.finish()
    def view_name(self):
        Shortcuts_menu.cost_n(self.cost_ent,"costumers.csv","View All Customers Name            Esc->Exit",["Customer Name","Address","State","TIN/GST no","Transport","Phone","GST","Date"],7,0,self.add_inv,'lavender','brown')
    def view_item(self):
        Shortcuts_menu.cost_n(self.itm,"items.csv","View All Items Name            Esc->Exit",["Description","Size","Net Rate","M.R.P","Quantity","Type","Discount","Date of item saved"],4,0,self.add_inv,'lavender','brown')
    def go1(self,event):
        self.cost_ent.focus()
    def go2(self,event):
        if self.cost_ent.get().upper() !="":
            fileexist11=os.path.isfile("costumers.csv")
            if not fileexist11:
                messagebox.showerror(parent=self.add_inv,title="Error",message="Customer's file  not found")
                self.add_inv.destroy()
            with open("costumers.csv","r") as f3:
                csv_reader=csv.reader(f3)
                costumer_name=[line[0] for line in csv_reader]
            if self.cost_ent.get().upper()  not in costumer_name:
                mbox=messagebox.askyesno(parent=self.add_inv,title="Account Not Found in File",message="Please save account details!!")  
                if mbox is True:
                    self.add_inv.destroy()
                    Add('light blue','blue')
            else:
                self.itm.focus()
        else:
            self.view_name()
        
    def go3(self,event):
        if self.itm.get().upper() !="":
            self.quant.focus()
        else:
            self.view_item()

    def go4(self,event):
        with open("items.csv","r") as r:
            csv_data=csv.reader(r)
            items_details=[line for line in csv_data if self.itm.get().upper()==line[0]]
        self.rate.insert(END,items_details[0][2])
        self.rate.focus()

    def go5(self,event):
        self.qu=int(self.quant.get())
        self.ra=int(self.rate.get())
        self.am=float(self.qu*self.ra)
        self.amount.insert(END,self.am)
        self.amount.configure(state="readonly")
        self.done.focus_force()
    def go6(self,event):
        self.done_itm()
    def go7(self,event):
        self.tax_combobox.focus_force()
    def go8(self,event):
        self.transen.focus_force()
    def go9(self,event):
        self.wayen.focus_force()
    def go10(self,event):
        self.orderen.focus_force()
    def go11(self,event):
        self.save_final=Button(self.inv_frame4,text="save",command=self.save_final_func,width=10,bd=1,font="consolas 15",bg="blue",fg="white")
        self.save_final.grid(row=4,column=3,pady=20)
        self.save_final.focus_force()
        self.save_final.bind("<Return>",self.go12)
        self.cancel=Button(self.inv_frame4,text="cancel",command=self.cancel_final,width=10,bd=1,font="consolas 15",bg="blue",fg="white")
        self.cancel.grid(row=4,column=4,padx=10,pady=20)
    def cancel_final(self):
        m=messagebox.askyesno(parent=self.add_inv,title="cancel saving",message="Are you sure")
        if m is True:
            self.add_inv.destroy()
    def go12(self,event):
        self.save_final_func()
    def save_final_func(self):
        mbo=messagebox.askyesno(parent=self.add_inv,title="save and Print",message="Are you Sure")
        if self.tax_combobox.get()=="GST  5%":
            self.tax_m=(5*self.total_amount)/100
        elif self.tax_combobox.get()=="GST 12%":
            self.tax_m=(12*self.total_amount)/100
        elif self.tax_combobox.get()=="GST 18%":
            self.tax_m=(18*self.total_amount)/100
        elif self.tax_combobox.get()=="GST 28%":
            self.tax_m=(28*self.total_amount)/100
        elif self.tax_combobox.get()=="GST  0%":
            self.tax_m=0
        self.gt=self.total_amount + self.tax_m +int(self.pcen.get())
        if mbo==True:
            for i in self.temp_cart:
                file_exists_=os.path.isfile("items_data.csv")
                with open("items_data.csv","a",newline="") as f__i:
                    csv_writer=DictWriter(f__i,fieldnames=["item","date","invoice_no","costumer","item_quantity","item_rate","item_amount"])
                    if not file_exists_:
                        csv_writer.writeheader()
                    csv_writer.writerow({
                        "item":str(i[0]),
                        "date":str(date.today().strftime('%d/%m/%y')),
                        "invoice_no":str(self.invoice_no).zfill(4),
                        "costumer":str(self.cost_ent.get().upper()),
                        "item_quantity":str(i[1]),
                        "item_rate":str(i[2]),
                        "item_amount":str(i[3])
                    })
            with open("items.csv","r") as f_1:    #after sale of particular item it will subtract those items from items file
                i_d=csv.reader(f_1)
                items_data=list(i_d)
                for line in items_data:
                    for items_ in self.temp_cart:
                        if items_[0] in line:
                            line[4]=int(line[4])-int(items_[1])
            with open("items.csv","w",newline="") as f_2:
                w_o=csv.writer(f_2)
                for line_1 in items_data:
                    w_o.writerow(line_1)  
            file_exists_acc=os.path.isfile("accounts_data.csv")
            with open("accounts_data.csv","a",newline="") as f__acc:
                csv_writer_ac=DictWriter(f__acc,fieldnames=["party_name","Date","Particulars","Voucher_type","Debit","Credit","Balance"])
                if not file_exists_acc:
                    csv_writer_ac.writeheader()
                csv_writer_ac.writerow({
                  "party_name":str(self.cost_ent.get().upper()),
                  "Date":str(date.today().strftime('%d/%m/%y')),
                  "Particulars":str(self.invoice_no).zfill(4),
                  "Voucher_type":"Sale",
                  "Debit":str(format(self.gt,".2f")),
                  "Credit":"",
                  "Balance":str(format(self.gt,".2f")),
                })
            file_exists=os.path.isfile("invoice_data.csv")
            with open("invoice_data.csv","a",newline="") as f:
                csv_writer=DictWriter(f,fieldnames=["invoice_no","date","costumer","cart","total_quantity","sub_total","local_gst_amount","total_amount","pack/frt","tax","transport","way","orderno"])
                if not file_exists:
                    csv_writer.writeheader()
                csv_writer.writerow({
                    "invoice_no":str(self.invoice_no).zfill(4),
                    "date":self.date_ent.get(),
                    "costumer":str(self.cost_ent.get().upper()),
                    "cart":self.cart_list,
                    "total_quantity":str(self.total_quantity),
                    "sub_total":str(self.total_amount),
                    "local_gst_amount":format(self.tax_m/2,".2f"),
                    "total_amount":str(format(self.gt,".2f")),
                    "pack/frt": str(self.pcen.get()),
                    "tax":str(format(self.tax_m,".2f")),
                    "transport":str(self.transen.get().upper()),
                    "way":str(self.wayen.get()),
                    "orderno":str(self.orderen.get())
                })
                messagebox.showinfo(parent=self.add_inv,title="Succesfull",message="Invoice Saved Successfully") 
            Reports.pdf_func((self.cost_ent.get().upper()),self.invoice_no)
            time.sleep(2)
            self.add_inv.destroy()    
    def exit(self,event):
        self.add_inv.destroy()   
class Invoice_Delete:
    def __init__(self):
        self.inv_del=Toplevel()
        self.inv_del.geometry("700x900+0+0")
        self.inv_del.config(bg="light blue")
        self.lbl=Label(self.inv_del,text="Delete Invoice",font="Times 30 bold",width=29,fg="white",bg="blue",bd=10)
        self.lbl.grid(row=2,column=0,pady=10)
        self.in_frame=LabelFrame(self.inv_del,bd=0,bg="light blue")
        self.in_frame.grid(row=3,column=0)
        self.in_ab=Label(self.in_frame,text=' Invoice No ',bg="blue",fg="white",width=10,font="consolas 15")
        self.in_ab.grid(row=0,column=1,padx=10,pady=10,sticky=t.W)
        self.in_en=Entry(self.in_frame,width=15,font="consolas 15",bd=0,fg="black",bg="white")
        self.in_en.grid(row=0,column=2,padx=10,pady=10)
        self.in_en.focus_force()
        self.in_en.bind("<Return>",self.ent_b)
        self.del_button=t.Button(self.in_frame,width= 10,text="Delete",command=self.choice,background="blue",foreground="white",font="consolas 13",bd=3)
        self.del_button.grid(row=4,column=1,padx=40,pady=10)
        self.back_button=t.Button(self.in_frame,width= 10,text="Back",command=self.inv_del.destroy,background="blue",foreground="white",font="consolas 13",bd=3)
        self.back_button.grid(row=4,column=2,padx=40,pady=10)
        self.inv_del.bind("<Escape>",self.exit)
        self.inv_del.focus_force()
        self.inv_del.overrideredirect(True)
    def exit(self,event):
        self.inv_del.destroy()
    def ent_b(self,event):
        if self.in_en.get() =="":
            Shortcuts_menu.inv_n(self.in_en,"invoice_data.csv","View all invoices",self.inv_del)
        else:
            self.choice()
    def choice(self):
        if self.in_en.get()=="":
            messagebox.showerror(parent=self.inv_del,title="Error",message="Entry box is empty")
            self.in_en.focus()
        else:
            if messagebox.askyesno(parent=self.inv_del,title="Delete Invoice",message="Are You Sure!!!"):
                invoice_number=self.in_en.get()
                flag=False
                with open("invoice_data.csv","r") as f:
                    csv_reader=csv.reader(f)
                    full_data=[]
                    data=[]
                    for line in csv_reader:
                        full_data.append(line)
                        if invoice_number in line:
                            data.append(line)
                            full_data.remove(line)
                            flag=True
                    with open("invoice_data.csv","w",newline="") as f1:
                        wo=csv.writer(f1)
                        for line in full_data:
                            wo.writerow(line)
                    if flag==False:
                        messagebox.showerror(parent=self.inv_del,title="Error",message=" Invoice Not Found")
                        self.inv_del.destroy()
                    else:
                        messagebox.showinfo(parent=self.inv_del,title="Successful",message=" Invoice Delete Successfully")
                        self.inv_del.destroy()
class Day_Register:
    def __init__(self,bgf,bgh):
        self.bgf=bgf
        self.bgh=bgh
        self.inv_day=Toplevel()
        self.inv_day.geometry("700x900+0+0")
        self.inv_day.config(bg=self.bgf)
        self.lbl=Label(self.inv_day,text="Day-Register",font="Times 30 bold",fg="white",bg=self.bgh,width=30,bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.in_frame=LabelFrame(self.inv_day,bd=0,bg=self.bgf)
        self.in_frame.grid(row=1,column=0)
        self.lbldf=Label(self.in_frame,text="Date from",font="consolas 15",fg="white",bg=self.bgh,width=13)
        self.lbldf.grid(row=1,column=2,pady=10)
        self.lbl_dfe=Entry(self.in_frame,width=10,font="consolas 15",bg=self.bgf,fg="black",bd=0)
        self.lbl_dfe.grid(row=1,column=3,pady=10,padx=5)
        self.lbl_dfe.insert(END,"01/02/20")
        self.lbl_dfe.focus()
        self.lbl_dfe.bind("<Return>",self.bind_d)
        self.lbldt=Label(self.in_frame,text=" To Date",font="consolas 15",fg="white",bg=self.bgh,width=13)
        self.lbldt.grid(row=1,column=4,pady=10,padx=25)
        self.lbl_dte=Entry(self.in_frame,width=10,font="consolas 15",bg=self.bgf,fg="black",bd=0)
        self.lbl_dte.grid(row=1,column=5,pady=10,padx=10)
        self.lbl_dte.insert(END,f"{date.today().strftime('%d/%m/%y')}")
        self.lbl_dte.configure(state="readonly")
        self.sale_lbl=Label(self.in_frame,text="Select",font="consolas 15",fg="white",bg=self.bgh,width=13)
        self.sale_lbl.grid(row=4,column=3,pady=10,padx=10)
        self.sale_combobox=ttk.Combobox(self.in_frame,width=15,font="consolas 16",state="readonly" )
        self.sale_combobox["values"]=('PARTICULAR','ALL')
        self.sale_combobox.grid(row=4,column=4,pady=20) 
        self.sale_combobox.current(0)
        self.sale_combobox.bind("<Return>",self.bind_c)
        self.inv_day.bind("<Escape>",self.exit)
        self.inv_day.focus_force()
        self.inv_day.overrideredirect(True)
    def bind_c(self,event):
        if self.sale_combobox.get()=="PARTICULAR":
            self.name_l=Label(self.in_frame,text="Customer Name",font="consolas 15",fg="white",bg=self.bgh,width=15)
            self.name_l.grid(row=5,column=3,pady=15)
            self.name_e=Entry(self.in_frame,width=15,font="consolas 15 bold",bg="white",fg="black",bd=0)
            self.name_e.grid(row=5,column=4)
            self.name_e.focus()
            self.name_e.bind("<Return>",self.cl)
            self.pr=Button(self.in_frame,width=10,text="Print",font="consolas 14",bg=self.bgh,fg="white",command=self.choice)
            self.pr.grid(row=6,column=3)
            self.bck=Button(self.in_frame,width=10,text="Back",font="consolas 14",bg=self.bgh,fg="white",command=self.inv_day.destroy)
            self.bck.grid(row=6,column=4)
        else:
            if messagebox.askyesno(parent=self.inv_day,title="Print Sale Register",message="Are You Sure!!!"):
                a=Reports.sales_register('ALL_INV',self.lbl_dfe.get(),self.inv_day)
                if a ==False:
                     messagebox.showerror(parent=self.inv_day,title="Error",message="No Invoice Found")
    def cl(self,event):
        if self.name_e.get()=="":
            Shortcuts_menu.cost_n(self.name_e,"costumers.csv","View All Customers Name            Esc->Exit",["Costumer Name","Address","State","TIN/GST no","Transport","Phone","GST","Date"],7,0,self.inv_day,self.bgf,self.bgh)
        else:
            self.choice()
    def choice(self):
        if self.name_e.get()=="":
            messagebox.showerror(parent=self.inv_day,title="Error",message="Entry box is Empty")
            self.name_e.focus()
        else:
            if messagebox.askyesno(parent=self.inv_day,title="Print Sale Register",message="Are You Sure!!!"):
                a=Reports.sales_register(self.name_e.get().upper(),self.lbl_dfe.get(),self.inv_day)
                if a ==False:
                    messagebox.showerror(parent=self.inv_day,title="Error",message="No Invoice Found")
                    self.name_e.delete(0,END)
                    self.name_e.focus()
                else:
                    time.sleep(2)
                    self.inv_day.destroy()
    def bind_d(self,event):
        self.sale_combobox.focus()
    def exit(self,event):
        self.inv_day.destroy()      
class Invoice_Print:
    def __init__(self,bgf,bgh):
        self.bgf=bgf
        self.bgh=bgh
        self.inv_pr=Toplevel()
        self.inv_pr.geometry("700x900")
        self.inv_pr.config(bg=self.bgf)
        self.lbl=Label(self.inv_pr,text="Print Invoice",width=30,font="Times 30 bold",fg="white",bg=self.bgh,bd=10)
        self.lbl.grid(row=1,column=0,pady=10)
        self.in_frame=LabelFrame(self.inv_pr,bd=0,bg=self.bgf)
        self.in_frame.grid(row=3,column=0,pady=30)
        self.in_ab=Label(self.in_frame,text=' Invoice No ',bg=self.bgh,fg="white",width=10,font="consolas 15")
        self.in_ab.grid(row=0,column=0,padx=10,pady=10,sticky=t.W)
        self.in_en=Entry(self.in_frame,width=15,font="consolas 15",bg="white",fg="black",bd=0)
        self.in_en.grid(row=0,column=1,pady=10)
        self.in_en.focus_force()
        self.cur_b=Button(self.in_frame,text="Last Bill",command=self.current_inv,width=10,bg=self.bgh,fg="white",font="consolas 14")
        self.cur_b.grid(row=4,column=0,pady=20)
        self.pr_b=Button(self.in_frame,text="Print",command=self.choice,width=10,bg=self.bgh,fg="white",font="consolas 14")
        self.pr_b.grid(row=4,column=1,padx=40,pady=20)
        self.bck_b=Button(self.in_frame,text="Back",command=self.inv_pr.destroy,width=10,bg=self.bgh,fg="white",font="consolas 14")
        self.bck_b.grid(row=4,column=2,padx=40,pady=20)
        self.in_en.bind("<Return>",self.ent_b)
        self.inv_pr.bind("<Escape>",self.exit)
        self.inv_pr.focus_force()
        self.inv_pr.overrideredirect(True)
    def exit(self,event):
        self.inv_pr.destroy()
    def ent_b(self,event):
        if self.in_en.get() =="":
            Shortcuts_menu.inv_n(self.in_en,"invoice_data.csv","View all invoices",self.inv_pr)
        else:
            self.choice()
    def current_inv(self):
        if messagebox.askyesno(parent=self.inv_pr,title="Print Invoice",message="Are You Sure!!!"):
            fileexist=os.path.isfile("current_invoice_pdf.pdf")
            if not fileexist:
                messagebox.showerror(parent=self.inv_pr,title="Error",message="You haven't made any Invoice Yet")
            else:
                webbrowser.open_new("current_invoice_pdf.pdf")
    def choice(self):
        if self.in_en.get()=="":
            messagebox.showerror(parent=self.inv_pr,title="Error",message="Entry Box is Empty")
            self.in_en.focus()
        else:
            if messagebox.askyesno(parent=self.inv_pr,title="Print Invoice",message="Are You Sure!!!"):
                invoice_number=self.in_en.get()
                with open("invoice_data.csv","r") as f:
                    data=csv.reader(f)
                    costumer_name=[line[2] for line in data if invoice_number==line[0]]
                    Reports.pdf_func(costumer_name[0],invoice_number)
                    time.sleep(2)
                    self.inv_pr.destroy()
class Invoice_summary:
    def __init__(self,bgf,bgh):
        self.bgf=bgf
        self.bgh=bgh
        self.sum_day=Toplevel()
        self.sum_day.geometry("700x900+0+0")
        self.sum_day.config(bg=self.bgf)
        self.lbl=Label(self.sum_day,text="Invoice Summary",width=29,font="Times 30 bold",fg="white",bg=self.bgh,bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.in_frame=LabelFrame(self.sum_day,bd=0,bg=self.bgf)
        self.in_frame.grid(row=2,column=0,padx=10,pady=30)
        self.lbldf=Label(self.in_frame,text="Date from",font="consolas 15",fg="white",bg=self.bgh,width=13)
        self.lbldf.grid(row=1,column=2,pady=10)
        self.lbl_dfe=Entry(self.in_frame,width=10,font="consolas 15",bg=self.bgf,fg="black",bd=0)
        self.lbl_dfe.grid(row=1,column=3,pady=10,padx=5)
        self.lbl_dfe.insert(END,"01/02/20")
        self.lbl_dfe.focus()
        self.lbl_dfe.bind("<Return>",self.open_)
        self.lbldt=Label(self.in_frame,text=" To Date",font="consolas 15",fg="white",bg=self.bgh,width=13)
        self.lbldt.grid(row=1,column=4,pady=10,padx=25)
        self.lbl_dte=Entry(self.in_frame,width=10,font="consolas 15",bg=self.bgf,fg="black",bd=0)
        self.lbl_dte.grid(row=1,column=5,pady=10,padx=10)
        self.lbl_dte.insert(END,f"{date.today().strftime('%d/%m/%y')}")
        self.lbl_dte.configure(state="readonly")
        self.pr=Button(self.in_frame,width=10,text="Print",font="consolas 14",bg=self.bgh,fg="white",command=self.open)
        self.pr.grid(row=2,column=3,pady=20)
        self.bck=Button(self.in_frame,width=10,text="Back",font="consolas 14",bg=self.bgh,fg="white",command=self.sum_day.destroy)
        self.bck.grid(row=2,column=4,pady=20)
        self.sum_day.bind("<Escape>",self.exit)
        self.sum_day.focus_force()
        self.sum_day.overrideredirect(True)
    def open(self):
        if messagebox.askyesno(parent=self.sum_day,title="print PDF",message="Invoice Summary"):
            Reports.summary_pdf(self.lbl_dfe.get(),self.sum_day)
            time.sleep(2)
            self.sum_day.destroy()
    def open_(self,event):
        self.open()
    def exit(self,event):
        self.sum_day.destroy()   
#**************************************Report**************************************
class Report:
    def __init__(self):
        self.report_window=Toplevel()
        self.report_window.geometry("700x900+0+0")
        self.report_window.config(bg="light blue")
        self.lbl=Label(self.report_window,text="Stock Menu",width=29,font="Times 30 bold",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.label_frame=LabelFrame(self.report_window,foreground="white",background="light blue",bd=5)
        self.label_frame.grid(row=1,column=0,padx=30,pady=20)
        self.cr=Button(self.label_frame,text="Customer Report",command=self.register,font="consolas 20 bold",bg="white",fg="black",)
        self.cr.grid(row=0,column=0,pady=10,padx=10)
        self.cr.focus()
        self.cr.bind("<Return>",self.register_bind)
        self.cr.bind("<Up>",lambda event: self.back.focus())
        self.cr.bind("<Down>",lambda event: self.ir.focus())
        self.ir=Button(self.label_frame,text="Item Report",command=self.item_report,font="consolas 20 bold",bg="white",fg="black")
        self.ir.grid(row=1,column=0,pady=10)
        self.ir.bind("<Return>",self.item_b)
        self.ir.bind("<Up>",lambda event: self.cr.focus())
        self.ir.bind("<Down>",lambda event: self.i_s.focus())
        self.i_s=Button(self.label_frame,text="Invoice Summary",command=self.summary,font="consolas 20 bold",bg="white",fg="black")
        self.i_s.grid(row=2,column=0,pady=10)
        self.i_s.bind("<Return>",self.summary_b)
        self.i_s.bind("<Up>",lambda event: self.ir.focus())
        self.i_s.bind("<Down>",lambda event: self.ts.focus())
        self.ts=Button(self.label_frame,text="Tax Statement",command=self.tax,font="consolas 20 bold",bg="white",fg="black")
        self.ts.grid(row=3,column=0,pady=10)
        self.ts.bind("<Return>",self.tax_b)
        self.ts.bind("<Up>",lambda event: self.i_s.focus())
        self.ts.bind("<Down>",lambda event: self.back.focus())
        self.back=Button(self.label_frame,text="Back(Esc)",command=self.report_window.destroy,font="consolas 20 bold",bg="white",fg="black")
        self.back.grid(row=6,column=0,pady=10)
        self.back.bind("<Return>",self.exit)
        self.back.bind("<Up>",lambda event: self.ts.focus())
        self.back.bind("<Down>",lambda event: self.cr.focus())
        self.report_window.focus_force()
        self.report_window.bind("<Escape>",self.exit)
        self.report_window.focus_force()
        self.report_window.overrideredirect(True)
    def register(self):
        Day_Register('light blue','blue')
    def register_bind(self,event):
        self.register()
    def item_report(self):
        Item_Report()
    def item_b(self,event):
        self.item_report()
    def tax(self):
        Tax_Statement()
    def tax_b(self,event):
        self.tax()
    def summary(self):
        Invoice_summary('light blue','blue')
    def summary_b(self,event):
        self.summary()
    def exit(self,event):
        self.report_window.destroy()
class Item_Report:
    def __init__(self):
        self.ir_day=Toplevel()
        self.ir_day.geometry("700x900+0+0")
        self.ir_day.config(bg="light blue")
        self.lbl=Label(self.ir_day,text="Items Stock Register",width=29,font="Times 30 bold",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.in_frame=LabelFrame(self.ir_day,bd=0,bg="light blue")
        self.in_frame.grid(row=1,column=0,padx=10,pady=30)
        self.lbldf=Label(self.in_frame,text="Date from",font="consolas 15",fg="white",bg="blue",width=13)
        self.lbldf.grid(row=1,column=2,pady=10)
        self.lbl_dfe=Entry(self.in_frame,width=10,font="consolas 15",bg="light blue",fg="black",bd=0)
        self.lbl_dfe.grid(row=1,column=3,pady=10,padx=5)
        self.lbl_dfe.insert(END,"01/02/20")
        self.lbl_dfe.focus()
        self.lbl_dfe.bind("<Return>",self.open_)
        self.lbldt=Label(self.in_frame,text=" To Date",font="consolas 15",fg="white",bg="blue",width=13)
        self.lbldt.grid(row=1,column=4,pady=10,padx=25)
        self.lbl_dte=Entry(self.in_frame,width=10,font="consolas 15",bg="light blue",fg="black",bd=0)
        self.lbl_dte.grid(row=1,column=5,pady=10,padx=10)
        self.lbl_dte.insert(END,f"{date.today().strftime('%d/%m/%y')}")
        self.lbl_dte.configure(state="readonly")
        self.pr=Button(self.in_frame,width=10,text="Print",font="consolas 14",bg="blue",fg="white",command=self.open)
        self.pr.grid(row=2,column=3,pady=20)
        self.bck=Button(self.in_frame,width=10,text="Back",font="consolas 14",bg="blue",fg="white",command=self.ir_day.destroy)
        self.bck.grid(row=2,column=4,pady=20)
        self.ir_day.bind("<Escape>",self.exit)
        self.ir_day.focus_force()
        self.ir_day.overrideredirect(True)
    def open(self):
        if messagebox.askyesno(parent=self.ir_day,title="print PDF",message="Items Sale Register"):
            Reports.item_register(self.lbl_dfe.get(),self.ir_day)
            time.sleep(2)
            self.ir_day.destroy()
    def open_(self,event):
        self.open()
    def exit(self,event):
        self.ir_day.destroy()
class Tax_Statement:
    def __init__(self):
        self.tx_day=Toplevel()
        self.tx_day.geometry("700x900+0+0")
        self.tx_day.config(bg="light blue")
        self.lbl=Label(self.tx_day,text="Tax Register",width=29,font="Times 30 bold",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.in_frame=LabelFrame(self.tx_day,bd=0,bg="light blue")
        self.in_frame.grid(row=1,column=0,padx=10,pady=30)
        self.lbldf=Label(self.in_frame,text="Date from",font="consolas 15",fg="white",bg="blue",width=13)
        self.lbldf.grid(row=1,column=2,pady=10)
        self.lbl_dfe=Entry(self.in_frame,width=10,font="consolas 15",bg="light blue",fg="black",bd=0)
        self.lbl_dfe.grid(row=1,column=3,pady=10,padx=5)
        self.lbl_dfe.insert(END,"01/02/20")
        self.lbl_dfe.focus()
        self.lbl_dfe.bind("<Return>",self.open_)
        self.lbldt=Label(self.in_frame,text=" To Date",font="consolas 15",fg="white",bg="blue",width=13)
        self.lbldt.grid(row=1,column=4,pady=10,padx=25)
        self.lbl_dte=Entry(self.in_frame,width=10,font="consolas 15",bg="light blue",fg="black",bd=0)
        self.lbl_dte.grid(row=1,column=5,pady=10,padx=10)
        self.lbl_dte.insert(END,f"{date.today().strftime('%d/%m/%y')}")
        self.lbl_dte.configure(state="readonly")
        self.pr=Button(self.in_frame,width=10,text="Print",font="consolas 14",bg="blue",fg="white",command=self.open)
        self.pr.grid(row=2,column=3,pady=20)
        self.bck=Button(self.in_frame,width=10,text="Back",font="consolas 14",bg="blue",fg="white",command=self.tx_day.destroy)
        self.bck.grid(row=2,column=4,pady=20)
        self.tx_day.bind("<Escape>",self.exit)
        self.tx_day.focus_force()
        self.tx_day.overrideredirect(True)
    def open(self):
        if messagebox.askyesno(parent=self.tx_day,title="print PDF",message="GST Sale Register"):
            Reports.gst_register(self.lbl_dfe.get(),self.tx_day)
            time.sleep(2)
            self.tx_day.destroy()
    def open_(self,event):
        self.open()
    def exit(self,event):
        self.tx_day.destroy()
#**************************************Account*******************************************
class Account:
    def __init__(self):
        self.acc_window=Toplevel()
        self.acc_window.geometry("700x900+0+0")
        self.acc_window.config(bg="light blue")
        self.lbl=Label(self.acc_window,text="Account Menu",width=29,font="Times 30 bold",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.label_frame=LabelFrame(self.acc_window,foreground="white",background="light blue",bd=5)
        self.label_frame.grid(row=1,column=0,padx=30,pady=20)
        self.ad=Button(self.label_frame,text="ADD",font="consolas 20 bold",command=self.add_ac,bg="white",fg="black")
        self.ad.grid(row=0,column=0,pady=10,padx=10)
        self.ad.focus()
        self.ad.bind("<Return>",self.add_ac_b)
        self.ad.bind("<Up>",lambda event: self.back.focus())
        self.ad.bind("<Down>",lambda event: self.upd.focus())
        self.upd=Button(self.label_frame,text="Update/Delete",command=self.update_d,font="consolas 20 bold",bg="white",fg="black")
        self.upd.grid(row=1,column=0,pady=10)
        self.upd.bind("<Return>",self.update_d_b)
        self.upd.bind("<Up>",lambda event: self.ad.focus())
        self.upd.bind("<Down>",lambda event: self.d_r.focus())
        self.d_r=Button(self.label_frame,text="Day-Register",command=self.ac_day,font="consolas 20 bold",bg="white",fg="black")
        self.d_r.grid(row=3,column=0,pady=10)
        self.d_r.bind("<Return>",self.ac_day_b)
        self.d_r.bind("<Up>",lambda event: self.upd.focus())
        self.d_r.bind("<Down>",lambda event: self.party_ac.focus())
        self.party_ac=Button(self.label_frame,text="View-Vouchers",command=self.view,font="consolas 20 bold",bg="white",fg="black")
        self.party_ac.grid(row=4,column=0,pady=10)
        self.party_ac.bind("<Return>",self.view_b)
        self.party_ac.bind("<Up>",lambda event: self.d_r.focus())
        self.party_ac.bind("<Down>",lambda event: self.party_summ.focus())
        self.party_summ=Button(self.label_frame,text="Party-Summary",command=self.party_r,font="consolas 20 bold",bg="white",fg="black")
        self.party_summ.grid(row=5,column=0,pady=10,padx=15)
        self.party_summ.bind("<Return>",self.party_r_b)
        self.party_summ.bind("<Up>",lambda event: self.party_ac.focus())
        self.party_summ.bind("<Down>",lambda event: self.back.focus())
        self.back=Button(self.label_frame,text="Back(Esc)",command=self.acc_window.destroy,font="consolas 20 bold",bg="white",fg="black")
        self.back.grid(row=6,column=0,pady=10)
        self.back.bind("<Return>",self.exit)
        self.back.bind("<Up>",lambda event: self.party_summ.focus())
        self.back.bind("<Down>",lambda event: self.ad.focus())
        self.acc_window.focus_force()
        self.acc_window.bind("<Escape>",self.exit)
        self.acc_window.overrideredirect(True)
    def exit(self,event):
        self.acc_window.destroy()
    def view(self):
        fileexist=os.path.isfile("vouchers_data.csv")
        if not fileexist:
            messagebox.showerror(parent=self.acc_window,title="Error",message="Vouchers File Not Found")
            self.acc_window.destroy()
        else:
            webbrowser.open_new("vouchers_data.csv")
    def view_b(self,event):
        self.view()
    def party_r(self):
        if messagebox.askyesno(parent=self.acc_window,title="Print PDF",message="Print Party Summary Pdf"):
            Reports.party_register_all(self.acc_window)
            time.sleep(2)
            self.acc_window.destroy()
    def party_r_b(self,event):
        self.party_r()
    def add_ac(self):
        Add_account()
    def add_ac_b(self,event):
        self.add_ac()
    def update_d(self):
        Update_delete()
    def update_d_b(self,event):
        self.update_d()
    def ac_day(self):
        Acc_day_Register()
    def ac_day_b(self,event):
        self.ac_day()

class Add_account:
    def __init__(self):
        self.add_ac_window=Toplevel()
        self.add_ac_window.geometry("700x900+0+0")
        self.add_ac_window.config(bg="light blue")
        self.lab=Label(self.add_ac_window,text="Add Voucher",bg="blue",fg="white",width=29,font="Times 30 bold",bd=10)
        self.lab.grid(row=0,column=0,pady=10)
        self.lf=LabelFrame(self.add_ac_window,bg="light blue",bd=0)
        self.lf.grid(row=1,column=0,pady=10)
        self.lab_vn=Label(self.lf,bg="blue",text="Voucher No",width=14,fg="white",font="consolas 15")
        self.lab_vn.grid(row=1,column=1,pady=10)
        self.lab_vn_e=Entry(self.lf,font="consolas 15",bg="light blue",fg="black",bd=0)
        self.lab_vn_e.grid(row=1,column=2,pady=10,padx=5)
        file_exists=os.path.isfile("vouchers_data.csv")
        if not file_exists:
            self.voucher_no=1
            self.voucher_no=str(self.voucher_no).zfill(4)
        else:
            with open("vouchers_data.csv","r") as iv:
                data=csv.reader(iv)
                vc_no=list(data)
                self.voucher_no=int(vc_no[len(vc_no)-1][2])+1
                self.voucher_no=str(self.voucher_no).zfill(4)
        self.lab_vn_e.insert(END,self.voucher_no)
        self.lab_vn_e.configure(state="readonly")
        self.date=Label(self.lf,text="Date",bg="blue",width=14,fg="white",font="consolas 15",bd=0)
        self.date.grid(row=2,column=1,padx=10,pady=10)
        self.lab_dt_e=Entry(self.lf,font="consolas 15",bg="light blue",fg="black",bd=0)
        self.lab_dt_e.grid(row=2,column=2,pady=10,padx=10)
        self.lab_dt_e.insert(END,str(date.today().strftime("%d/%m/%y")))
        self.lab_dt_e.bind("<Return>",self.date_b)
        self.lb_c=Label(self.lf,bg="blue",text="Voucher Type",width=14,fg="white",font="consolas 15")
        self.lb_c.grid(row=3,column=1,padx=10,pady=10)
        self.vt_combobox=ttk.Combobox(self.lf,width=15,font="consolas 15",state="readonly" )
        self.vt_combobox["values"]=('Cash','Reciept','Credit Note')
        self.vt_combobox.grid(row=3,column=2) 
        self.vt_combobox.current(0)
        self.vt_combobox.focus()
        self.vt_combobox.bind("<Return>",self.vt_combobox_b)
        self.lf2=LabelFrame(self.add_ac_window,bg="light blue",bd=0)
        self.lf2.grid(row=2,column=0,pady=10)
        self.party=Label(self.lf,text="Party Name",width=14,bg="blue",fg="white",font="consolas 15",bd=0)
        self.party.grid(row=4,column=1,pady=10)
        self.party_e=Entry(self.lf,font="consolas 15 bold",bg="light blue",fg="black",bd=0)
        self.party_e.grid(row=4,column=2,pady=10)
        self.party_e.bind("<Return>",self.party_b)
        self.lf3=LabelFrame(self.lf2,bg="light blue",bd=2,width=450,height=270)
        self.lf3.grid(row=1,column=0,padx=20,pady=5)
        self.pal=Label(self.lf3,text=" Particulars",width=20,bg="blue",fg="white",font="consolas 15",bd=0)
        self.pal.grid(row=0,column=0)
        self.aml=Label(self.lf3,text="Amount",width=20,bg="blue",fg="white",font="consolas 15",bd=0)
        self.aml.grid(row=0,column=1)
        self.csh=Label(self.lf3,text="Cash/D.D",bg="blue",width=14,fg="white",font="consolas 15 bold",bd=5)
        self.csh.grid(row=1,column=0,pady=20)
        self.am_e=Entry(self.lf3,font="consolas 15 bold",width=15,bg="light blue",fg="black",bd=0)
        self.am_e.grid(row=1,column=1,pady=10)
        self.reg=self.am_e.register(correct)
        self.am_e.config(validate="key",validatecommand=(self.reg,"%P"))
        self.am_e.bind("<Return>",self.save_b)
        self.csh=Label(self.lf3,text="Narration",bg="blue",width=14,fg="white",font="consolas 15 bold",bd=5)
        self.csh.grid(row=2,column=0,pady=20)
        self.csh_e=Entry(self.lf3,font="consolas 14 bold",width=19,bg="light blue",fg="black",bd=0)
        self.csh_e.grid(row=2,column=1,pady=10)
        self.csh_e.insert(END,f"Based on Voch/Type")
        self.csh_e.configure(state="readonly")
        self.fr0=LabelFrame(self.add_ac_window,bg="light blue",bd=0)
        self.fr0.grid(row=3,column=0,pady=10)
        self.save=Button(self.fr0,width=7,command=self.final_save,text="Save",font="consolas 15 bold",bg="blue",fg="white")
        self.save.grid(row=0,column=0)
        self.cancel=Button(self.fr0,width=7,command=self.add_ac_window.destroy,text="Cancel",font="consolas 15 bold",bg="blue",fg="white")
        self.cancel.grid(row=0,column=1,padx=30)
        self.add_ac_window.focus_force()
        self.add_ac_window.bind("<Escape>",self.exit)
        self.add_ac_window.overrideredirect(True)
    def date_b(self,event):
        self.vt_combobox.focus()
    def vt_combobox_b(self,event):
        self.party_e.focus()
    def party_b(self,event):
        if self.party_e.get()=="":
            Shortcuts_menu.cost_n(self.party_e,"costumers.csv","View All Customers Name            Esc->Exit",["Customer Name","Address","State","TIN/GST no","Transport","Phone","GST","Date"],7,0,self.add_ac_window,'lavender','steelblue')
        else:
            self.am_e.focus()
    def exit(self,event):
        self.add_ac_window.destroy()
    def save_b(self,event):
        self.final_save()
    def final_save(self):
        mbox=messagebox.askyesno(parent=self.add_ac_window,title="Save",message="Save Voucher")
        if mbox is True:
            file_exists_acc=os.path.isfile("vouchers_data.csv")
            with open("vouchers_data.csv","a",newline="") as f__acc:
                csv_writer_ac=DictWriter(f__acc,fieldnames=["party_name","Date","Particulars","Voucher_type","Debit","Credit","Balance"])
                if not file_exists_acc:
                    csv_writer_ac.writeheader()
                csv_writer_ac.writerow({
                  "party_name":str(self.party_e.get().upper()),
                  "Date":str(date.today().strftime('%d/%m/%y')),
                  "Particulars":str(self.voucher_no).zfill(4),
                  "Voucher_type":self.vt_combobox.get(),
                  "Debit":"",
                  "Credit":float(self.am_e.get()),
                  "Balance":"",
                })
            messagebox.showinfo(parent=self.add_ac_window,title="Successful",message="Voucher Saved successfully")
            Reports.print_voucher(self.lab_vn_e.get(),self.add_ac_window)
            time.sleep(2)
            self.add_ac_window.destroy()
class Update_delete:
    def __init__(self):
        self.update_ac=Toplevel()
        self.update_ac.geometry("700x900+0+0")
        self.update_ac.config(bg="light blue")
        self.lbl=Label(self.update_ac,text="Enter The Details of Account",width=29,font="Times 30 bold ",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=2,column=0,pady=20)
        self.lab_frame=LabelFrame(self.update_ac,foreground="white",background="light blue",bd=0)
        self.lab_frame.grid(row=3,column=0)
        self.name_label=Label(self.lab_frame,text="Voucher No:",bg="blue",fg="white",font="consolas 15 ",width=15)
        self.name_label.grid(row=0,column=1,padx=10,pady=10,sticky=t.W)
        self.name_entry=Entry(self.lab_frame,width=15,font="consolas 15",bd=0)
        self.name_entry.grid(row=0,column=2,pady=10,padx=10)
        self.name_entry.focus()
        self.name_entry.bind("<Return>",self.go)
        self.del_button=t.Button(self.lab_frame,width= 10,text="Delete",command=self.delete,background="blue",foreground="white",font="consolas 13",bd=3)
        self.del_button.grid(row=4,column=1,padx=40,pady=10)
        self.back_button=t.Button(self.lab_frame,width= 10,text="Back",command=self.update_ac.destroy,background="blue",foreground="white",font="consolas 13",bd=3)
        self.back_button.grid(row=4,column=2,padx=40,pady=10)
        self.update_ac.bind("<Escape>",self.exit_b)
        self.update_ac.overrideredirect(True)
        self.update_ac.focus_force()
    def go(self,event):
        if self.name_entry.get()=="":
            Shortcuts_menu.voucher_sc(self.name_entry,self.update_ac)
        else:
            self.delete()
    def exit_b(self,event):
        self.update_ac.destroy()
    def delete(self):
        if messagebox.askyesno(parent=self.update_ac,title="Delete voucher",message="Are You Sure!!!"):
            voucher_number=self.name_entry.get()
            flag=False
            if voucher_number=="":
                messagebox.showerror(parent=self.update_ac,title="Error",message="Not Found")
                self.name_entry.focus()
            else:
                fileexist_v=os.path.isfile("vouchers_data.csv")
                if not fileexist_v:
                    messagebox.showerror(parent=self.update_ac,title="Error",message="Vouchers File Not Found")
                    self.update_ac.destroy()
                else:
                    with open("vouchers_data.csv","r") as f:
                        csv_reader=csv.reader(f)
                        full_data=[]
                        data=[]
                        for line in csv_reader:
                            full_data.append(line)
                            if voucher_number in line:
                                data.append(line)
                                full_data.remove(line)
                                flag=True
                        with open("vouchers_data.csv","w",newline="") as f1:
                            wo=csv.writer(f1)
                            for line in full_data:
                                wo.writerow(line)
                        if flag==False:
                            messagebox.showerror(parent=self.update_ac,title="Error",message=" voucher Not Found")
                            self.update_ac.destroy()
                        else:
                            messagebox.showinfo(parent=self.update_ac,title="successfull",message=" voucher Delete Successfully")
                            self.update_ac.destroy()
class Acc_day_Register:
    def __init__(self):
        self.acc_day=Toplevel()
        self.acc_day.geometry("700x900+0+0")
        self.acc_day.config(bg="light blue")
        self.lbl=Label(self.acc_day,text="Accounts-Day-Register",font="Times 30 bold",fg="white",bg="steel blue",width=29,bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.in_frame=LabelFrame(self.acc_day,bd=0,bg="light blue")
        self.in_frame.grid(row=1,column=0)
        self.lbldf=Label(self.in_frame,text="Date from",font="consolas 15",fg="white",bg="blue",width=13)
        self.lbldf.grid(row=1,column=2,pady=10)
        self.lbl_dfe=Entry(self.in_frame,width=10,font="consolas 15",bg="light blue",fg="black",bd=0)
        self.lbl_dfe.grid(row=1,column=3,pady=10,padx=5)
        self.lbl_dfe.insert(END,"01/01/20")
        self.lbl_dfe.focus()
        self.lbl_dfe.bind("<Return>",self.bind_d)
        self.lbldt=Label(self.in_frame,text=" To Date",font="consolas 15",fg="white",bg="blue",width=13)
        self.lbldt.grid(row=1,column=4,pady=10,padx=25)
        self.lbl_dte=Entry(self.in_frame,width=10,font="consolas 15",bg="light blue",fg="black",bd=0)
        self.lbl_dte.grid(row=1,column=5,pady=10,padx=10)
        self.lbl_dte.insert(END,f"{date.today().strftime('%d/%m/%y')}")
        self.lbl_dte.configure(state="readonly")
        self.sale_lbl=Label(self.in_frame,text="Party Name",font="consolas 15",fg="white",bg="blue",width=13)
        self.sale_lbl.grid(row=4,column=3,pady=30,padx=10)
        self.name_e=Entry(self.in_frame,width=15,font="consolas 15 bold",bg="white",fg="black",bd=0)
        self.name_e.grid(row=4,column=4)
        self.pr=Button(self.in_frame,width=10,text="Print",font="consolas 14",bg="blue",fg="white",command=self.pri)
        self.pr.grid(row=5,column=3)
        self.bck=Button(self.in_frame,width=10,text="Back",font="consolas 14",bg="blue",fg="white",command=self.acc_day.destroy)
        self.bck.grid(row=5,column=4)
        self.name_e.bind("<Return>",self.name_b)
        self.acc_day.focus_force()
        self.acc_day.bind("<Escape>",self.exit)
        self.acc_day.overrideredirect(True)
    def bind_d(self,event):
        self.name_e.focus()
    def exit(self,event):
        self.acc_day.destroy()
    def pri(self):
        if self.name_e.get()=="":
            messagebox.showerror(parent=self.acc_day,title="Error",message="Entry Box is Empty")
            self.name_e.focus()
        else:
            file_exists_11=os.path.isfile("vouchers_data.csv")
            if not file_exists_11:
                messagebox.showerror(parent=self.acc_day,title="Error",message="Vouchers File Not Found")
                self.acc_day.destroy()
            else:
                with open ("vouchers_data.csv","r") as f:
                    csv_reader=csv.reader(f)
                    costumer_name=[line[0] for line in csv_reader]
                if self.name_e.get().upper()  not in costumer_name:
                    mbox=messagebox.askyesno(parent=self.acc_day,title="Voucher Not Found in Database",message="Please Save Voucher details!!")  
                    if mbox is True:
                        Add_account()
                        self.acc_day.destroy() 
                else:
                    Reports.party_register(self.name_e.get().upper(),self.lbl_dfe.get(),self.acc_day)
                    time.sleep(2)
                    self.acc_day.destroy()
    def name_b(self,event):
        if self.name_e.get()=="":
            Shortcuts_menu.cost_n(self.name_e,"costumers.csv","View All Custumors Name            Esc->Exit",["Customer Name","Address","State","TIN/GST no","Transport","Phone","GST","Date"],7,0,self.acc_day,'lightsteelblue','steelblue')
        else:
            self.pri()
#***********************************billing****************************
class Billing:
    def __init__(self):
        self.billing_window=Toplevel()
        self.billing_window.geometry("700x900+0+0")
        self.billing_window.config(bg="light blue")
        self.lbl=Label(self.billing_window,text="Billing Menu",width=29,font="Times 30 bold",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.label_frame=LabelFrame(self.billing_window,foreground="white",background="light blue",bd=5)
        self.label_frame.grid(row=1,column=0,padx=30,pady=20)
        self.cr=Button(self.label_frame,text="Invoice Bill",command=self.print,font="consolas 20 bold",bg="white",fg="black",)
        self.cr.grid(row=0,column=0,pady=10,padx=10)
        self.cr.focus()
        self.cr.bind("<Return>",self.print_b)
        self.cr.bind("<Up>",lambda event: self.back.focus())
        self.cr.bind("<Down>",lambda event: self.ir.focus())
        self.ir=Button(self.label_frame,text="Payment Voucher",command=self.voucher,font="consolas 20 bold",bg="white",fg="black")
        self.ir.grid(row=1,column=0,pady=10,padx=10)
        self.ir.bind("<Return>",self.voucher_b)
        self.ir.bind("<Up>",lambda event: self.cr.focus())
        self.ir.bind("<Down>",lambda event: self.back.focus())
        self.back=Button(self.label_frame,text="Back(Esc)",command=self.billing_window.destroy,font="consolas 20 bold",bg="white",fg="black")
        self.back.grid(row=2,column=0,pady=10)
        self.back.bind("<Return>",self.exit)
        self.back.bind("<Up>",lambda event: self.ir.focus())
        self.back.bind("<Down>",lambda event: self.cr.focus())
        self.billing_window.focus_force()
        self.billing_window.bind("<Escape>",self.exit)
        self.billing_window.focus_force()
        self.billing_window.overrideredirect(True)
    def exit(self,event):
        self.billing_window.destroy()
    def print(self):
        Invoice_Print('light blue','blue')
    def print_b(self,event):
        self.print()
    def voucher(self):
        Credit_Reciept('light blue','blue')
    def voucher_b(self,event):
        self.voucher()
class Credit_Reciept:
    def __init__(self,bgf,bgh):
        self.bgf=bgf
        self.bgh=bgh
        self.rc_pr=Toplevel()
        self.rc_pr.geometry("700x900")
        self.rc_pr.config(bg=self.bgf)
        self.lbl=Label(self.rc_pr,text="Print Payment Voucher",width=29,font="Times 30 bold",fg="white",bg=self.bgh,bd=10)
        self.lbl.grid(row=2,column=0,pady=20)
        self.in_frame=LabelFrame(self.rc_pr,bd=0,bg=self.bgf)
        self.in_frame.grid(row=3,column=0)
        self.in_ab=Label(self.in_frame,text=' Voucher No ',bg=self.bgh,fg="white",width=10,font="consolas 15")
        self.in_ab.grid(row=0,column=0,padx=10,pady=10,sticky=t.W)
        self.in_en=Entry(self.in_frame,width=15,font="consolas 15",bg="white",fg="black",bd=0)
        self.in_en.grid(row=0,column=1,pady=10)
        self.in_en.focus_force()
        self.in_en.bind("<Return>",self.ent_b)
        self.cur_b=Button(self.in_frame,text="Last Voucher",command=self.current_inv,width=13,bg=self.bgh,fg="white",font="consolas 14")
        self.cur_b.grid(row=3,column=0,pady=20)
        self.pr_b=Button(self.in_frame,text="Print",command=self.choice,width=10,bg=self.bgh,fg="white",font="consolas 14")
        self.pr_b.grid(row=3,column=1,padx=40,pady=20)
        self.bck_b=Button(self.in_frame,text="Back",command=self.rc_pr.destroy,width=10,bg=self.bgh,fg="white",font="consolas 14")
        self.bck_b.grid(row=3,column=2,padx=40,pady=20)
        self.rc_pr.bind("<Escape>",self.exit)
        self.rc_pr.focus_force()
        self.rc_pr.overrideredirect(True)
    def exit(self,event):
        self.rc_pr.destroy()
    def ent_b(self,event):
        if self.in_en.get() =="":
            Shortcuts_menu.voucher_sc(self.in_en,self.rc_pr)
        else:
            self.choice()
    def current_inv(self):
        if messagebox.askyesno(parent=self.rc_pr,title="Print Voucher",message="Are You Sure?"):
            fileexist=os.path.isfile("payment_sleep.pdf")
            if not fileexist:
                messagebox.showerror(parent=self.rc_pr,title="Error",message="You haven't made any Voucher Yet")
            else:
                webbrowser.open_new("payment_sleep.pdf")
    def choice(self):
        if self.in_en.get()=="":
            messagebox.showerror(parent=self.rc_pr,title="Error",message="Entry box is Empty")
        else:
            if messagebox.askyesno(parent=self.rc_pr,title="Print Voucher",message="Are You Sure?"):
                Reports.print_voucher(self.in_en.get(),self.rc_pr)
#*********************************Purchase**************************
class Purchase:
    def __init__(self):
        self.purc_window=Toplevel()
        self.purc_window.geometry("700x900+0+0")
        self.purc_window.config(bg="light blue")
        self.lbl=Label(self.purc_window,text="Party Purchase Stock ",width=29,font="Times 30 bold",fg="white",bg="blue",bd=10)
        self.lbl.grid(row=0,column=0,pady=10)
        self.label_frame=LabelFrame(self.purc_window,foreground="white",background="light blue",bd=5)
        self.label_frame.grid(row=1,column=0,padx=30,pady=20)
        self.cr=Button(self.label_frame,text="Particular Register",command=self.particular,font="consolas 20 bold",bg="white",fg="black",)
        self.cr.grid(row=0,column=0,pady=10,padx=10)
        self.cr.focus()
        self.cr.bind("<Return>",self.particular_b)
        self.cr.bind("<Up>",lambda event: self.back.focus())
        self.cr.bind("<Down>",lambda event: self.ir.focus())
        self.ir=Button(self.label_frame,text="Summary Register",command=self.all,font="consolas 20 bold",bg="white",fg="black")
        self.ir.grid(row=1,column=0,pady=10,padx=10)
        self.ir.bind("<Return>",self.all_b)
        self.ir.bind("<Up>",lambda event: self.cr.focus())
        self.ir.bind("<Down>",lambda event: self.back.focus())
        self.back=Button(self.label_frame,text="Back(Esc)",command=self.purc_window.destroy,font="consolas 20 bold",bg="white",fg="black")
        self.back.grid(row=2,column=0,pady=10)
        self.back.bind("<Return>",self.exit)
        self.back.bind("<Up>",lambda event: self.ir.focus())
        self.back.bind("<Down>",lambda event: self.cr.focus())
        self.purc_window.focus_force()
        self.purc_window.bind("<Escape>",self.exit)
        self.purc_window.focus_force()
        self.purc_window.overrideredirect(True)
    def exit(self,event):
        self.purc_window.destroy()
    def particular(self):
        Acc_day_Register()
    def particular_b(self,event):
        self.particular()
    def all(self):
        if messagebox.askyesno(parent=self.purc_window,title="Print Summary",message="Are You Sure?"):
            Reports.party_register_all(self.purc_window)
    def all_b(self,event):
        self.all()
#*******************************END********************************
if __name__ == "__main__":
        window=Tk()
        Main(window)
