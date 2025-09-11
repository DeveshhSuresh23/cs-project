import tkinter

tk=tkinter
#main starting
root=tk.Tk()
root.title('MENU')
root.geometry('1500x600')
root.configure(bg='black')
s=''
i=tk.IntVar()
# a control variable that is something that hold a integer has been created
i.set(3)
#i am setting its value to 3
final=[]
appsorder=[]
entreesorder=[]
dessertsorder=[]
#***********************
#sorting if member or not
#defining functions
def showmenu():
    if i.get()!=3:
        global wind2
        wind2.withdraw()
    if i.get()==0:
        discount=0
        menu()
        
    else:
        wind5=tkinter.Toplevel(root)
        wind5.title('MENU')
        wind5.geometry('1500x600')
        wind5.configure(bg='black')
        name=tk.Entry(wind5,width=30,bg='white')
        name.place(x=50,y=24)
        namelabel=tk.Label(wind5,text=('name'),fg='white',bg='black')
        namelabel.place(x=0,y=24)

        passcode=tk.Entry(wind5,width=30,bg='white',show='*')
        passcode.place(x=50,y=70)
        passcodelabel=tk.Label(wind5,text=('passcode'),fg='white',bg='black')
        passcodelabel.place(x=0,y=70)

        menu()

#what to do if guest    
def guest():
    global i
    global wind2
    root.withdraw()
    wind2=tk.Toplevel(root)
    wind2.geometry('1500x600')
    wind2.configure(bg='black')
    member=tk.Radiobutton(wind2,text='member',font=(30),fg='black',bg='#E16C2E',value=1,variable=i)
    member.place(x=50,y=100)

    notmember=tk.Radiobutton(wind2,text='not a member',font=(30),fg='black',bg='#E16C2E',value=0,variable=i)
    notmember.place(x=300,y=100)

    submit=tk.Button(wind2,text='SUBMIT',font=(30),fg='black',bg='#E16C2E',command=showmenu)
    submit.place(x=175,y=300)

    how=tkinter.Button(wind2,text='INSTRUCTIONS', font=('Arial', 14), fg='black', bg='#E16C2E',command=lambda: [wind2.withdraw(), howto()])
    how.place(x=500,y=400)
#what to do if staff
def staff():
    root.withdraw()
    wind6=tk.Tk()
    wind6.geometry('1500x900')
    wind6.title('staff verification')
    wind6.configure(bg='black')
    name=tk.Entry(wind6,width=30,bg='white')
    name.place(x=50,y=24)
    namelabel=tk.Label(wind6,text=('name'),fg='white',bg='black')
    namelabel.place(x=0,y=24)

    passcode=tk.Entry(wind6,width=30,bg='white',show='*')
    passcode.place(x=50,y=70)
    passcodelabel=tk.Label(wind6,text=('passcode'),fg='white',bg='black')
    passcodelabel.place(x=0,y=70)
    
#staff and guest buttons in root
staff=tk.Button(root,text='click if staff',font=(30),fg='black',bg='#E16C2E',command=staff)
staff.place(x=50,y=100)

guest=tk.Button(root,text='click if guest',font=(30),fg='black',bg='#E16C2E',command=guest)
guest.place(x=200,y=100)

appslist = [
    "Spinach Artichoke Dip",
    "Crispy Spring Rolls",
    "Caprese Skewers",
    "Mini Crab Cakes",
    "Garlic Parmesan Breadsticks",
    "Loaded Potato Skins",
    "Shrimp Cocktail",
    "Hummus Platter",
    "Chicken Satay",
    "Bruschetta"
]

entreeslist = [
    "Grilled Salmon",
    "Chicken Tikka Masala",
    "Classic Beef Lasagna",
    "Mushroom Risotto",
    "Pan-Seared Duck Breast",
    "Spicy Shrimp Scampi",
    "Vegetable Korma",
    "New York Strip Steak",
    "Lamb Shank",
    "Black Bean Burger"
]

