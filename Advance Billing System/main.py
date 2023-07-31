from tkinter import *
from tkinter import ttk
#from PIL import Image,ImageTk
from tkinter import PhotoImage
from tkinter import messagebox
import random

#------------------------FUNCTIONS----------------------------------------------
billnumber = random.randint(1000,10000)
constant = "OCK"
#------------------------CHECKBUTTON FUNCTIONS----------------------------------------------
def toggle_widget_swallow():
    if check_var_swallow.get():
        swallow_combobox.config(state=NORMAL)
        swallowQty_spinbox.config(state=NORMAL)
        swallowAmount.config(state=NORMAL)
        swallowRate_spinbox.config(state=NORMAL)

    else:
        swallow_combobox.config(state=DISABLED)
        swallowQty_spinbox.config(state=DISABLED)
        swallowAmount.config(state=DISABLED)
        swallowRate_spinbox.config(state=DISABLED)

def toggle_widget_soup():
    if check_var_soup.get():
        soup_combobox.config(state=NORMAL)
        soupQty_spinbox.config(state=NORMAL)
        soupAmount.config(state=NORMAL)
        soupRate_spinbox.config(state=NORMAL)
    else:
        soup_combobox.config(state=DISABLED)
        soupQty_spinbox.config(state=DISABLED)
        soupAmount.config(state=DISABLED)
        soupRate_spinbox.config(state=DISABLED)

def toggle_widget_protein():
    if check_var_protein.get():
        protein_combobox.config(state=NORMAL)
        proteinQty_spinbox.config(state=NORMAL)
        proteinAmount.config(state=NORMAL)
        proteinRate_spinbox.config(state=NORMAL)
    else:
        protein_combobox.config(state=DISABLED)
        proteinQty_spinbox.config(state=DISABLED)
        proteinAmount.config(state=DISABLED)
        proteinRate_spinbox.config(state=DISABLED)

def toggle_widget_drink():
    if check_var_drink.get():
        drink_combobox.config(state=NORMAL)
        drinkQty_spinbox.config(state=NORMAL)
        drinkAmount.config(state=NORMAL)
        drinkRate_spinbox.config(state=NORMAL)
    else:
        drink_combobox.config(state=DISABLED)
        drinkQty_spinbox.config(state=DISABLED)
        drinkAmount.config(state=DISABLED)
        drinkRate_spinbox.config(state=DISABLED)
       
       
#------------------------EXIT FUNCTION BUTTON----------------------------------------------

def exitProgram():
    if messagebox.askyesno("Billing System", "Do you want to Close or Exit the Billing System?"):
        root.destroy()
        
def clear():
    swallowAmount.delete(0,END)
    swallowQty_spinbox.delete(0,END)
    swallowRate_spinbox.delete(0,END)
    swallow_combobox.delete(0,END)
    
    soupAmount.delete(0,END)
    soupQty_spinbox.delete(0,END)
    soupRate_spinbox.delete(0,END)
    soup_combobox.delete(0,END)
    
    proteinAmount.delete(0,END)
    proteinQty_spinbox.delete(0,END)
    proteinRate_spinbox.delete(0,END)
    protein_combobox.delete(0,END)
    
    drinkAmount.delete(0,END)
    drinkQty_spinbox.delete(0,END)
    drinkRate_spinbox.delete(0,END)
    drink_combobox.delete(0,END)

    entryText.delete(1.0,END)
    
