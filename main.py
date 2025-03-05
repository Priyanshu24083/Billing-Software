from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile




class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # =================Variables=================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()





        #Product Category List
        self.Category=["Select Option","Clothing","Lifestyle","Mobiles"]

        #SubCatClothing
        self.SubCatClothing=["Pant","Shirt","T-Shirt"]
        self.pant=["Levis","Peter England","Spykar"]
        self.price_levis=5000
        self.price_PeterEngland=7000
        self.price_Spykar=8000

        self.Shirt=["Peter England","Louis Phillipe","Canary London"]
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_Canary=3000

        self.T_shirt=["Polo","Roadster","Jack&Jones"]
        self.price_polo=1500
        self.price_Roadster=1800
        self.price_JackJones=1700

        #SubCatLifestyle
        self.SubCatLifestyle=['Bath Soap','Face Cream','Hair Oil']
        self.Bath_soap=['Pears','Lux','Santoor','Wild Stone']
        self.price_pears=float(20)
        self.price_lux=20
        self.price_Santoor=25
        self.price_WildStone=30

        self.Face_Cream=['Cetaphil','Ponds','Boro Plus','Niviea']
        self.price_Cetaphil=300
        self.price_Ponds=75
        self.price_Boro=125
        self.price_niviea=95

        self.Hair_oil=['Parachute','Mama Earth','Jasmine']
        self.price_para=50
        self.price_mamaearth=100
        self.price_Jasmine=75

        #SubCatMobile
        self.SubcatMobiles=['Iphone',"Realme","Samsung","One Plus"]
        self.Iphone=['Iphone 15','Iphone 14 Pro','Iphone 14','Iphone 13 Pro']
        self.price_15=150000
        self.price_14pro=140000
        self.price_14=130000
        self.price_13pro=120000


        self.Realme=['Realme 11','Realme 10','Realme 9','Realme 8']
        self.price_11a=30000
        self.price_10a=26000
        self.price_9a=22000
        self.price_8a=18000


        self.Samsung=['Samsung S23','Samsung S22','Samsung M21','Samsung FE']
        self.price_23s=120000
        self.price_22s=80000
        self.price_ms=24000
        self.price_fe=40000


        self.OnePlus=['One Plus 10R','One Plus 9R','One Plus 8R','One Plus Nord']
        self.price_10r=48000
        self.price_9r=38000
        self.price_8r=32000
        self.price_nord=22000







        #IMAGE 1
        img=Image.open("IMAGES/img1.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        #IMAGE 2
        img_1=Image.open("IMAGES/feature1.jpg")
        img_1=img_1.resize((515,130),Image.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=515,height=130)

        #IMAGE 3
        img_2=Image.open("IMAGES/img3.jpg")
        img_2=img_2.resize((515,130),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=515,height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #Customer Label Frame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial',10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Product Label Frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)

        #Category
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)
   

        #SubCategory
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="SubCategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,font=('arial',10,'bold'),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=('arial',10,'bold'),width=24,state="readonly")
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,font=('arial',10,'bold'),width=24,state="readonly",textvariable=self.prices)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        #IMAGE 1
        img12=Image.open("IMAGES/Screenshot (49).png")
        img12=img12.resize((490,340),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=490,height=340)

        #IMAGE 2
        img_13=Image.open("IMAGES/Screenshot (48).png")
        img_13=img_13.resize((490,340),Image.LANCZOS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lbl_img_13=Label(MiddleFrame,image=self.photoimg_13)
        lbl_img_13.place(x=490,y=0,width=500,height=340)


        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=10,width=500,height=40)


        self.lblBill=Label(Search_Frame,font=('arial',12,'bold'),bg="red",fg="white",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=26)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)


        self.BtnSearch=Button(Search_Frame,command=self.find_bill,height=1,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        #RightFrame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter Frame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.lblSubTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="SubTotal",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubtotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=('arial',10,'bold'),width=26)
        self.EntrySubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('arial',10,'bold'),width=26)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('arial',10,'bold'),width=26)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,height=2,command=self.clear,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()


        self.l=[]


    #Function
    def AddItem(self):
        self.n=self.prices.get()
        self.m=(self.qty.get())*(self.n)  
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name" )
        else:           
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))- (self.prices.get())))/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))- (self.prices.get()))))/100))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")

        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n==================================================")

            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")

            self.textarea.insert(END,"\n==================================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('Bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()}")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"Print")

    def find_bill(self):
        found="No"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'Bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="YES"

            if found=='NO':
                messagebox.showerror("Error","Invalid Bill No.")



    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()
        self.SubCategory.set("")

         



    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\tWelcome to Priyanshu's Mini Mall")
        self.textarea.insert(END,f"\n BILL Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")


        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQTY\tPrice")
        self.textarea.insert(END,"\n==================================================\n")





    def Categories(self,event=""):
            if self.Combo_Category.get()=="Clothing":
                self.ComboSubCategory.config(value=self.SubCatClothing)
                self.ComboSubCategory.current(0)

            if self.Combo_Category.get()=="Lifestyle":
                self.ComboSubCategory.config(value=self.SubCatLifestyle)
                self.ComboSubCategory.current(0)

            if self.Combo_Category.get()=="Mobiles":
                self.ComboSubCategory.config(value=self.SubcatMobiles)
                self.ComboSubCategory.current(0)



    def Product_add(self,event=""):
            if self.ComboSubCategory.get()=="Pant":
               self.ComboProduct.config(value=self.pant)
               self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Shirt":
               self.ComboProduct.config(value=self.Shirt)
               self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="T-Shirt":
               self.ComboProduct.config(value=self.T_shirt)
               self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Bath Soap":
               self.ComboProduct.config(value=self.Bath_soap)
               self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Face Cream":
               self.ComboProduct.config(value=self.Face_Cream)
               self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Hair Oil":
               self.ComboProduct.config(value=self.Hair_oil)
               self.ComboProduct.current(0)


            if self.ComboSubCategory.get()=="Iphone":
               self.ComboProduct.config(value=self.Iphone)
               self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Realme":
               self.ComboProduct.config(value=self.Realme)
               self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="Samsung":
               self.ComboProduct.config(value=self.Samsung)
               self.ComboProduct.current(0)

            if self.ComboSubCategory.get()=="One Plus":
               self.ComboProduct.config(value=self.OnePlus)
               self.ComboProduct.current(0)

    def price(self,event=""):
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_PeterEngland)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_Spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Canary London":
            self.ComboPrice.config(value=self.price_Canary)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pears":
            self.ComboPrice.config(value=self.price_pears)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_Santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Wild Stone":
            self.ComboPrice.config(value=self.price_WildStone)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Cetaphil":
            self.ComboPrice.config(value=self.price_Cetaphil)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_Ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Boro Plus":
            self.ComboPrice.config(value=self.price_Boro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Niviea":
            self.ComboPrice.config(value=self.price_niviea)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mama Earth":
            self.ComboPrice.config(value=self.price_mamaearth)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jasmine":
            self.ComboPrice.config(value=self.price_Jasmine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone 15":
            self.ComboPrice.config(value=self.price_15)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone 14 Pro":
            self.ComboPrice.config(value=self.price_14pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone 14":
            self.ComboPrice.config(value=self.price_14)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone 13 Pro":
            self.ComboPrice.config(value=self.price_13pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Realme 11":
            self.ComboPrice.config(value=self.price_11a)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Realme 10":
            self.ComboPrice.config(value=self.price_10a)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Realme 9":
            self.ComboPrice.config(value=self.price_9a)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Realme 8":
            self.ComboPrice.config(value=self.price_8a)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung S23":
            self.ComboPrice.config(value=self.price_23s)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung S22":
            self.ComboPrice.config(value=self.price_22s)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M21":
            self.ComboPrice.config(value=self.price_ms)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung FE":
            self.ComboPrice.config(value=self.price_fe)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="One Plus 10R":
            self.ComboPrice.config(value=self.price_10r)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="One Plus 9R":
            self.ComboPrice.config(value=self.price_9r)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="One Plus 8R":
            self.ComboPrice.config(value=self.price_8r)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="One Plus Nord":
            self.ComboPrice.config(value=self.price_nord)
            self.ComboPrice.current(0)
            self.qty.set(1)



if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()