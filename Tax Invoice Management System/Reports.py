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
#===============Invoice Bill Pdf==========================
def pdf_func(invoice_name,no):
    invoice_no=str(no)
    fi="current_invoice_pdf"
    pdfile=canvas.Canvas(f"{fi}.pdf",bottomup=0)
    with open("costumers.csv","r") as p1:
        part=csv.reader(p1)
        costumer_details=[line for line in part if invoice_name==line[0]]
    with open("invoice_data.csv","r") as p2:
        part=csv.reader(p2)
        party=[line for line in part if invoice_no==line[0]]
    cart_data=party[0][3]
    cart_data=cart_data.replace("[","")
    cart_data=cart_data.replace("]","")
    cart_data=cart_data.replace("'","")
    cart=cart_data.split(",")
    index=len(cart)
    def num_words(n):
        number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        nty=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninty"]
        tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        w=str(n)
        if "." in w:
            a=w.split(".")
            n=int(a[0])
        if n>9999999:
            return "Cant show for more than 7 digits"
        else:
            d=[0,0,0,0,0,0,0]
            i=0
            while n>0:
                d[i]=n%10
                i+=1
                n=n//10
            num=""
            if d[6]!=0:
                if d[6]==1:
                    num+=tens[d[5]] +" "+"Lakh"+" "
                else:
                    num+=nty[d[6]]+""+number[d[5]] +" "+"Lakh"+" "
            else:
                if d[5]!=0:
                    num+=number[d[5]] +""+"Lakh"+" "
            if d[4]!=0:
                if(d[4]==1):
                    num+=tens[d[3]]+ " Thousand "
                else:
                    num+=nty[d[4]]+number[d[3]]+  " Thousand "
            else:
                if d[3]!=0:
                    num+=number[d[3]]+ " Thousand "
            if d[2]!=0:
                num+=number[d[2]]+"Hundred"
            if d[1] != 0:
                if (d[1] == 1):
                    num += tens[d[0]]
                else:
                    num += nty[d[1]] + " " + number[d[0]]
            else:
                if d[0] != 0:
                    num += number[d[0]]
            return num
    def cart_filling(e):
        pdfile.setFont("Helvetica",10)    
        y,j,k,l,m=325,0,1,2,3
        for i in range(1,e):
            pdfile.drawString(25,y,str(i))         #sr no
            pdfile.drawString(45,y,cart[j])      #item name
            pdfile.drawString(206,y,"960810")        #hsn no
            pdfile.drawString(242,y,cart[k])     #quant
            pdfile.drawString(274,y,cart[l])     #mrp
            pdfile.drawString(318,y,cart[m])     #tax value
            y+=30
            j+=6
            k+=6
            l+=6
            m+=6
    if index==6:
        for d in range(24):
            cart.append(" ")
        cart_filling(2)
    elif index==12:
        for d in range(18):
            cart.append(" ")
        cart_filling(3)
    elif index==18:
        for d in range(12):
            cart.append(" ")
        cart_filling(4)
    elif index==24:
        for d in range(6):
            cart.append(" ")
        cart_filling(5)
    elif index==30:
        cart_filling(6)
    def local_cart(f):
        pdfile.setFont("Helvetica",9)
        y2,p=325,4 
        for i in range(f):
            pdfile.drawString(377,y2,"2.5%")                 #cgst rate
            pdfile.drawString(401,y2,cart[p])          #cgst amount
            pdfile.drawString(440,y2,"2.5%")                 #sgst rate
            pdfile.drawString(464,y2,cart[p])          #sgst amount
            y2+=30
            p+=6
    def inter_cart(f):
        pdfile.setFont("Helvetica",9)
        y2,p=325,5
        for i in range(f):
            pdfile.drawString(503,y2,"5%")
            pdfile.drawString(532,y2,cart[p])  
            y2+=30
            p+=6
    if costumer_details[0][6]=="LOCAL":        # tax Amount
        pdfile.drawString(320,708,party[0][6])
        pdfile.drawString(320,721,party[0][6])
        pdfile.drawString(465,680,party[0][6]) 
        pdfile.drawString(402,680,party[0][6])   
        if index==6:
            local_cart(1)
        elif index==12:
            local_cart(2)
        elif index==18:
            local_cart(3)
        elif index==24:
            local_cart(4)
        elif index==30:
            local_cart(5)
    if costumer_details[0][6]=="INTERSTATE":
        pdfile.drawString(320,734,party[0][9])   #sun total data
        pdfile.drawString(533,680,party[0][9])    #side gst box
        if index==6:
            inter_cart(1)
        elif index==12:
            inter_cart(2)
        elif index==18:
            inter_cart(3)
        elif index==24:
            inter_cart(4)
        elif index==30:
            inter_cart(5)
    pdfile.drawString(270,25,"Tax invoice")
    pdfile.setFont("Helvetica",8)
    pdfile.drawString(530,24,"Orignal")
    pdfile.drawString(530,45,"Duplicate")
    pdfile.setFont("Times-Bold",40)
    pdfile.drawString(11,67,"Caerulean Bytechains Pvt Ltd")
    pdfile.setFont("Courier-Oblique",11)
    pdfile.drawString(145,90,"Software,Hardware,Blockchain")
    f=[]
    Frame(20,100,198,40,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica-Bold",12)
    pdfile.drawString(10,115,"     GSTIN:36AAJCC7146D1ZP")
    pdfile.drawString(10,130,"     PAN:AAJCC7146D")
    Frame(218,100,235,40,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica",12)
    pdfile.drawString(200,115,"            Plot no 151A Phase 1 Saket Colony,")
    pdfile.drawString(205,130,"                   Hyderabad, Telangana 500062")
    Frame(453,100,120,40,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(425,115,"           Ph:9948129995")
    pdfile.drawString(429,130,"               9052029995")
    Frame(20,150,286,120,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(12,167,"   Party Name:")
    pdfile.setFont("Helvetica-Bold",14)
    pdfile.drawString(25,192,costumer_details[0][0])  #name of party
    pdfile.setFont("Helvetica-Bold",12)
    pdfile.drawString(25,225,f"State: {costumer_details[0][2]}")  #state
    pdfile.setFont("Helvetica",12)
    pdfile.drawString(25,210,costumer_details[0][1])  #adress
    pdfile.drawString(25,240,f"GST No: {costumer_details[0][3]}")
    pdfile.drawString(25,255,f"Contact: {costumer_details[0][5]}")
    Frame(306,150,267,24,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(296,169,"    Invoice No.")
    pdfile.setFont("Helvetica-Bold",11)
    pdfile.drawString(410,169,f"{party[0][0]}/2020-21")
    pdfile.setFont("Helvetica",11)
    Frame(306,174,267,24,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(296,193,"    Invoice Date.")
    pdfile.drawString(410,193,party[0][1])
    Frame(306,198,267,24,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(296,217,"    Transport.")
    pdfile.drawString(410,217,party[0][10])
    Frame(306,222,267,24,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(306,241," Order No/Dt.")
    pdfile.drawString(410,241,party[0][12])
    Frame(306,246,267,24,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(296,265,"    Way Bill.")
    pdfile.drawString(410,265,party[0][11])
    Frame(306,150,95,120,showBoundary=1).addFromList(f,pdfile)
    Frame(20,270,553,400,showBoundary=1).addFromList(f,pdfile)
    Frame(20,270,553,40,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica-Bold",12)
    pdfile.drawString(10,284,"    Sr")
    pdfile.drawString(10,296,"    No")
    Frame(40,270,165,400,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica-Bold",13)
    pdfile.drawString(28,284,"       Discription of Goods/")
    pdfile.drawString(28,296,"       Services")
    Frame(205,270,35,400,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica",10)
    pdfile.drawString(207,284,"HSN/") 
    pdfile.drawString(207,296,"SAC")
    Frame(240,270,30,400,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(242,284," Qty")
    Frame(270,270,45,400,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(274,284,"M R P")
    Frame(315,270,60,400,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(319,284,"Taxable")
    pdfile.drawString(319,296," Value")
    Frame(375,270,63,20,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(380,284," CGST")
    Frame(438,270,63,20,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(443,284," SGST")
    Frame(501,270,72,20,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(506,284," IGST")
    Frame(375,290,25,380,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica",9)
    pdfile.drawString(377,300,"Rate")
    Frame(400,290,38,380,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(402,300,"Amount")
    Frame(438,290,25,380,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(440,300,"Rate")
    Frame(463,290,38,380,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(465,300,"Amount")
    Frame(501,290,25,380,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(503,300,"Rate")
    pdfile.drawString(533,300,"Amount")
    Frame(20,670,170,67,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica-Bold",13)
    pdfile.drawString(35,685,"Bank Details:")
    pdfile.setFont("Helvetica-Bold",12)
    pdfile.drawString(35,702,"Bank:ICICI BANK")
    pdfile.drawString(35,718,"A/C-1234567890")
    pdfile.drawString(35,734,"IFSC-ICIC0001234")
    Frame(190,670,50,67,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica",10)
    Frame(315,670,60,67,showBoundary=1).addFromList(f,pdfile)
    pdfile.drawString(190,705,"Total pcs")
    pdfile.drawString(242,680,"Sub-Total")
    pdfile.drawString(242,693,"+Freight Chrg")
    pdfile.drawString(242,708,"ADD:CGST")
    pdfile.drawString(242,721,"ADD:SGST")
    pdfile.drawString(242,734,"ADD:IGST")
    pdfile.drawString(195,715,party[0][4])
    pdfile.drawString(320,680,party[0][5])
    pdfile.drawString(320,693,party[0][8]) 
    Frame(20,737,553,12,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica-Bold",12)
    pdfile.drawString(242,747,"Grand Total")
    pdfile.drawString(320,747,party[0][7])
    Frame(375,670,63,67,showBoundary=1).addFromList(f,pdfile)
    pdfile.setFont("Helvetica",10) 
    Frame(438,670,63,67,showBoundary=1).addFromList(f,pdfile)
    Frame(501,670,72,67,showBoundary=1).addFromList(f,pdfile)
    #t&c
    pdfile.setFont("Helvetica-BoldOblique",13)   #40,790   money in words
    pdfile.setFont("Helvetica-Bold",11)
    pdfile.drawString(23,763,num_words(party[0][7]))
    pdfile.drawString(40,780,"Terms & Conditions:")
    pdfile.setFont("Helvetica",7)
    pdfile.drawString(22,790,"1) Intrest @ 24% p.a will be charged if the bill is not paid within 15 Days.")
    pdfile.drawString(22,800,"2) Goods once Sold Cannot be taken back,Complain be made")
    pdfile.drawString(22,810,"    within 24 hours of delivery.")
    pdfile.drawString(22,820,"3) All Disputes are subjects to Hyderabad Jurisdictions.")
    pdfile.setFont("Helvetica",9)
    pdfile.drawString(300,759,"     Certified that the particulars given above are true & Correct")
    pdfile.drawString(300,775,"         For")
    pdfile.setFont("Helvetica-Bold",12)
    pdfile.drawString(330,775,"    Caerulean Bytechains Pvt Ltd")
    pdfile.setFont("Courier-BoldOblique",12)
    pdfile.drawString(370,820,"             (Authorised Sign)")
    pdfile.save()
    webbrowser.open_new("current_invoice_pdf.pdf")
#==================================================================
def sales_register(costumer_name,fromdate,window1):
    filexists_3=os.path.isfile("invoice_data.csv")
    if not filexists_3:
        messagebox.showerror(parent=window1,title="Error",message="Invoice File Not Found")
        window1.destroy()
    f=True
    costumer_invoices=[]
    day_reg=[]
    if costumer_name!="ALL_INV":
        with open("invoice_data.csv","r") as f1:
            data1=csv.reader(f1)
            for l in data1:
                if costumer_name==l[2]:
                    costumer_invoices.append(l)
    else:
        with open("invoice_data.csv","r") as f1:
            data1=csv.reader(f1)
            for l in data1:
                costumer_invoices.append(l)
            costumer_invoices.pop(0)
    if len(costumer_invoices)==0:
        f=False
        return f
    else:
        for d in costumer_invoices:
            if d[1].split("/")[1]>fromdate.split("/")[1]:
                day_reg.append(d)
            elif d[1].split("/")[1]==fromdate.split("/")[1]:
                if d[1].split("/")[0]>=fromdate.split("/")[0]:
                    day_reg.append(d)   
        all_cart=[]
        for a1 in range(len(day_reg)):
            cart_data=day_reg[a1][3]
            cart_data=cart_data.replace("[","")
            cart_data=cart_data.replace("]","")
            cart_data=cart_data.replace("'","")
            cart=cart_data.split(",")
            all_cart.append(cart)
        total_invoices=len(all_cart)
        day_pdf=canvas.Canvas("day_register.pdf",bottomup=0)
        day_pdf.setFont("Times-Bold",25)
        day_pdf.drawString(215,50,"Sales Register")
        day_pdf.line(215,55,360,55)
        fr=[]
        day_pdf.setFont("Helvetica-Bold",11)
        day_pdf.drawString(230,70,f"{fromdate} To {date.today().strftime('%d/%m/%y')}")
        day_pdf.setFont("Helvetica-Bold",8)
        day_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
        day_pdf.drawString(465,60,f"Page No {day_pdf.getPageNumber()}")
        #*******************Discription loop****************
        x1=[30,80,200,320,350,385,430,465]
        y1=[50,120,120,30,35,45,35,75]
        string=["Bill no","Party Name","Item Discription","Qty","Rate","Amount","Tax","GST/G.Total"]
        i,j,k=0,0,0
        for frame1 in range(8):
            Frame(x1[i],80,y1[j],20,showBoundary=1).addFromList(fr,day_pdf)
            day_pdf.drawString(x1[i]+3,95,string[k])
            i+=1
            j+=1
            k+=1
        #*******************frames /frt****************************
        z=100
        z2=115
        z3=135
        z5=135
        x5=[210,330,360,395,437]
        day_pdf.setFont("Helvetica-Bold",8)
        for ind in range(total_invoices):
            if z5>=756:
                day_pdf.showPage()
                day_pdf.setFont("Helvetica-Bold",8)
                day_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
                day_pdf.drawString(465,60,f"Page No {day_pdf.getPageNumber()}")
                z=100
                z2=115
                z3=135
                z5=135
                x5=[210,330,360,395,437]
            flag=0
            day_pdf.drawString(45,z3,day_reg[ind][0])   # Bill no
            day_pdf.drawString(90,z3,day_reg[ind][2])    # party name
            z3+=((len(all_cart[ind]))//6+3)*20
            day_pdf.drawString(33,z2,day_reg[ind][1])
            z2+=((len(all_cart[ind]))//6+2+1)*20
            for mf in range((len(all_cart[ind]))//6+2): #iteration 1   -->4
                i,j=0,0
                for frame2 in range(8):
                    Frame(x1[i],z,y1[j],20,showBoundary=1).addFromList(fr,day_pdf)
                    i+=1
                    j+=1
                z+=20
            z+=20
            if len(all_cart[ind])==30:
                for d2 in range(4,25,5):
                    all_cart[ind].pop(d2)
            elif len(all_cart[ind])==24:
                for d2 in range(4,24,5):
                    all_cart[ind].pop(d2)
            elif len(all_cart[ind])==18:
                for d2 in range(4,18,5):
                    all_cart[ind].pop(d2)
            elif len(all_cart[ind])==12:
                for d2 in range(4,12,5):
                    all_cart[ind].pop(d2)
            elif len(all_cart[ind])==6:
                all_cart[ind].pop(4)
            for  l in range((len(all_cart[ind]))//5):
                for n in range(len(x5)):
                    day_pdf.drawString(x5[n]-7,z5,all_cart[ind][flag])
                    day_pdf.setFillColorRGB(100,0,0)
                    day_pdf.drawString(508,z5,"5%")
                    day_pdf.setFillColorRGB(0,0,0)
                    flag+=1
                z5+=20
            day_pdf.setFillColorRGB(0,0,450)
            day_pdf.drawString(206,z5,f"Frieght Rate: {day_reg[ind][8]}")
            day_pdf.setFillColorRGB(0,0,0)
            day_pdf.drawString(325,z5,day_reg[ind][4])
            day_pdf.drawString(431,z5,day_reg[ind][9])
            day_pdf.drawString(390,z5,day_reg[ind][5])
            day_pdf.drawString(480,z5,day_reg[ind][7])
            day_pdf.setFillColorRGB(0,0,0)
            z5+=60     
        webbrowser.open_new("day_register.pdf")
        day_pdf.save()
        return f
#=========================Item Register Pdf==========================================
def item_register(fromdate,window_name):
    file_exists_1=os.path.isfile("items.csv")
    if not file_exists_1:
        messagebox.showerror(parent=window_name,title="Error",message="Items File Not Found")
        window_name.destroy()
    with open("items.csv","r") as f1:
        data=csv.reader(f1)
        items_name=[]
        for line in data:
            items_name.append(line[0])
    items_name.pop(0)            #available items in our system
    with open("items_data.csv","r") as it:
        data_=csv.reader(it)
        data1=list(data_)
        data1.pop(0)
        data=[]
    for d in data1:
            if d[1].split("/")[1]>fromdate.split("/")[1]:
                data.append(d)
            elif d[1].split("/")[1]==fromdate.split("/")[1]:
                if d[1].split("/")[0]>=fromdate.split("/")[0]:
                    data.append(d)
    items_data=[]
    for i in items_name:
        temp_cart_items=[ line for line in data if i ==line[0]]
        items_data.append(temp_cart_items)
    resulting_list=[ele for ele in items_data if ele !=[]]            #seperate list of available items
    item_pdf=canvas.Canvas("item_sale_register.pdf",bottomup=0)
    item_pdf.setFont("Times-Bold",25)
    item_pdf.drawString(195,60,"Item Sales Register")
    item_pdf.line(195,65,397,65)
    item_pdf.setFont("Times-Bold",13)
    item_pdf.drawString(220,80,f"{fromdate} To {date.today().strftime('%d/%m/%y')}")
    fr=[]
    item_pdf.setFont("Helvetica-Bold",11)
    item_pdf.setFont("Helvetica-Bold",9)
    item_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
    item_pdf.drawString(465,60,f"Page No {item_pdf.getPageNumber()}")
    #*******************Discription loop****************
    x1=[40,150,200,235,370,415,460]
    y1=[110,50,35,135,45,45,65]
    string=["Item Discription","Date","Bill no","Party Name","Qty","Rate","Amount"]
    i,j,k=0,0,0
    for frame1 in range(7):
        Frame(x1[i],90,y1[j],20,showBoundary=1).addFromList(fr,item_pdf)
        item_pdf.drawString(x1[i]+3,105,string[k])
        i+=1
        j+=1
        k+=1
    #************************************************************************

    z=120
    item_pdf.setFont("Helvetica-Bold",8)
    for av_items in resulting_list:
        total_q=0
        total_a=0
        item_pdf.setFillColorRGB(0,0,0)
        for mi in range(len(av_items)):
            if z>=720:
                item_pdf.showPage()
                item_pdf.setFont("Helvetica-Bold",8)
                item_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
                item_pdf.drawString(465,60,f"Page No {item_pdf.getPageNumber()}")
                z=80
            p=0
            for i in range(7):
                item_pdf.drawString(x1[p]+5,z,av_items[mi][i])
                item_pdf.line(x1[p],z-10,x1[p],z+6)
                p+=1
            item_pdf.line(40,z+5,525,z+5)
            total_q+=int(av_items[mi][4])
            total_a+=float(av_items[mi][6])
            z+=15
        item_pdf.setFillColorRGB(100,0,0)
        item_pdf.drawString(335,z+5,"Total")
        item_pdf.drawString(372,z+5,str(total_q))
        item_pdf.drawString(462,z+5,str(total_a))
        z+=25       
    item_pdf.save()
    webbrowser.open_new("item_sale_register.pdf")
#================================Gst Tax Register=======================================
def gst_register(fromdate,window_name):
    file_exists_1=os.path.isfile("invoice_data.csv")
    if not file_exists_1:
        messagebox.showerror(parent=window_name,title="Error",message="Invoice File Not Found")
        window_name.destroy()
    data=[]
    new_data=[]
    with open("invoice_data.csv","r") as f1:
            data1=csv.reader(f1)
            data=list(data1)
            data.pop(0)
    for d in data:
            if d[1].split("/")[1]>fromdate.split("/")[1]:
               new_data.append(d)
            elif d[1].split("/")[1]==fromdate.split("/")[1]:
                if d[1].split("/")[0]>=fromdate.split("/")[0]:
                    new_data.append(d)
    
    update_resulting_list=[]
    for i in new_data:
        resulting_list=[]
        resulting_list.append(i[0])
        resulting_list.append(i[1])
        resulting_list.append(i[2])
        resulting_list.append(i[4])
        resulting_list.append(i[5])
        resulting_list.append(i[9])
        resulting_list.append((float(i[5])+float(i[9])))
        update_resulting_list.append(resulting_list)
    item_pdf=canvas.Canvas("gst_register.pdf",bottomup=0)
    item_pdf.setFont("Times-Bold",25)
    item_pdf.drawString(195,60,"GST Register")
    item_pdf.line(195,65,340,65)
    fr=[]
    item_pdf.setFont("Helvetica-Bold",11)
    item_pdf.setFont("Helvetica-Bold",10)
    item_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
    item_pdf.drawString(465,60,f"Page No {item_pdf.getPageNumber()}")
    #*******************Discription loop****************
    x1=[40,80,130,250,300,350,410]
    y1=[40,50,120,50,50,60,90]
    string=["Bill no","Date","Party Name","Qty","Amount","Tax","Total"]
    i,j,k=0,0,0
    for frame1 in range(7):
        Frame(x1[i],80,y1[j],20,showBoundary=1).addFromList(fr,item_pdf)
        item_pdf.drawString(x1[i]+3,95,string[k])
        i+=1
        j+=1
        k+=1
    #************************************************************************
    z=110
    total_q=0
    total_a=0
    total_t=0
    grand_total=0
    item_pdf.setFont("Helvetica-Bold",8)
    for c in range(len(update_resulting_list)):
        if z>=750:
            item_pdf.showPage()
            item_pdf.setFont("Helvetica-Bold",8)
            item_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
            item_pdf.drawString(465,60,f"Page No {item_pdf.getPageNumber()}")
            z=100
        p=0
        total_q+=int(update_resulting_list[c][3])
        total_a+=float(update_resulting_list[c][4])
        total_t+=float(update_resulting_list[c][5])
        grand_total+=float(update_resulting_list[c][6])
        for i in range(7):
            item_pdf.drawString(x1[p]+5,z,str(update_resulting_list[c][p]))
            item_pdf.line(x1[p],z-10,x1[p],z+6)
            p+=1
            item_pdf.line(40,z+5,500,z+5)
        z+=15
    item_pdf.setFillColorRGB(100,0,0)
    item_pdf.drawString(220,z+5,"Total")
    item_pdf.drawString(255,z+5,str(total_q))
    item_pdf.drawString(302,z+5,str(total_a))
    item_pdf.drawString(352,z+5,str(total_t))
    item_pdf.drawString(414,z+5,str(grand_total))
    item_pdf.save()
    webbrowser.open_new("gst_register.pdf")
#============================All Costumers Register======================================
def party_register_all(window_name):
    party_name=[]
    file_exists_1=os.path.isfile("accounts_data.csv")
    if not file_exists_1:
        messagebox.showerror(parent=window_name,title="Error",message="Accounts File Not Found")
        window_name.destroy()
    with open("accounts_data.csv","r") as f1:
        csv_read=csv.reader(f1)
        accounts_data=list(csv_read)
        party_name=[i[0] for i in accounts_data]
        party_name.pop(0)
    final_party_names = list(dict.fromkeys(party_name))
    final_party_names.sort()
    update_resulting_list=[]
    for p in final_party_names:
        resulting_list=[]
        for line in accounts_data:
            if line[0]==p:
                resulting_list.append(line)
        update_resulting_list.append(resulting_list)
    for i in update_resulting_list:
        for line in i:
            temp_d=float(i[0][4])
            for j in range(1,len(i)):
                i[j][6]=str(float(i[j][4])+temp_d)
                temp_d=float(i[j][6])
    update_pdf_data=[]
    for i in update_resulting_list:
        pdf_data=[]
        pdf_data.append(i[len(i)-1][0])
        pdf_data.append(i[len(i)-1][6])
        update_pdf_data.append(pdf_data)
    fileexist=os.path.isfile("vouchers_data.csv")
    if  not fileexist:
        final_temp_list=[]
        for i in update_pdf_data:
            final_temp_list.append(i[0])
            final_temp_list.append(0)
    else:
        with open("vouchers_data.csv","r") as vd:
            csv_v=csv.reader(vd)
            vouchers_data_file=list(csv_v)
        vouchers_data_file.pop(0)
        final_temp_list=[]
        for l in update_pdf_data:
            final_temp_list.append(l[0])
            temp_a=0
            for i in vouchers_data_file:
                if l[0]==i[0]:
                    temp_a+=float(i[5])
            final_temp_list.append(temp_a)
    for i in update_pdf_data:
        for j in range(len(final_temp_list)-1):
            if final_temp_list[j] in i:
                i.append(final_temp_list[j+1])
    final_combine_list=[]
    for i in update_pdf_data:
        combine_data=[]
        combine_data.append(i[0])
        combine_data.append(i[1])
        combine_data.append(i[2])
        combine_data.append(float(i[1])-float(i[2]))
        final_combine_list.append(combine_data)
    #********************************************************************
    voucherall_pdf=canvas.Canvas("voucher_all.pdf",bottomup=0)
    voucherall_pdf.setFont("Times-Bold",25)
    voucherall_pdf.drawString(40,60,f"Accounting Summary")
    voucherall_pdf.setFont("Times-Bold",15)
    voucherall_pdf.drawString(200,78,f"Of All Parties")
    fr=[]
    voucherall_pdf.setFont("Helvetica-Bold",11)
    voucherall_pdf.setFont("Helvetica-Bold",10)
    voucherall_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
    voucherall_pdf.drawString(465,60,f"Page No {voucherall_pdf.getPageNumber()}")
    #*******************Discription loop****************
    x1=[40,240,330,420]
    y1=[200,90,90,80]
    string=["Party Name","Debit (Sale)","Credit(Vouchers)","Net Balance"]
    i,j,k=0,0,0
    for frame1 in range(4):
        Frame(x1[i],90,y1[j],20,showBoundary=1).addFromList(fr,voucherall_pdf)
        voucherall_pdf.drawString(x1[i]+5,105,string[k])
        i+=1
        j+=1
        k+=1
        #************************************************************************
    z=125
    for i in range(len(final_combine_list)):
        if z>=801:
            voucherall_pdf.showPage()
            voucherall_pdf.setFont("Helvetica-Bold",10)
            z=140
        p=0
        for v in range(4):
            voucherall_pdf.drawString(x1[p]+5,z,str(final_combine_list[i][p]))
            voucherall_pdf.line(x1[p],z-14,x1[p],z+6)
            p+=1
            voucherall_pdf.line(40,z+5,500,z+5)
        z+=20
    voucherall_pdf.save()
    webbrowser.open_new("voucher_all.pdf")
#=================Particular Costumer Register================================
def party_register(name,fromdate,window_name):
    data=[]
    new_data=[]
    voucher_data=[]
    newvoucher_data=[]
    file_exists_1=os.path.isfile("accounts_data.csv")
    if not file_exists_1:
        messagebox.showerror(parent=window_name,title="Error",message="Accounts File Not Found")
        window_name.destroy()
    file_exists_2=os.path.isfile("vouchers_data.csv")
    if not file_exists_2:
        messagebox.showerror(parent=window_name,title="Error",message="Vouchers File Not Found")
        window_name.destroy()
    with open("vouchers_data.csv","r") as f1:
            data1=csv.reader(f1)
            for i in data1:
                if name==i[0]:
                    voucher_data.append(i)
    for d in voucher_data:
        if d[1].split("/")[1]>fromdate.split("/")[1]:
            newvoucher_data.append(d)
        elif d[1].split("/")[1]==fromdate.split("/")[1]:
            if d[1].split("/")[0]>=fromdate.split("/")[0]:
                newvoucher_data.append(d)
    with open("accounts_data.csv","r") as f1:
            data1=csv.reader(f1)
            for i in data1:
                if name==i[0]:
                    data.append(i)
    if len(data)==0:
        new_data=[]
        temp_d=0
    else:
        for d in data:
            if d[1].split("/")[1]>fromdate.split("/")[1]:
                new_data.append(d)
            elif d[1].split("/")[1]==fromdate.split("/")[1]:
                if d[1].split("/")[0]>=fromdate.split("/")[0]:
                    new_data.append(d)
        new_data.sort(key=lambda x: x[1].split("/")[1] )
        temp_d=float(new_data[0][4])
        for i in range(1,len(new_data)):
            new_data[i][6]=str(float(new_data[i][4])+temp_d)
            temp_d=float(new_data[i][6])
    #********************************************************************
    voucher_pdf=canvas.Canvas("voucher_register.pdf",bottomup=0)
    voucher_pdf.setFont("Times-Bold",25)
    voucher_pdf.drawString(40,60,f"Ledger Account:")
    voucher_pdf.setFont("Times-Bold",14)
    voucher_pdf.drawString(225,58,name)
    fr=[]
    voucher_pdf.setFont("Helvetica-Bold",11)
    voucher_pdf.setFont("Helvetica-Bold",10)
    voucher_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
    voucher_pdf.drawString(465,60,f"Page No {voucher_pdf.getPageNumber()}")
    #*******************Discription loop****************
    x1=[40,90,150,225,315,405]
    y1=[50,60,75,90,90,100]
    string=["Date","Particulars","Voucher Type","Debit","Credit","Balance"]
    i,j,k=0,0,0
    for frame1 in range(6):
        Frame(x1[i],110,y1[j],20,showBoundary=1).addFromList(fr,voucher_pdf)
        voucher_pdf.drawString(x1[i]+3,125,string[k])
        i+=1
        j+=1
        k+=1
        #************************************************************************
    voucher_pdf.setFont("Helvetica-Bold",13)
    voucher_pdf.drawString(40,90,f"Sale:")
    voucher_pdf.drawString(85,90,f"{fromdate} To {date.today().strftime('%d/%m/%y')}")
    z=140
    voucher_pdf.setFont("Helvetica-Bold",10)
    for c in range(len(new_data)):
        p=0
        f=1
        for i in range(6):
            voucher_pdf.drawString(x1[p]+5,z,str(new_data[c][f]))
            voucher_pdf.line(x1[p],z-10,x1[p],z+6)
            p+=1
            f+=1
            voucher_pdf.line(40,z+5,500,z+5)
        z+=15
    z+=20
    voucher_pdf.setFont("Helvetica-Bold",13)
    voucher_pdf.drawString(40,z,f"Vouchers:")
    voucher_pdf.drawString(120,z,f"{fromdate} To {date.today().strftime('%d/%m/%y')}")
    voucher_pdf.setFont("Helvetica-Bold",10)
    z+=30
    voucher_pdf.line(40,z+5-20,500,z+5-20)
    temp_v=0
    for i in range(len(newvoucher_data)):
        if z>=801:
            voucher_pdf.showPage()
            voucher_pdf.setFont("Helvetica-Bold",10)
            z=140
        p=0
        f=1
        temp_v+=float(newvoucher_data[i][5])
        for v in range(6):
            voucher_pdf.drawString(x1[p]+5,z,str(newvoucher_data[i][f]))
            voucher_pdf.line(x1[p],z-14,x1[p],z+6)
            p+=1
            f+=1
            voucher_pdf.line(40,z+5,500,z+5)
        z+=15
    voucher_pdf.setFont("Helvetica-Bold",13)
    voucher_pdf.drawString(40,z+10,f"Available Balance:")
    voucher_pdf.drawString(170,z+10,f"{temp_d} - {temp_v} = {temp_d-temp_v}")
    voucher_pdf.save()
    webbrowser.open_new("voucher_register.pdf")
#===============================Invoice Summary pdf=======================================
def summary_pdf(fromdate,window_name):
    file_exists_1=os.path.isfile("invoice_data.csv")
    if not file_exists_1:
        messagebox.showerror(parent=window_name,title="Error",message="Invoice File Not Found")
        window_name.destroy()
    filter_list=[]
    with open("invoice_data.csv","r") as f:
        csv_data_=csv.reader(f)
        csv_data=list(csv_data_)
        csv_data.pop(0)
    for d in csv_data:
        if d[1].split("/")[1]>fromdate.split("/")[1]:
            filter_list.append(d)
        elif d[1].split("/")[1]==fromdate.split("/")[1]:
            if d[1].split("/")[0]>=fromdate.split("/")[0]:
                filter_list.append(d)
    dates=[]
    for  i in filter_list:
        dates.append(i[1])
    final_dates=list(dict.fromkeys(dates))
    resulting_list=[]
    for i in final_dates:
        temp=[]
        for j in filter_list:
            if i == j[1]:
                temp.append(j)
        resulting_list.append(temp)
    #********************************************************************************************
    inv_pdf=canvas.Canvas("invoice_summary.pdf",bottomup=0)
    inv_pdf.setFont("Times-Bold",25)
    inv_pdf.drawString(195,55,"Invoice Summary")
    inv_pdf.line(195,60,370,60)
    fr=[]
    inv_pdf.setFont("Helvetica-Bold",11)
    inv_pdf.drawString(230,75,f"{fromdate} To {date.today().strftime('%d/%m/%y')}")
    inv_pdf.setFont("Helvetica-Bold",10)
    inv_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
    inv_pdf.drawString(465,60,f"Page No {inv_pdf.getPageNumber()}")
    #*******************Discription loop****************
    x1=[40,90,130,250,300,350,410]
    y1=[50,40,120,50,50,60,90]
    string=["Date","Bill no","Party Name","Qty","Amount","Tax","Total"]
    i,j,k=0,0,0
    for frame1 in range(7):
        Frame(x1[i],90,y1[j],20,showBoundary=1).addFromList(fr,inv_pdf)
        inv_pdf.drawString(x1[i]+3,105,string[k])
        i+=1
        j+=1
        k+=1
    #************************************************************************
    z=125
    v=[0,2,4,5,9,7]

    for i in range(len(resulting_list)):
        if z>=801:
            inv_pdf.showPage()
            inv_pdf.setFont("Helvetica-Bold",10)
            inv_pdf.drawString(465,50,date.today().strftime('%d/%m/%y'))
            inv_pdf.drawString(465,60,f"Page No {inv_pdf.getPageNumber()}")
            z=130
        inv_pdf.line(40,z-15,500,z-15)
        inv_pdf.drawString(43,z,str(resulting_list[i][i][1]))
        for j in range(len(resulting_list[i])):
            p=0
            q=1
            for k in range(6):
                inv_pdf.drawString(x1[q]+5,z,str(resulting_list[i][j][v[k]]))
                inv_pdf.line(x1[p],z-15,x1[p],z+5)
                inv_pdf.line(410,z-15,410,z+5)
                p+=1
                q+=1
                inv_pdf.line(90,z+5,500,z+5)
            z+=20
        z+=15
    inv_pdf.save()
    webbrowser.open_new("invoice_summary.pdf")
#=================================Payment Reciept pdf======================================
def print_voucher(no,window_name):
    with open("vouchers_data.csv","r") as f:
        csv_data_=csv.reader(f)
        data=list(csv_data_)
    pdf_data=[]
    for i in data:
        if no==i[2]:
            pdf_data=i
    if len(pdf_data)==0:
        messagebox.showerror(parent=window_name,title="Error",message="Voucher Not Found")
        window_name.destroy()
    else:
        party_address=""
        with open("costumers.csv","r") as f2:
            csv_d_=csv.reader(f2)
            costumers_data=list(csv_d_)
        for i in costumers_data:
            if pdf_data[0]==i[0]:
                party_address=i[1]
    def num_words(n):
            number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
            nty=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninty"]
            tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
            w=str(n)
            if "." in w:
                a=w.split(".")
                n=int(a[0])
            if n>9999999:
                return "Cant show for more than 7 digits"
            else:
                d=[0,0,0,0,0,0,0]
                i=0
                while n>0:
                    d[i]=n%10
                    i+=1
                    n=n//10
                num=""
                if d[6]!=0:
                    if d[6]==1:
                        num+=tens[d[5]] +" "+"Lakh"+" "
                    else:
                        num+=nty[d[6]]+""+number[d[5]] +" "+"Lakh"+" "
                else:
                    if d[5]!=0:
                        num+=number[d[5]] +""+"Lakh"+" "
                if d[4]!=0:
                    if(d[4]==1):
                        num+=tens[d[3]]+ " Thousand "
                    else:
                        num+=nty[d[4]]+number[d[3]]+  " Thousand "
                else:
                    if d[3]!=0:
                        num+=number[d[3]]+ " Thousand "
                if d[2]!=0:
                    num+=number[d[2]]+"Hundred"
                if d[1] != 0:
                    if (d[1] == 1):
                        num += tens[d[0]]
                    else:
                        num += nty[d[1]] + " " + number[d[0]]
                else:
                    if d[0] != 0:
                        num += number[d[0]]
                return num
    amount_in_words=num_words(pdf_data[5])
    #**********************************************************************************
    sleep_pdf=canvas.Canvas("payment_sleep.pdf",bottomup=0)
    fr=[]
    Frame(55,100,480,200,showBoundary=1).addFromList(fr,sleep_pdf)
    sleep_pdf.setFont("Times-Bold",25)
    sleep_pdf.drawString(215,130,"Altaf Enterprises")
    Frame(155,140,300,25,showBoundary=1).addFromList(fr,sleep_pdf)
    sleep_pdf.setFont("Courier-Bold",12)
    sleep_pdf.drawString(158,153,"NEW F-130,Raghubir Nagar,New Delhi-110027")
    sleep_pdf.setFont("Helvetica-Bold",12)
    sleep_pdf.drawString(280,180,"Reciept")
    sleep_pdf.setFont("Helvetica-Bold",10)
    sleep_pdf.drawString(460,115,"Ph:9711335668")
    sleep_pdf.drawString(473,127,":8920046546")
    sleep_pdf.setFont("Times-Roman",12)
    sleep_pdf.drawString(70,200,"Voucher No:")
    sleep_pdf.drawString(70,220,"Party Name:")
    sleep_pdf.drawString(71,255,"Amount      :")
    sleep_pdf.drawString(71,280,"Narration    :")
    sleep_pdf.setFont("Times-Bold",12)
    sleep_pdf.drawString(150,200,pdf_data[2])
    sleep_pdf.drawString(150,220,pdf_data[0])
    sleep_pdf.setFont("Helvetica",10)
    sleep_pdf.drawString(445,200,f"Date: {pdf_data[1]}")
    sleep_pdf.setFont("Courier-Oblique",9)
    sleep_pdf.drawString(440,295,"(Authorised Sign)")
    sleep_pdf.drawString(150,235,party_address)
    sleep_pdf.setFont("Courier",10)
    sleep_pdf.drawString(150,266,f"(Rs {str(amount_in_words)})")
    sleep_pdf.setFont("Times-Bold",12)
    sleep_pdf.drawString(150,255,pdf_data[5])
    sleep_pdf.drawString(150,280,pdf_data[3])
    sleep_pdf.save()
    webbrowser.open_new("payment_sleep.pdf")