def order():
    nairaSign = "\u20A6" 
    koboSign = ".00"
    swallowQ = int(swallowQty_spinbox.get()) 
    swallowR = int(swallowRate_spinbox.get())

    swallow_amount = swallowQ * swallowR

    swallowAmount.delete(0,END)
    swallowAmount.insert(0,nairaSign)
    swallowAmount.insert(END, swallow_amount)
    swallowAmount.insert(END, koboSign)

    soupQ = int(soupQty_spinbox.get())
    soupR = int(soupRate_spinbox.get())
    soup_amount = soupQ * soupR
    soupAmount.delete(0,END)
    soupAmount.insert(0,nairaSign)
    soupAmount.insert(END,soup_amount)
    soupAmount.insert(END, koboSign)

    proteinQ = int(proteinQty_spinbox.get())
    proteinR = int(proteinRate_spinbox.get())
    protein_amount = proteinQ * proteinR
    proteinAmount.delete(0,END)
    proteinAmount.insert(0,nairaSign)
    proteinAmount.insert(END, protein_amount)
    proteinAmount.insert(END, koboSign)

    drinkQ = int(drinkQty_spinbox.get())
    drinkR = int(drinkRate_spinbox.get())
    drink_amount = (drinkQ * drinkR)
    drinkAmount.delete(0,END)
    drinkAmount.insert(0,nairaSign)
    drinkAmount.insert(END,drink_amount)
    drinkAmount.insert(END, koboSign)
    #-----------------------GET ALL ITEMS ----------------------------------
    #for swallow only
    itemSwallow = swallow_combobox.get()
    qtySwallow = swallowQty_spinbox.get()
    rateSwallow = swallowRate_spinbox.get()
    
     #for soup only
    itemSoup = soup_combobox.get()
    qtySoup = soupQty_spinbox.get()
    rateSoup = soupRate_spinbox.get()

     #for protein only
    itemProtein = protein_combobox.get()
    qtyProtein = proteinQty_spinbox.get()
    rateProtein = proteinRate_spinbox.get()

     #for drinks only
    itemDrink = drink_combobox.get()
    qtyDrink = drinkQty_spinbox.get()
    rateDrink = drinkRate_spinbox.get()

     #-----------------------TOTAL BILL PER RECEIPT ------------------------------------------
    subTotalBill = swallow_amount +   soup_amount +   protein_amount +   drink_amount
    serviceCharge = subTotalBill * 0.1
    vat = subTotalBill * 0.05
    totalBill = subTotalBill +  serviceCharge +    vat
    
     #-----------------------GET ALL ITEMS INTO THE RECEIPT ----------------------------------
    TotalBill = swallow_amount+soup_amount +protein_amount+ drink_amount
    entryText.delete(1.0,END)
    entryText.insert(END,"==================================================")
    entryText.insert(END,"--------------------RECEIPT-----------------------")
    entryText.insert(END,"==================================================")
    entryText.insert(END,"\t\t\t**Welcome Customer**\n\n\n")
    entryText.insert(END,"Customer's Details: \n")
    entryText.insert(END,f"Bill Number: {constant}{billnumber} \n\n")
    entryText.insert(END,"--------------------------------------------------\n")
    entryText.insert(END,"ITEMS\t\tQTY\tRATE\t\tAmount\n\n")
    entryText.insert(END,"--------------------------------------------------\n")
    entryText.insert(END,f"{itemSwallow}\t\t{qtySwallow}\t{rateSwallow}\t\t{nairaSign}{swallow_amount}{koboSign} \n\n")#swallow
    entryText.insert(END,f"{itemSoup}\t\t{qtySoup}\t{rateSoup}\t\t{nairaSign}{soup_amount}{koboSign} \n\n")#soup
    entryText.insert(END,f"{itemProtein}\t\t{qtyProtein}\t{rateProtein}\t\t{nairaSign}{protein_amount}{koboSign} \n\n")#protein
    entryText.insert(END,f"{itemDrink}\t\t{qtyDrink}\t{rateDrink}\t\t{nairaSign}{drink_amount}{koboSign} \n\n\n")#drink

    entryText.insert(END,"--------------------------------------------------\n")
    entryText.insert(END,f"\t\tSub-Total:{nairaSign}{subTotalBill}\n")#subtotal bill
    entryText.insert(END,f"\t\tService-Charge:{nairaSign}{serviceCharge}\n")#service charge
    entryText.insert(END,f"\t\tVAT:{nairaSign}{vat}\n")#VAT
    entryText.insert(END,"--------------------------------------------------\n")
    entryText.insert(END,f"\t\tTotal:{nairaSign}{totalBill}\n")#total bill
    
