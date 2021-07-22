import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Gauranitai27#",database="fooddelivery")
mycursor=mydb.cursor()
    

def validate_login(username,password):
    mycursor.execute("select * from userdetails where username like %s",(username,))
    data=mycursor.fetchall()
    name=data[0][1]
    passw=data[0][2] 
    if name==username and passw==password:
        return 1


def order(username):
    print("1:Idly"+'\n'+"2:Dosa"+'\n'+"3:Meal"+'\n'+"4:Biriyani"+'\n'+"5:Parotta")
    d={1:"Idly",2:"Dosa",3:"Meal",4:"Biriyani",5:"Parotta"}
    print("Enter your option :")
    option=int(input())
    if option>=1 and option<=5:
        
        food=d[option]
        mycursor.execute("select cost from fooddetails where foodname like %s",(food,))
        data=mycursor.fetchone()
        cost=int(data[0])
        print("Enter the count of order :")
        count=int(input())
        global totalcost
        totalcost=cost*count 
        mycursor.execute("insert into orderdetails(username,foodordered,totalcost) values (%s,%s,%s)",(username,food,totalcost,))
        mydb.commit()
        mycursor.execute("select * from orderdetails where username like %s",(username,))
        data=mycursor.fetchall()
        name=data[-1][0]
        food=data[-1][1]
        cost=data[-1][2] 
        print("Name :%s"%name)
        print("Food Ordered :%s"%food)
        print("Total Cost :%s"%cost)
        return 1
    else:
        print("Invalid option")
        return 0 


def display(username):
    mycursor.execute("select * from orderdetails where username like %s",(username,))
    data=mycursor.fetchall() 
    if data:
        print("Name :%s"%data[0][0])
        for row in range(len(data)):
            print("Food Ordered :%s"%data[row][1])
            print("Total Cost :%s"%data[row][2])
    else:
        print("No Records found!")
    return 1

def display_user(username):
    mycursor.execute("select * from userdetails where username like %s",(username,))
    data=mycursor.fetchall()
    print("User_Id :%s"%data[0][0])
    print("Name:%s"%data[0][1])
    for row in range(len(data)):
        print("Password :%s"%data[row][2])
        print("Mail :%s"%data[row][3])
        print("Phone :%s"%data[row][4])
        print("Address :%s"%data[row][5])
        print()
    return 1

def display_all():
    mycursor.execute("select * from userdetails")
    data=mycursor.fetchall() 
    for row in range(len(data)):
        print("User_Id :%s"%data[row][0])
        print("Name:%s"%data[row][1])
        print("Password :%s"%data[row][2])
        print("Mail :%s"%data[row][3])
        print("Phone :%s"%data[row][4])
        print("Address :%s"%data[row][5])
        print()
    return 1

def display_food():
    mycursor.execute("select * from fooddetails")
    data=mycursor.fetchall() 
    for row in range(len(data)):
        print("Foodname :%s"%data[row][0],end=" ")
        print("Cost:%s"%data[row][1])
        print()
    
def display_orders():
    mycursor.execute("select * from orderdetails")
    data=mycursor.fetchall() 
    if data:
        for row in range(len(data)):
            print("Name :%s"%data[row][0],end="       ")
            print("Foodname :%s"%data[row][1],end="        ")
            print("Cost:%s"%data[row][2])
            print()
    else:
        print("No Records found!")


print("welcome to Foodparadise !!") 
destination=input("Are you a user or admin or newuser?"+'\n'+" Type your destination :") 
destination=destination.lower()

if destination=="newuser":
    username=input("Enter your name :")
    password=input("Enter your password :")
    mail=input("Enter your mail :")
    phone=input("Enter your Phone number :")
    address=input("Enter your address :")
    mycursor.execute("insert into userdetails(userid,username,password,mail,phone,address) values(NULL,%s,%s,%s,%s,%s)",(username,password,mail,phone,address,))
    mydb.commit()
    print("Registration success !!")


if destination=="user":
    username=input("Enter your name :")
    password=input("Enter your password :")
    if validate_login(username,password):
        print("1:Order food ")
        print("2:Display my previous orders")
        option=int(input("Enter your option :"))
        if option==1:
            if order(username):
                print("Order Success")
        elif option==2:
            display(username) 
        else:
            print("Invalid option Please enter valid option")
    else:
        print("User does not exist") 


if destination=="admin":
    print("1.Display the particular user details"+'\n'+"2.Display all the records"+'\n'+"3.Display food table"+'\n'+"4.Display order details")
    print("Enter your option :")
    option=int(input())
    if option==1:
        username=input("Enter the username: ")
        display_user(username)
    elif option==2:
        display_all() 
    elif option==3:
        display_food() 
    elif option==4:
        display_orders()
    else:
        print("Invalid option Please choose correct option!")