dessertslist = [
    "Chocolate Lava Cake",
    "New York Style Cheesecake",
    "Tiramisu",
    "Apple Crumble",
    "Crème Brûlée",
    "Brownie Sundae",
    "Key Lime Pie",
    "Red Velvet Cake",
    "Sticky Toffee Pudding",
    "Mango Mousse"
]


def howto():
    global howwind
    howwind1=tk.Toplevel(root)
    howwind1.geometry('1500x900')
    howwind1.configure(bg='black')
    h=tk.Label(howwind1,text="""```
To use the LEXMI NICOS menu application as a guest, follow these instructions:

1.  **Starting the Application**: When the main window appears, click on the "click if guest" button.
2.  **Membership Selection**: A new window will pop up. If you are a member, select "member". Otherwise, choose "not a member".
3.  **Accessing the Menu**:
    * **If you selected "not a member"**: Click "SUBMIT". You will be taken directly to the main "LEXMI NICOS" menu.
    * **If you selected "member"**: Enter any text for "name" and "passcode", then click "Login". This will also take you to the main "LEXMI NICOS" menu.
4.  **Browse Categories**: On the main "LEXMI NICOS" menu, you can click on "Appetizers", "Entrees", or "Desserts" to view items within each category.
5.  **Selecting Items and Quantities**:
    * Once you are on a category screen (Appetizers, Entrees, or Desserts), you will see a list of items.
    * Next to each item, there is an input box. Enter the desired quantity (a whole number) for the item you wish to order.
    * If you do not want an item, leave its input box as '0' or empty.
6.  **Saving Your Selections (Crucial Step!)**: After entering quantities for items in a category, **you MUST click the "Submit" button** (located at the top-left) to save your selections for that category. Failing to click "Submit" will result in your selections not being added to your order.
7.  **Navigating Between Categories**: Use the "Go to Appetizers", "Go to Entrees", or "Go to Desserts" buttons on any category screen to switch between categories. Remember to "Submit" your changes before moving to another category.
8.  **Returning to the Main Menu**: At any point, you can click the "Back to Menu" button to return to the main "LEXMI NICOS" menu.
9.  **Finalizing Your Order**: Once you have made all your selections across all desired categories and clicked "Submit" for each, click the "see order" button (available on any category screen). This will take you to the "FINAL ORDER" screen, where you can review your complete order.
10. **Modifying Your Order**: If you need to make changes after reviewing your final order, use the "Go to" buttons on the "FINAL ORDER" screen to navigate back to the specific category, adjust quantities, click "Submit" again, and then return to "FINAL ORDER" by clicking "see order" again. You can also click the "Refresh" button on the "FINAL ORDER" screen to update the displayed order after making changes in a category.
11. **Exiting the Application**: To close the application, simply close the main "MENU" window using its 'X' button. This will close all associated windows.

**Important Notes**:
* Always click "Submit" after entering quantities for items in a category.
* Only use whole numbers for quantities.
* This version of the application does not calculate prices.
```.""",font=(25),fg='#E16C2E',bg='black')
    h.pack()

    back=tk.Button(howwind1,text='BACK',font=(50),width=40,bg='#E16C2E',fg='black',command=lambda:[howwind1.destroy(),wind2.deiconify()])
    back.place(x=500,y=700)
def menu():
    global wind3
    wind3 = tkinter.Toplevel(root)
    wind3.title('MENU')
    wind3.geometry('1500x600')
    wind3.configure(bg='black')

    wlcm = tkinter.Label(wind3, text="WELCOME TO", font=('TIMES NEW ROMAN', 12), fg='white', bg='black')
    wlcm.place(x=740, y=0)

    ttl = tkinter.Label(wind3, text="LEXMI NICOS", font=('ELEPHANT', 40), fg='#E16C2E', bg='black')
    ttl.place(x=570, y=20)

    appsbutton = tkinter.Button(wind3, text="Appetizers", font=('Arial', 14), fg='black', bg='#E16C2E', width=15, height=2,command=apps)
    appsbutton.place(x=50, y=120)

    entreesbutton = tkinter.Button(wind3, text="Entrees", font=('Arial', 14), fg='black', bg='#E16C2E', width=15, height=2,command=entrees)
    entreesbutton.place(x=250, y=120)

    dessertsbutton = tkinter.Button(wind3, text="Desserts", font=('Arial', 14), fg='black', bg='#E16C2E', width=15, height=2,command=desserts)
    dessertsbutton.place(x=450, y=120)




