# Using OOP
class receptionist: # Reciptionist & Manager Rules #Employee in Hospital
    def check_rooms(self):    # Check empty rooms 
        for i,j in rooms.items():
            if j == 0:
                print("The Empty Rooms is : " + i )
    def new_reservation(self):   # New Reservation
    
        while True:
            print("If you want to make a new reservation press Y" +  
                  " if you want to exit press N")
            check = input()
            if check == "Y" :   
                room = input("Enter Your Choosen Room\n")
                self.iden = int(input("Please Enter your National ID\n"))
                rooms[room] = self.iden

                details = ["name", "age", "adress",
                           "phone", "blood", "gender", "disese"]
                a = input("Please Enter Your Name \n")
                details.insert(0, a)
                b = int(input("Please Enter Your Age \n"))
                details.insert(1, b)
                c = input("Please Enter Your Adress \n")
                details.insert(2, c)
                d = int(input("Please Enter Your Phone Number \n"))
                details.insert(3, d)
                e = input("Please Enter Your Blood Type \n")
                details.insert(4, e)
                f = input("Please Enter Your Gender \n")
                details.insert(5, f)
                g = input("Please Enter Your Disese \n")
                details.insert(6, g)
                reservation[self.iden] = details
                print("\n" + str(self.iden) + " You are Now in " + str(room) + "\n")
            else:
                print("Thank you for Using our System")
                break
    
    def check_out(self):   
        self.iden = int(input("Please Enter your National ID\n"))
        night = int(input("Please Enter Number of Nights in Hospital\n"))
        price = night * 300 
        for i,j in reservation.items():
            if i == self.iden :
                print("Your Totally price is : "+str(price))
            else:
                print("sorry you aren't register in the system of Hospital")
                break

# inhertance in OOP
class receptionist_manager(receptionist):    #Employee in Hospital
    def remove(self):   #remove reservation
        while True:
            print("If you want to remove in reservation press Y" +  
                  " if you want to exit press N")
            check = input()
            if check == "Y" :
                self.iden = input("Please Enter The ID : \n")
                for i ,j in reservation.items():
                    if i == self.iden :
                        print("Successfully Removed")
                        reservation.pop(self.iden)
                    else:
                        print("This Items isn't found")
            else:
                sign_out()
    def edit(self):    #edit reservation
        while True:
            print("If you want to edit in reservation press Y" +  
                  " if you want to exit press N")
            check = input()
            if check == "Y" :
                self.iden = input("Please Enter The ID : \n")
                for i ,j in reservation.items():
                    if i == self.iden :
                        details = ["name","age","adress","phone","blood","gender","disese"]
                        x = input("Please Enter Your Name \n")
                        z = details.insert(0,x)
                        b = int(input("Please Enter Your Age \n"))
                        z = details.insert(1,b)
                        c = input("Please Enter Your Adress \n")
                        z = details.insert(2,c)
                        d = int(input("Please Enter Your Phone Number \n"))
                        z = details.insert(3,d)
                        e = input("Please Enter Your Blood Type \n")
                        z = details.insert(4,e)
                        f = input("Please Enter Your Gender \n")
                        z = details.insert(5,f)
                        g = input("Please Enter Your Disese \n")
                        z = details.insert(6,g)
                        reservation[self.iden]= details
                        print("Successfully Edition")
                    else:
                        print("This Items isn't found")

            else:
                       sign_out()

def log_in (failure):   #log in the system  # First Operation
    while failure<3: 
        user = input("Please Enter Your UserName : \n").strip()
        password = input("Please Enter Your Password : \n").strip()
        for i,j in employee.items():  # loop to check the employee
            if i == user and j == password :
                    print ("\nWelcome (" + i + ") in our System ")
                    global b
                    for a,b in assign.items():
                        if a == i :
                            print("you are " + b)
                            for f,g in roles.items():
                                if f == b :
                                    print("your roles is :" )
                                    for c in g:
                                        print("    " + c)
                                    check(b)
                                    sign_out()
                                        
        else:
            print("Incorrect username or password")
            failure+=1
    else:
        print("\nYou aren't Allow To Enter in our System in This Time")
                              
def check(b):    #Second Operation
    if b == "Admin":
        Admin()
    elif b == "Receptionist":
        a = receptionist()
        while True:
            print("If You Want To Continue  press ' Y' \n")
            confirm = input()
            if confirm == "Y":
                print("1.Check Empty Rooms","\n2.New Reservation","\n3.check Out","\n____________________")
                confirm1 = input()
                if confirm1 =="1":
                    a.check_rooms()
                    a.new_reservation()
                elif confirm1 == "2":
                    a.new_reservation()
                elif confirm1 == "3":
                    a.check_out()

            else:
                break

    elif b == "Reports_User":
        Reports_User()
    elif b == "Receptionist_Manager":
        c = receptionist_manager()
        while True:
            print("If You Want To Continue  press ' Y' \n")
            confirm = input()
            if confirm == "Y":
                print("1.Check Empty Rooms","\n2.New Reservation","\n3.check Out","\n4.Remove Reservation","\n5.Edit Reservation","\n____________________")
                confirm1 = input()
                if confirm1 =="1":
                    c.check_rooms()
                    c.new_reservation()
                elif confirm1 == "2":
                    c.new_reservation()
                elif confirm1 == "3":
                    c.check_out()
                elif confirm1 == "4":
                    c.remove()
                elif confirm1 == "5":
                    c.edit()
            else:
                break

def Admin():    #Employee in Hospital
    while True:
            print("If You Want To Continue  press ' Y' \n")
            confirm = input()
            if confirm == "Y":
                print("Enter your new member information")
                add = input("Please Enter your username : \n").strip()
                value = input("Please Enter your password : \n").strip()
                employee[add] = value  
            else:
                sign_out()

def Reports_User():  #Employee in Hospital
    while True:
            print("If You Want To Write a Report of Patient press ' Y' \n")
            confirm = input()
            if confirm == "Y":
                y = int(input("Please Enter Your ID\n"))
                x= input("Please Write Your Report : \n").strip()
                print("\n"+ str(y)+"\nYour Report is \n" + x)
            else:
                sign_out()
    
    
    
def sign_out(): #out of System
    while True:
            print("If You Want To Sign Out  press ' Y'  any Thing else press N \n")
            confirm = input()
            if confirm == "Y":
                    break
                    
            

                
employee = {"ahmed_ayman":"123@ahm","mohamed":"1245@$","hussein":"1346790","ibrahim":"adanyf1459"}

roles = {"Admin":["Create New User"],"Receptionist":["1.Check Rooms","2.New Reservation","3.Check Out"]
            ,"Reports_User":["Generating Report"],
            "Receptionist_Manager":["1.Check Rooms","2.New Reservation","3.Check Out","4.Remove Reservation","5.Edit Reservation"]}

assign = {"ahmed_ayman":"Admin","mohamed":"Receptionist","hussein":"Reports_User","ibrahim":"Receptionist_Manager"}

rooms = {"Room1":1,"Room2":1,"Room3":0,"Room4":1,"Room5":1,"Room6":0,"Room7":0,"Room8":0,"Room9":1}
reservation = {}

print("Welcome in ElShams Hospital")
failure = 0
log_in(failure)

