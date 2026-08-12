import mysql.connector as sql
import datetime as dt

# Database Connection & Initial Setup
con = sql.connect(host="localhost", user="root", password="1234")
c = con.cursor()
c.execute("create database if not exists BMS")
c.execute("use BMS")
c.execute("create table if not exists Products(ItNo int(6) unique, Category varchar(25), Item varchar(25), Stock int, Price int)")
con.commit()


# 1. ADD NEW ITEM
def AddItem():
    print("\n")
    n = int(input("Enter ItemNo : "))
    cat = input("Enter Category : ")
    item = input("Enter Item : ")
    stock = int(input("Enter product stock : "))
    price = int(input("Enter the price : "))
    try:
        a = "insert into Products values(%s,%s,%s,%s,%s)"
        data = (n, cat, item, stock, price)
        c.execute(a, data)
        con.commit()
        print("\n ***ITEM ADDED TO THE MENU***")
    except:
        print("Database Error. Please try again later")
    main()


# 2. DISPLAY DETAILS OF AN ITEM
def Find():
    d = int(input("Enter ItemNo: "))
    c.execute("select Itno from products")
    itnolist = c.fetchall()
    if (d,) in itnolist:
        c.execute("Select * from Products where ItNo={}".format(d))
        F = c.fetchone()
        print('\n' * 2)
        print("---------------------------------------------------------------------------------")
        print("{0:<10}{1:<10}{2:<25}{3:<8}{4:<8}".format('PNO', 'CATEGORY', 'ITEM', 'QNTY', 'PRICE'))
        print("---------------------------------------------------------------------------------")
        print("{0:<10}{1:<10}{2:<25}{3:<8}{4:<8}".format(F[0], str(F[1]), str(F[2]), F[3], F[4]))
        print("---------------------------------------------------------------------------------")
    else:
        print("The Specified Item Doesn't Exist.")
    main()


# 3. ORDERING FROM MENU
def Order():
    Menu()
    name = input("ENTER CUSTOMER NAME:")
    n = int(input("HOW MANY ITEMS WOULD THE CUSTOMER LIKE TO ORDER?"))
    lst = []
    nst = []
    for i in range(n):
        try:
            print("\n")
            d = input("Enter ItemNo: ")
            c.execute("Select Item,Price,stock from Products where ItNo={}".format(d))
            F = c.fetchone()
            print("SELECTED ITEM : ", F[0], "|", "PRICE = Rs.", F[1], '/-')
            qnty = int(input("Quantity Required:"))
            availqty = F[2]
            if qnty > availqty:
                print("Sorry, we do not have that much stock left.")
                continue
            else:
                nst.append(F[0])
                lst.append(F[1] * qnty)
                c.execute("update products set stock = stock -{} where Itno={}".format(qnty, d))
        except:
            print("Item doesn't exist")

    print('\n', '----------------------------------------------------------------------------')
    print("\t BAKE 'N TAKE \n \t\t\tWe make edible Incredible!! \n DATE:", dt.date.today())
    print('\n')
    print("CUSTOMER:", name)
    print('\n')
    print(' SNO ', '\t', 'ITEM', '\t', ' PRICE')
    for i in range(len(nst)):
        print(" ", i + 1, '\t', nst[i], '\t', lst[i])

    total_amount = 0
    for a in range(len(lst)):
        total_amount += lst[a]

    print('\n AMOUNT PAYABLE = Rs.', total_amount)
    print('\n \n \t \t \t THANK YOU FOR YOUR PURCHASE 😊 ')
    print('---------------------------------------------------------------------------------')
    choice = input("CONFIRM ORDER?(Y/N)")
    if choice.upper() == "Y":
        con.commit()
        print('\n ***ORDER PLACED***\n')
        main()
    else:
        Order()