#finalising the order
def finaliseorder():
    global finalwind
    finalwind = tkinter.Toplevel(root)
    finalwind.title('FINAL ORDER')
    finalwind.geometry('1500x900')
    finalwind.configure(bg='black')

    refresh=tk.Button(finalwind, text='Refresh',font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda:[finalwind.destroy(),finaliseorder()])
    refresh.place(x=500, y=20 * (len(dessertslist) + 8))

    title_label = tk.Label(finalwind, text="YOUR ORDER", font=('ELEPHANT', 20), fg='#E16C2E', bg='black')
    title_label.place(x=600, y=20)
    
    apps_button = tk.Button(finalwind, text="Go to Appetizers", font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [finalwind.withdraw(), apps()])
    apps_button.place(x=150, y=20 * (len(dessertslist) + 6))

    entrees_button = tk.Button(finalwind, text="Go to Entrees", font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [finalwind.withdraw(), entrees()])
    entrees_button.place(x=300, y=20 * (len(dessertslist) + 6))

    desserts_button = tk.Button(finalwind, text="Go to Desserts", font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [finalwind.withdraw(), desserts()])
    desserts_button.place(x=450, y=20 * (len(dessertslist) + 6))

    back_button = tk.Button(finalwind, text="Back to Menu", font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [finalwind.withdraw(), menu()])
    back_button.place(x=600, y=20 * (len(dessertslist) + 6))

    global final
    final = []
    for i in range(len(appslist)):
        global appsorder
        if i<len(appsorder) and appsorder[i] != "0":
            final.append(appslist[i] + ", " + appsorder[i])
    
    for i in range(len(entreeslist)):
        global entreesorder
        if i<len(entreesorder) and entreesorder[i] != "0":
            final.append(entreeslist[i] + ", " + entreesorder[i])

    for i in range(len(dessertslist)):
        global dessertsorder
        if i<len(dessertsorder) and dessertsorder[i] != "0":
            final.append(dessertslist[i] + ", " + dessertsorder[i])

    for i in final:
        j=tk.Label(finalwind,text=i,font=(10),fg='white',bg='black')
        j.place(x=0,y=60+25*(final.index(i)))