def receipt():
    print("Receipt")
    print (swallow_amount)
    
root = Tk()
root.title("RECEIPT SYSTEM")
root.resizable(0,0)
# Set the window icon for macOS or Linux
#try:
 #   icon_image = PhotoImage(file="learn.png")  # Replace "icon.png" with the correct path to your image
  #  root.iconphoto(True, icon_image)
#except:
 #   pass


#root.geometry("750x650+850+60")
#root.iconbitmap("icon.ico")
#------------------------Customer's Details--------------------------------------------
#customersDetailsFrame = LabelFrame(root,text = "Customers Details")

#lblFirstName =Label(root,text = "First Name: ")
#lblFirstName.grid(row = 0,column = 0)

#customersDetailsFrame.pack(side = TOP)
#------------------------Background Image--------------------------------------------
# Load the background image
background_image = PhotoImage(file="learn.png")

# Create a label to hold the background image and place it at the back
background_label = Label(root, image=background_image)
background_label.image = background_image  # Keep a reference to the image object
background_label.place(x=0, y=0, relwidth=1, relheight=1)

containerFrameReceipt = Frame(root)
containerFrameReceipt.pack()
#------------------------Receipt Display Text--------------------------------------------
entryText = Text(containerFrameReceipt,height = 30,width=50,relief = GROOVE,bd =10)
entryText.pack(pady=10,padx=10,side=RIGHT)


#------------------------HEADINGS--------------------------------------------
containerFrameItems = Frame(containerFrameReceipt)
containerFrameItems.pack(side=BOTTOM)

labelSN = Label(containerFrameItems,text = "S/N"
                ,relief = GROOVE,bd=10
                ,bg="red",fg="white"
                ,font="bold")
labelSN.grid(row = 0,column = 0)

labelItem = Label(containerFrameItems,text = "ITEMS"
                  ,relief = RIDGE,bd=10
                ,bg="red",fg="white"
                ,font="bold")
labelItem.grid(row = 0,column = 1)

labelQty = Label(containerFrameItems,text = "QTY."
                 ,relief = SUNKEN,bd=10
                ,bg="red",fg="white"
                ,font="bold")
labelQty.grid(row = 0,column = 2)

labelRate = Label(containerFrameItems,text = "RATE"
                  ,relief = FLAT,bd=10
                ,bg="red",fg="white"
                ,font="bold")
labelRate.grid(row = 0,column = 3)

labelAmount = Label(containerFrameItems,text = "AMOUNT"
                    ,relief = GROOVE,bd=10
                ,bg="red",fg="white"
                ,font="bold")
labelAmount.grid(row = 0,column = 4)


#------------------------SOLD ITEMS----------------------------------------------
#------------------------FOR SWALLOW----------------------------------------------
check_var_swallow = BooleanVar()
swallow_check = Checkbutton(containerFrameItems,text = "Swallow"
                            ,variable=check_var_swallow, command=toggle_widget_swallow)
swallow_check.grid(row =1 ,column =0)

swallow_combobox = ttk.Combobox(containerFrameItems,values =["Garri","Fufu","Amala","Pounded Yam","Wheat"],state=DISABLED)
swallow_combobox.grid(row = 1,column = 1)

swallowQty_spinbox = Spinbox(containerFrameItems,from_ = 1,to='infinity',state=DISABLED)
swallowQty_spinbox.grid(row =1 ,column =2)

swallowRate_spinbox = Spinbox(containerFrameItems,from_ = 20,to='infinity',state=DISABLED)
swallowRate_spinbox.grid(row =1 ,column =3)

