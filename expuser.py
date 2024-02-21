import os
from expadmin import Admin
import datetime
from tabulate import tabulate


class User:
    dis = 10
    
    def __init__(self,sid="NA",sname="NA",type="NA",price="NA",size="NA",quant="NA"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price 
        self.size = size
        self.quant = quant

    def displayCloth(self):
        with open ("clothadmin.txt","r") as fp:
            data = []
            for c in fp:
                x = c[:-1].split(",")
                data.append(x)
              
            headers = ["Cloth ID","Cloth Nme","Type","Price","Size","Quantity"]

            table = tabulate(data,headers,tablefmt="grid")
            print(table)

    def searchCloth(self,snm):
        found = False
        with open("clothadmin.txt",'r') as fp:
            listsearch = []
            for c in fp:
                x = c[:-1].split(",")
                if snm == x[1]: 
                    listsearch.append(x)
                    found = True
                    
                else:
                    pass

            if found == False:
                print("Item Not Found")
            else:
                headers = ["Cloth ID","Cloth Nme","Type","Price","Size","Quantity"]
                table = tabulate(listsearch,headers,tablefmt="grid")
                print(table)

    def addToCart(self,id):
        found = False
        with open("clothadmin.txt",'r') as fp:
            for c in fp:
                x = c.split(",")
                x.pop()
                if str(id) == x[0]:
                    with open("mycart.txt","a") as fp:
                        z = ",".join(x)
                        fp.write(str(z)+"\n")
                        print("id",id,"succesfully added to cart")
                        found = True
                        break
                else:
                    pass
            if found == False:
                print("Please enter correct id")

    def displayMyCart(self):
        print("Welcom to Your Cart")
        with open("mycart.txt","r") as fp:
            data = []
            for c in fp:
                x = c[:-1].split(",")
                data.append(x)
              
            headers = ["Cloth ID","Cloth Nme","Type","Price","Size","Quantity"]

            table = tabulate(data,headers,tablefmt="grid")
            print(table)

    def buyItem(self,id):
        
            found = False
            #container
            list = []
            sum = 1
            with open("clothadmin.txt",'r') as fp:
                for i in fp:
                    #convert to list
                    x = i.split(",")
                    
                    if str(id) == x[0]:
                        
                        q = int(input("Enter quantity : "))
                        print("confirm order id y/n =",id)
                        confirmation = input("Enter your confirmation response y/n : ")
                        
                        #handle quantity 
                        if q <= int(x[5]):
                            if (confirmation.lower() == "y"):
                                
                                print("Your total amount is ",float(x[3])*q)
                                
                                discount = input("Apply discount code on your coupon to get 10 % discount : ")
                                if (discount == "dis10"):
                                    abc = (float(x[3])*q)-(float(x[3])*q *User.dis/100)
                                    print("Please pay amount",abc)
                                else:
                                    abc = float(x[3])*q
                                    print("Please pay amount",abc)

                                amount = float(input("Please pay amount : "))
                                if amount == abc:
                                    print("Purchase successfull")

                                    #save sell records for admin
                                    with open("selladmin.txt","a") as fp:
                                        #for billing purpose
                                        with open("bill.txt","w") as bil:
                                            #store current date and write in files
                                            d = x.copy()
                                            d.pop()
                                            f = ",".join(d)
                                            
                                            dat = datetime.datetime.now()
                                            fp.write(f+","+str(amount)+","+str(q)+","+str(dat)+"\n")
                                            bil.write(f+","+str(amount)+","+str(q)+","+str(dat)+"\n")
                                    
                                    #c object is in main file which have if constraint
                                
                                    c = Admin()  
                                    #print bill 
                                    c.printBill()

                                        
                                    u = User()
                                    u.removeItem(id)
                                    found = True
                                    a = x[5]
                                    c = int(a)-q
                                    a = str(c)+"\n"
                                    x[5] = a

                                    

                                else:
                                    print("insuffisient amount")
                                    sum = 0
                            elif (confirmation.lower() == "n"):
                                print("You denied confirmation want to buy again")
                            else:
                                print("Invalid choice")
                                sum = 0
                        else:
                            print("Only ",int(x[5]),"Left in stocks")
                            sum = 0
                            break
                        
                        #join the x which is in list form
                        j = ",".join(x)
                        list.append(j)
                    else:
                        list.append(i)
                
                z="".join(list)
                
                
                if found == True:
                    #fill container wise
                    with open("clothadmin.txt","w") as fp:
                        for c in z:
                            fp.write(str(c))
                elif found ==  False and sum ==0:
                    pass
                elif found == False and sum == 1:
                    print("id not Found")
        
        

    def removeItem(self,id):
        with open("mycart.txt","r") as fp:
            found = False
            list = []
            for i in fp:
                x = i.split(",")
                if str(id) == x[0]:
                    found = True
                    pass
                else:
                    list.append(i)
            
            z = "".join(list)
            if found == True:
                 with open("mycart.txt","w") as fp:
                    for i in z:
                        fp.write(str(i))
                    print("Item with id",id,"removed successfully from your cart")
            else:
                print("Id not present")

    def __str__(self):
        return str(self.sid)+","+self.sname+","+self.type+","+str(self.price)+","+self.size+","+str(self.quant)+"\n"


if __name__ =="__main__":
    b = User()