#appatizers window    
def apps():
    global finalwind
    wind3.withdraw()
    appswind = tkinter.Toplevel(root)
    appswind.title('APPETIZERS')
    appswind.geometry('1500x900')
    appswind.configure(bg='black')
    global tapps
    tapps = []
    e=''

    beware=tk.Label(appswind,text='do check order before finalising',bg='black',fg='white',font='10')
    beware.place(x=800,y=600)

    for i in appslist:
        if len(i)>len(e):
            e=i
    
    for i in appslist:
        entry = tk.StringVar()
        entry.set('0')

        j = tk.Label(appswind, text=i, font=('Arial', 12), fg='white', bg='black')
        j.place(x=0, y=20 * appslist.index(i))

        k = tk.Entry(appswind, textvariable=entry, width=5, font=('Arial', 12))
        k.place(x=7*len(e)+100, y=20 * appslist.index(i))

        tapps.append(entry)
    def appsfunc():
        global appsorder,tapps,final
        appsorder=[]
        for i in tapps:
            appsorder.append(i.get())
        final = []
        for i in range(len(appslist)):
            if i<len(appsorder) and appsorder[i] != "0":
                final.append(appslist[i] + ", " + appsorder[i])
        
        for i in range(len(entreeslist)):
            if i<len(entreesorder) and entreesorder[i] != "0":
                final.append(entreeslist[i] + ", " + entreesorder[i])

        for i in range(len(dessertslist)):
            global dessertsorder
            if i<len(dessertsorder) and dessertsorder[i] != "0":
                final.append(dessertslist[i] + ", " + dessertsorder[i])

        global s
        s=''
        for i in final:
            s=s+'\n'+i
        ordertext=tk.Label(appswind,text=s,bg='black',fg='white',font=(12))
        ordertext.place(x=800,y=0)
    Submit = tk.Button(appswind, text='Submit', font=('Arial', 14), fg='black', bg='#E16C2E', command=appsfunc)
    Submit.place(x=0, y=20*(len(appslist) + 3))

    def open_entrees():
        appswind.withdraw()
        entrees()

    def open_desserts():
        appswind.withdraw()
        desserts()

    entrees_button = tk.Button(appswind, text="Go to Entrees", font=('Arial', 12), fg='black', bg='#E16C2E', command=open_entrees)
    entrees_button.place(x=150, y=20 * (len(appslist) + 3))

    desserts_button = tk.Button(appswind, text="Go to Desserts", font=('Arial', 12), fg='black', bg='#E16C2E', command=open_desserts)
    desserts_button.place(x=300, y=20 * (len(appslist) + 3))

    back_button = tk.Button(appswind, text="Back to Menu", font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [appswind.withdraw(), menu()])
    back_button.place(x=450, y=20 * (len(appslist) + 3))

    global finalwind
    Finalise=tk.Button(appswind,text='see order',font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [appswind.withdraw(), finaliseorder()])
    Finalise.place(x=300,y=20*(len(appslist)+6))




#entrees window
def entrees():
    wind3.withdraw()
    entreewind = tkinter.Toplevel(root)
    entreewind.title('ENTREES')
    entreewind.geometry('1500x900')
    entreewind.configure(bg='black')

    t = []

    e=''
    for i in entreeslist:
        if len(i)>len(e):
            e=i
    beware=tk.Label(entreewind,text='do check order before finalising',bg='black',fg='white',font='10')
    beware.place(x=800,y=600)
      
    for i in entreeslist:
        entry = tk.StringVar()
        entry.set('0')

        j = tk.Label(entreewind, text=i, font=('Arial', 12), fg='white', bg='black')
        j.place(x=0, y=20 * entreeslist.index(i))

        k = tk.Entry(entreewind, textvariable=entry, width=5, font=('Arial', 12))
        k.place(x=7*len(e)+100, y=20 * entreeslist.index(i))

        t.append(entry)

    def entreesfunc():
        global entreesorder
        entreeorder=[]
        for i in t:
            entreesorder.append(i.get())

        final = []
        for i in range(len(appslist)):
            if i<len(appsorder) and appsorder[i] != "0":
                final.append(appslist[i] + ", " + appsorder[i])
        
        for i in range(len(entreeslist)):
            if i<len(entreesorder) and entreesorder[i] != "0":
                final.append(entreeslist[i] + ", " + entreesorder[i])

        for i in range(len(dessertslist)):
            global dessertsorder
            if i<len(dessertsorder) and dessertsorder[i] != "0":
                final.append(dessertslist[i] + ", " + dessertsorder[i])

        global s
        s=''
        for i in final:
            s=s+'\n'+i
        ordertext=tk.Label(entreewind,text=s,bg='black',fg='white',font=(12))
        ordertext.place(x=800,y=0)
    Submit = tk.Button(entreewind, text='Submit', font=('Arial', 14), fg='black', bg='#E16C2E', command=entreesfunc)
    Submit.place(x=0, y=20 * (len(entreeslist) + 3))

    def open_apps():
        entreewind.withdraw()
        apps()

    def open_desserts():
        entreewind.withdraw()
        desserts()

    apps_button = tk.Button(entreewind, text="Go to Appetizers", font=('Arial', 12), fg='black', bg='#E16C2E', command=open_apps)
    apps_button.place(x=150, y=20 * (len(entreeslist) + 3))

    desserts_button = tk.Button(entreewind, text="Go to Desserts", font=('Arial', 12), fg='black', bg='#E16C2E', command=open_desserts)
    desserts_button.place(x=300, y=20 * (len(entreeslist) + 3))

    back_button = tk.Button(entreewind, text="Back to Menu", font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [entreewind.withdraw(), menu()])
    back_button.place(x=450, y=20 * (len(entreeslist) + 3))

    global finalwind
    Finalise=tk.Button(entreewind,text='see order',font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [entreewind.withdraw(), finaliseorder()])
    Finalise.place(x=300,y=20*(len(entreeslist)+6))