# 4. UPDATING AN ITEM
def UpdtIt():
    d = input("Enter ItemNo: ")
    c.execute("Select * from Products where ItNo={}".format(d))
    F = c.fetchone()
    if F:
        print(" 1.Update Quantity \n 2.Update Price")
        ch = int(input("Choice(1|2) :"))
        if ch == 1:
            s = int(input("New Quantity :"))
            c.execute("Update Products set Stock={} where ItNo={}".format(s, d))
            con.commit()
            print("UPDATED SUCCESSFULLY")
            main()
        elif ch == 2:
            p = int(input("New Price:"))
            c.execute("Update Products set Price={} where ItNo={}".format(p, d))
            con.commit()
            print("PRICE UPDATED SUCCESSFULLY")
            main()
        else:
            print("..Choice Invalid...Redirecting...")
            main()
    else:
        print("The specified item doesnt exist")
        UpdtIt()


# 5. DISPLAY MENU (INTERNAL)
def Menu():
    c.execute("Select ItNo,Item,Price from Products")
    F = c.fetchall()
    print("\n*--------------------------------------------*")
    print("*                    MENU                    *")
    print("*--------------------------------------------*")
    print(" {0:<15}{1:<15}{2:<15}".format('ITEM NO', 'ITEM', 'PRICE'))
    print(' ----------------------------------------------')
    for row in F:
        print(" {0:<15}{1:<15}{2:<15}".format(row[0], str(row[1]), row[2]))
    print(' ----------------------------------------------')


# 6. DISPLAY MENU (USER SELECTION)
def DisplayMenu():
    c.execute("Select ItNo,Item,Price from Products")
    F = c.fetchall()
    print("\n*--------------------------------------------*")
    print("*                    MENU                    *")
    print("*--------------------------------------------*")
    print(" {0:<15}{1:<15}{2:<15}".format('ITEM NO', 'ITEM', 'PRICE'))
    print(' ----------------------------------------------')
    for row in F:
        print(" {0:<15}{1:<15}{2:<15}".format(row[0], str(row[1]), row[2]))
    print(' ----------------------------------------------')
    main()


# 7. DISPLAY ALL ITEMS
def Display():
    c.execute("Select * from Products")
    F = c.fetchall()
    count = c.rowcount
    print("DETAILS OF ITEMS IN THE BAKERY")
    print("Total No. Of Items:", count)
    print()
    print("{0:<10}{1:<25}{2:<25}{3:<15}{4:<15}".format('PNO', 'CATEGORY', 'ITEM', 'QNTY', 'PRICE'))
    print("---------------------------------------------------------------------------------")
    for row in F:
        print("{0:<10}{1:<25}{2:<25}{3:<15}{4:<15}".format(row[0], str(row[1]), str(row[2]), row[3], row[4]))
        print("---------------------------------------------------------------------------------")
    main()


# 8. MAIN PROGRAM
def main():
    print("""
+-----------------------------------------------------------+
|                        BAKE 'N TAKE                       |
+-----------------------------------------------------------+
    """)
    print("1. VIEW MENU")
    print("2. ADD NEW ITEM")
    print("3. SEARCH AN ITEM")
    print("4. ORDER PLACEMENT")
    print("5. UPDATE AN ITEM")
    print("6. DISPLAY ALL ITEMS")
    print("7. EXIT\n")

    choice = int(input("Enter the Task Number: "))
    print('\n')

    if choice == 1:
        DisplayMenu()
    elif choice == 2:
        AddItem()
    elif choice == 3:
        Find()
    elif choice == 4:
        Order()
    elif choice == 5:
        UpdtIt()
    elif choice == 6:
        Display()
    elif choice == 7:
        print("\t\t Thank you for using this service!")
    else:
        print("!!Enter a valid choice!!")
        main()


# 9. LOGIN AUTHENTICATION
def pswd():
    print("TRI-TECH INTERNATIONAL DBMS\n")
    o = input("Enter Your Username: ")
    if o == "Manager":
        ps = input("Enter the Password: ")
        if ps == "sweets4life":
            main()
        else:
            print("...WRONG PASSWORD...\n")
            pswd()
    else:
        print("...WRONG USERNAME...\n")
        pswd()


# Execute Program
pswd()
