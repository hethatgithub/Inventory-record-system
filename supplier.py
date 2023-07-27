from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Record System | Developed by Group 19")
        self.root.config(bg="white")
        self.root.focus_force()
        #==========================================
        #=====All Variables=====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_supp_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
      




        #====self.root===        
        #==options==
        label_search=Label(self.root,text="Invoice No.",bg="white",font=("goudy old style",15))
        label_search.place(x=700,y=80)

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=800,y=80,width=160)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#0f4d7d",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)

        #===title====
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)


        #===content===
        #===row1====
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=80)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_supp_invoice,font=("goudy old style",15),bg="lightblue").place(x=180,y=80,width=180)

        #=====row2====
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightblue").place(x=180,y=120,width=180)

        #===row3===
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightblue").place(x=180,y=160,width=180)

        #===row4===
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightblue")
        self.txt_desc.place(x=180,y=200,width=470,height=140)


        #===buttons===
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x= 180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="black",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)


        #===Employee Details===

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL,width=20)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL,width=20)

        self.SupplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice",text="Invoice No.")
        self.SupplierTable.heading("name",text="NAME")
        self.SupplierTable.heading("contact",text="CONTACT")
        self.SupplierTable.heading("desc",text="Description")
        self.SupplierTable["show"]="headings"
        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=90)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=90)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        #=============================================================================

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supp_invoice.get()=="":  
                  messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_supp_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                      messagebox.showerror("Error","Invoice No. already assigned, try different",parent=self.root)
                else:
                      cur.execute ("Insert into supplier(invoice,name,contact,desc)values(?,?,?,?)",(
                                                self.var_supp_invoice.get(),
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_desc.get('1.0',END),
                                              


                      ))
                      con.commit()
                      messagebox.showinfo("Success","Supplier added Successfully",parent=self.root) 
                      self.show()
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try: 
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                 self.SupplierTable.insert('',END,values=row)

        except Exception as ex:
             messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    


    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))       
        row=content['values']
       # print(row)
        self.var_supp_invoice.set(row[0])
        self.var_name.set(row[1]) 
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3]),
      
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supp_invoice.get()=="":  
                  messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_supp_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                      messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                      cur.execute ("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_desc.get('1.0',END),
                                                self.var_supp_invoice.get(),
                                              


                      ))
                      con.commit()
                      messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root) 
                      self.show()
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supp_invoice.get()=="":  
                  messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_supp_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                      messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do yo really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_supp_invoice.get(),))
                        con.cummit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_supp_invoice.set("")
        self.var_name.set("") 
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get=="":
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    

         
                   

if __name__=="__main__":
        root=Tk()
        obj=supplierClass(root)
        root.mainloop()