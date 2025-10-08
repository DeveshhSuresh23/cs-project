import tkinter

tk=tkinter
#main starting
root=tk.Tk()
root.title('MENU')
root.geometry('1500x600')
root.configure(bg='black')
s=''
i=tk.IntVar()
i.set(3)
final=[]
appsorder=[]
entreesorder=[]
dessertsorder=[]
#sorting if member or not
def showmenu():
    if i.get()!=3:
        global wind2
        wind2.withdraw()
    if i.get()==0:
        discount=0
        menu()
    else:
        global wind5
        wind5 = tk.Toplevel(root)
        wind5.title('Member Verification')
        wind5.geometry('600x300')  # same compact window as staff
        wind5.configure(bg='black')

        # Name Label and Entry
        namelabel = tk.Label(wind5, text='Name:', fg='white', bg='black', font=('Arial', 12))
        namelabel.place(x=50, y=40)
        name = tk.Entry(wind5, width=30, bg='white', font=('Arial', 12))
        name.place(x=150, y=40)

        # Passcode Label and Entry
        passcodelabel = tk.Label(wind5, text='Passcode:', fg='white', bg='black', font=('Arial', 12))
        passcodelabel.place(x=50, y=90)
        passcode = tk.Entry(wind5, width=30, bg='white', show='*', font=('Arial', 12))
        passcode.place(x=150, y=90)

        members = {'a':'1'}

        def check():
            namegiven = name.get()
            code = passcode.get()
            for namegiven in members.keys():
                if code == members[namegiven]:
                    result = tk.Label(wind5, text='ACCESS GRANTED', fg='white', bg='black', font=('Arial', 12, 'bold'))
                    result.place(x=220, y=180)
                    # keep your original call to menu() if you want it after login
                    menu()
                    break
                else:
                    result = tk.Label(wind5, text='ACCESS DENIED', fg='white', bg='black', font=('Arial', 12, 'bold'))
                    result.place(x=220, y=180)

        # Submit Button
        submit = tk.Button(wind5, text='SUBMIT', font=('Arial', 12, 'bold'),
                           fg='black', bg='#E16C2E', width=10, height=1, command=check)
        submit.place(x=250, y=140)
