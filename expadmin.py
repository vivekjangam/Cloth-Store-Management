
from tabulate import tabulate


class Admin:
    def addcloth(self,c):
        with open("clothadmin.txt","a") as fp:
            fp.seek(0,0)
            fp.write(str(c))
        
    
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


    def delteItem(self,id):
        with open("clothadmin.txt","r") as fp:
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
                 with open("clothadmin.txt","w") as fp:
                    for i in z:
                        fp.write(str(i))
                    print("Item with id",id,"removed successfully")
            else:
                print("id not found")

    def updateItem(self,id):
        with open("clothadmin.txt","r") as fp:
            found = False
            list = []
            for i in fp:
                x = i.split(",")
                if str(id) == x[0]:
                    found = True 
                    print("Do you want to update Name (y/n)")
                    choice = input("Enter your Choice (y/n)")
                    if choice == "y":
                        name = input("Enter New name (sweatshirt,hoodie,t-shirt,planeshirt) : ")
                        x[1] = name
                    
                    print("Do you want to update size (y/n)")
                    choice = input("Enter your Choice (y/n)")
                    if choice == "y":
                        size = input("Enter New Size (s,m,l,xl,xll) : ")
                        x[4] = size
                    
                    print("Do you want to update Price (y/n)")
                    choice = input("Enter your Choice (y/n)")
                    if choice == "y":
                        price = float(input("Enter New Price : "))
                        x[3] = str(price)
                    
                    print("Do you want to update quantity (y/n) : ")
                    choice = input("Enter your Choice (y/n)")
                    if choice == "y":
                        quant = int(input('Enter quantity : '))
                        x[5] = str(quant)

                    j = ",".join(x)
                    list.append(j)
                else:
                    list.append(i)
            
            z="".join(list)    
            if found == True:
                with open("clothadmin.txt","w") as fp:
                    for c in z:
                        fp.write(str(c))
            else:
                print("id not Found")

    def allBill(self):
        with open("selladmin.txt","r+") as fp:
            data = []
            for c in fp:
                x = c[:-1].split(",")
                data.append(x)
              
            headers = ["Cloth ID","Cloth Nme","Type","Price","Size","Amount Paid","Quantity","Date And Time"]

            table = tabulate(data,headers,tablefmt="grid")
            print(table)
    
    def printBill(self):
        with open("bill.txt","r") as fp:
            data = []
            for c in fp:
                x = c[:-1].split(",")
                data.append(x)
              
            headers = ["Cloth ID","Cloth Nme","Type","Price","Size","Amount Paid","Quantity","Date And Time"]

            table = tabulate(data,headers,tablefmt="grid")
            print(table)
            
    def searchClothbyID(self, id):
        found = False
        with open("clothadmin.txt",'r') as fp:
            data = []
            for c in fp:
                x = c.split(",")
                if str(id) == x[0]:
                    data.append(x)
                    found = True
                    return 0;
                else:
                    pass
            
            if found == False:
                print("Item Not Found")
            else:
                headers = ["Cloth ID","Cloth Nme","Type","Price","Size","Quantity"]
                table = tabulate(data,headers,tablefmt="grid")
                print(table)



        

    

            
        

        
