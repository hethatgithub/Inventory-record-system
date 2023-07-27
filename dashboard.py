from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from catagory import catagoryClass
from  product import productClass
from supplier import supplierClass
from sales import salesClass
from billing import BillClass
import time

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1525x790+0+0")
        self.root.title("Inventory Record System | Developed by Group 19")
        self.root.config(bg="white")
        # ==title==
        self.icon_title = PhotoImage(file="IRS latest\IRS\images\images\logo1.png")
        title = Label(self.root, text="Inventory Record System", image=self.icon_title, compound=LEFT, font=(
            "times new roman", 40, "bold"), bg="dark blue", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        # ==button_logout==
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"),
                            bg="yellow", cursor="hand2").place(x=1350, y=10, height=50, width=150)

        # ==clock_label==
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Record System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman", 15), bg="grey", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ==Left Menu==
        self.MenuLogo = Image.open("IRS latest\IRS\images\images\menu_im.png")
        # directly resize image in program
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="grey")
        LeftMenu.place(x=0, y=102, width=200, height=665)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        self.icon_side = PhotoImage(file="IRS latest\IRS\images\images\side.png")
        lbl_menu = Label(LeftMenu, text="Menu", font=(
            "times new roman", 20), bg="#009688").pack(side=TOP, fill=X)

        btn_Employee = Button(LeftMenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_Supplier = Button(LeftMenu, text="Supplier",command=self.supplier, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_Category = Button(LeftMenu, text="Category",command=self.catagory, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_Product = Button(LeftMenu, text="Product",command=self.product, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_Sales = Button(LeftMenu, text="Sales",command=self.sales, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_Exit = Button(LeftMenu, text="Exit",command=root.destroy, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        # ==content==
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=(
            "gouldy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_Supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE, bg="red", fg="white", font=(
            "gouldy old style", 20, "bold"))
        self.lbl_Supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_Category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE, bg="lime", fg="white", font=(
            "gouldy old style", 20, "bold"))
        self.lbl_Category.place(x=1000, y=120, height=150, width=300)

        self.lbl_Products = Label(self.root, text="Total Products\n[ 0 ]", bd=5, relief=RIDGE, bg="green", fg="white", font=(
            "gouldy old style", 20, "bold"))
        self.lbl_Products.place(x=300, y=300, height=150, width=300)

        self.lbl_Sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="orange", fg="white", font=(
            "gouldy old style", 20, "bold"))
        self.lbl_Sales.place(x=650, y=300, height=150, width=300)

        self.update_date_time()
        # ==footer==
        lbl_footer = Label(self.root, text="IRS -Inventory Record System  |  Developed by group 13\n for any Technical Issue Contact above Reference",font=("times new roman", 12), bg="grey", fg="white").pack(side=BOTTOM, fill=X)

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
    
    def catagory(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = catagoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def bill(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = BillClass(self.new_win)
      

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Record System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
        

    

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()    # window stays and doesnt finish