######################################################################################################################################################################

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
    wind6 = tk.Tk()
    wind6.geometry('600x300')  # More compact and centered window
    wind6.title('Staff Verification')
    wind6.configure(bg='black')

    # Name Label and Entry
    namelabel = tk.Label(wind6, text='Name:', fg='white', bg='black', font=('Arial', 12))
    namelabel.place(x=50, y=40)
    name = tk.Entry(wind6, width=30, bg='white', font=('Arial', 12))
    name.place(x=150, y=40)

    # Passcode Label and Entry
    passcodelabel = tk.Label(wind6, text='Passcode:', fg='white', bg='black', font=('Arial', 12))
    passcodelabel.place(x=50, y=90)
    passcode = tk.Entry(wind6, width=30, bg='white', show='*', font=('Arial', 12))
    passcode.place(x=150, y=90)

    employee = {'a': '1'}

    def check():
        namegiven = name.get()
        code = passcode.get()
        for namegiven in employee.keys():
            if code == employee[namegiven]:
                result = tk.Label(wind6, text='ACCESS GRANTED', fg='white', bg='black', font=('Arial', 12, 'bold'))
                result.place(x=220, y=180)
            else:
                result = tk.Label(wind6, text='ACCESS DENIED', fg='white', bg='black', font=('Arial', 12, 'bold'))
                result.place(x=220, y=180)

    # Submit Button
    submit = tk.Button(wind6, text='SUBMIT', font=('Arial', 12, 'bold'), fg='black', bg='#E16C2E', width=10, height=1, command=check)
    submit.place(x=250, y=140)

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
    howwind1 = tk.Toplevel(root)
    howwind1.geometry('1000x700')  # smaller but comfortably readable window
    howwind1.configure(bg='black')
    howwind1.title('How to Use the App')

    instructions = (
        "📝 HOW TO USE:\n\n"
        "• If you're a member, select 'Member' and enter any text for Name and Passcode, then click 'Login'.\n"
        "• If you're not a member, choose 'Not a Member' and click 'SUBMIT' to open the main 'LEXMI NICOS' menu.\n\n"
        "• On the menu screen, click 'Appetizers', 'Entrees', or 'Desserts' to browse food categories.\n"
        "• In each category, type the quantity you want next to each item (leave it blank or 0 if you don’t want that item).\n"
        "• Important: click 'Submit' at the top-left to save your selections before moving to another category.\n\n"
        "• Use the 'Go to' buttons to navigate between categories.\n"
        "• Click 'Back to Menu' anytime to return to the main menu.\n"
        "• Once done, click 'Finalise Order' to review your complete order.\n"
        "• To make changes, go back using the 'Go to' buttons, edit quantities, click 'Submit' again, and re-finalize your order.\n\n"
        "• To exit, simply close the main 'MENU' window using the 'X' button.\n\n"
        "💡 Tips:\n"
        "  - Always click 'Submit' after entering quantities.\n"
        "  - Use only whole numbers (no decimals or letters).\n"
        "  - This version does not calculate prices."
    )

    h = tk.Label(
        howwind1,
        text=instructions,
        font=('Arial', 14),
        fg='#E16C2E',
        bg='black',
        justify='left',
        wraplength=950,  # ensures wrapping within the window
    )
    h.pack(padx=30, pady=30, anchor='w')

    back = tk.Button(
        howwind1,
        text='BACK',
        font=('Arial', 14, 'bold'),
        width=25,
        bg='#E16C2E',
        fg='black',
        command=lambda: [howwind1.destroy(), wind2.deiconify()]
    )
    back.pack(pady=20)

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
        global appsorder,tapps,final,entreesorder,dessertsorder
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
    Finalise=tk.Button(appswind,text='Finalise order',font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [appswind.withdraw(), finaliseorder()])
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
        
    for i in entreeslist:
        entry = tk.StringVar()
        entry.set('0')

        j = tk.Label(entreewind, text=i, font=('Arial', 12), fg='white', bg='black')
        j.place(x=0, y=20 * entreeslist.index(i))

        k = tk.Entry(entreewind, textvariable=entry, width=5, font=('Arial', 12))
        k.place(x=7*len(e)+100, y=20 * entreeslist.index(i))

        t.append(entry)

    def entreesfunc():
        global entreesorder, appsorder, dessertsorder
        entreesorder=[]
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
    Finalise=tk.Button(entreewind,text='Finalise order',font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [entreewind.withdraw(), finaliseorder()])
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
        

    for i in dessertslist:
        entry = tk.StringVar()
        entry.set('0')

        j = tk.Label(dessertswind, text=i, font=('Arial', 12), fg='white', bg='black')
        j.place(x=0, y=20 * dessertslist.index(i))

        k = tk.Entry(dessertswind, textvariable=entry, width=5, font=('Arial', 12))
        k.place(x=7*len(e)+100, y=20 * dessertslist.index(i))

        t.append(entry)

    def dessertsfunc():
        global dessertsorder, appsorder, entreesorder
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
            if i<len(dessertsorder) and dessertsorder[i] != "0":
                final.append(dessertslist[i] + ", " + dessertsorder[i])

        global s
        s=''
        for i in final:
            s=s+'\n'+i
        ordertext=tk.Label(dessertswind,text=s,bg='black',fg='white',font=(12))
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
    Finalise=tk.Button(dessertswind,text='Finalise order',font=('Arial', 12), fg='black', bg='#E16C2E', command=lambda: [dessertswind.withdraw(), finaliseorder()])
    Finalise.place(x=300,y=20*(len(dessertslist)+6))