swallowAmount = Entry(containerFrameItems,state=DISABLED)
swallowAmount.grid(row =1 ,column =4)

#------------------------FOR SOUP--------------------------------------------
check_var_soup = BooleanVar()
soup_check = Checkbutton(containerFrameItems,text = "Soup",variable=check_var_soup, command=toggle_widget_soup)
soup_check.grid(row =2,column =0)

soup_combobox = ttk.Combobox(containerFrameItems,values =["Okro","Native","Bitterleave","Oha","Afang","Fisher-Man","Gnut Soup"],state=DISABLED)
soup_combobox.grid(row = 2,column = 1)

soupQty_spinbox = Spinbox(containerFrameItems,from_ = 1,to='infinity',state=DISABLED)
soupQty_spinbox.grid(row =2 ,column =2)

soupRate_spinbox = Spinbox(containerFrameItems,from_ = 20,to='infinity',state=DISABLED)
soupRate_spinbox.grid(row =2 ,column =3)

soupAmount = Entry(containerFrameItems,state=DISABLED)
soupAmount.grid(row =2 ,column =4)

#------------------------FOR PROTEIN--------------------------------------------
check_var_protein = BooleanVar()
protein_check = Checkbutton(containerFrameItems,text = "Protein",variable=check_var_protein, command=toggle_widget_protein)
protein_check.grid(row =3 ,column =0)

protein_combobox = ttk.Combobox(containerFrameItems,values =["Goatmeat","Chicken","Turkey","Croker-Fish","Assorted","Cat-Fish"],state=DISABLED)
protein_combobox.grid(row = 3,column = 1)

proteinQty_spinbox = Spinbox(containerFrameItems,from_ = 1,to='infinity',state=DISABLED)
proteinQty_spinbox.grid(row =3 ,column =2)

proteinRate_spinbox = Spinbox(containerFrameItems,from_ = 20,to='infinity',state=DISABLED)
proteinRate_spinbox.grid(row =3 ,column =3)

proteinAmount = Entry(containerFrameItems,state=DISABLED)
proteinAmount.grid(row =3 ,column =4)

#------------------------FOR DRINKS--------------------------------------------
check_var_drink = BooleanVar()
drink_check = Checkbutton(containerFrameItems,text = "Drinks",variable=check_var_drink, command=toggle_widget_drink)
drink_check.grid(row =4 ,column =0)

drink_combobox = ttk.Combobox(containerFrameItems,values =["Wine","Juice","Bottle-Water","Minerals","Malt"],state=DISABLED)
drink_combobox.grid(row = 4,column = 1)

drinkQty_spinbox = Spinbox(containerFrameItems,from_ = 1,to='infinity',state=DISABLED)
drinkQty_spinbox.grid(row =4 ,column =2)

drinkRate_spinbox = Spinbox(containerFrameItems,from_ = 20,to='infinity',state=DISABLED)
drinkRate_spinbox.grid(row =4 ,column =3)

drinkAmount = Entry(containerFrameItems,state=DISABLED)
drinkAmount.grid(row =4 ,column =4)

orderButton = Button(containerFrameItems,text = "Place Order"
                     ,relief = GROOVE,bd=10
                ,bg="red",fg="white"
                ,font="bold"
                     ,command = order)
orderButton.grid(row =5 ,column =0)

clearButton = Button(containerFrameItems,text = "Clear"
                     ,relief = GROOVE,bd=10
                ,bg="red",fg="white"
                ,font="bold",command = clear)
clearButton.grid(row =5 ,column =1)

exitButton = Button(containerFrameItems,text = "Exit"
                     ,relief = GROOVE,bd=10
                ,bg="red",fg="white"
                ,font="bold"
                     ,command = exitProgram)
exitButton.grid(row =5 ,column =2)



for widget in containerFrameItems.winfo_children():
    widget.grid_configure(padx = 20,pady = 10)
    widget.configure(font = "14",width = 8)







 
root.mainloop()