#desserts window
def desserts():
    wind3.withdraw()
    dessertswind = tkinter.Toplevel(root)
    dessertswind.title('DESSERTS')
    dessertswind.geometry('1500x900')
    dessertswind.configure(bg='black')

    t = []

    e=''
    for i in dessertslist:
        if len(i)>len(e):
            e=i
    beware=tk.Label(dessertswind,text='do check order before finalising',bg='black',fg='white',font='10')
    beware.place(x=800,y=600)
    

    for i in dessertslist:
        entry = tk.StringVar()
        entry.set('0')

        j = tk.Label(dessertswind, text=i, font=('Arial', 12), fg='white', bg='black')
        j.place(x=0, y=20 * dessertslist.index(i))

        k = tk.Entry(dessertswind, textvariable=entry, width=5, font=('Arial', 12))
        k.place(x=7*len(e)+100, y=20 * dessertslist.index(i))

        t.append(entry)

    def dessertsfunc():
        global dessertsorder
        dessertsorder=[]
        for i in t:
            dessertsorder.append(i.get())

        final = []
        for i in range(len(appslist)):
            if i<len(appsorder) and appsorder[i] != "0":
                final.append(appslist[i] + ", " + appsorder[i])
        
        for i in range(len(entreeslist)):
            if i<len(entreesorder) and entreesorder[i] != "0":
                final.append(entreeslist[i] + ", " + entreesorder[i])

        for i in range(len(dessertslist)):
            dessertsorder
            if i<len(dessertsorder) and dessertsorder[i] != "0":
                final.append(dessertslist[i] + ", " + dessertsorder[i])

        global s
        s=''
        for i in final:
            s=s+'\n'+i
        ordertext=tk.Label(appswind,text=s,bg='black',fg='white',font=(12))
        ordertext.place(x=800,y=0)
        
    Submit = tk.Button(dessertswind, text='Submit', font=('Arial', 14), fg='black', bg='#E16C2E', command=dessertsfunc)
    Submit.place(x=0, y=20 * (len(dessertslist) + 3))

    def open_apps():
        dessertswind.withdraw()
        apps()

    def open_entrees():
        dessertswind.withdraw()
        entrees()

    apps_button = tk.Button(dessertswind, text="Go to Appetizers", font=('Arial', 12), fg='black', bg='#E16C2E', command=open_apps)
    apps_button.place(x=150, y=20 * (len(dessertslist) + 3))

    entrees_button = tk.Button(dessertswind, text="Go to Entrees", font=('Arial', 12), fg='black', bg='#E16C2E', command=open_entrees)
    entrees_button.place(x=300, y=20 * (len(dessertslist) + 3))

    back_button = tk.Button(dessertswind, text="Back to Menu", font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [dessertswind.withdraw(), menu()])
    back_button.place(x=450, y=20 * (len(dessertslist) + 3))
    global finalwind
    Finalise=tk.Button(dessertswind,text='see order',font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [dessertswind.withdraw(), finaliseorder()])
    Finalise.place(x=300,y=20*(len(dessertslist)+6))











