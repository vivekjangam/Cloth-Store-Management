from expuser import User
from expadmin import Admin

if (__name__=="__main__"):
    c = Admin()
    u = User()
    print('''
              1.Admin
              2.User
              ''')
    try:
        choice = int(input("Enter your choice : "))
        if choice == 1:
            print("Enter user id and Password correctly")
            adminid = int(input("Enter User id a: "))
            passw = input("Enter your Password : ")
            x = 0
        
            if adminid == 13579 and passw == "addminj":
                print("Login succesful")

                n = 0
                while n!=10:
                        print('''
                        1.add cloth variety
                        2.display
                        30.search by id
                        3.search by name
                        4.delete item
                        5.Update by id
                        6.display sell records
                        10.Exit
                        ''')
                    
                        ch = int(input("Enter your choice  : "))

                #add cloth variety
                        if (ch==1):
                            sid = int(input("Enter id : "))
                            zad = c.searchClothbyID(sid)
                            if zad == 0:
                                print("Id already present")
                            else :
                                
                                #exception @2
                                try:
                                    snm = input("Enter Name (sweatshirt,hoodie,t-shirt,planeshirt): ")
                                    if snm not in ("sweatshirt","hoodie","t-shirt","planeshirt"):
                                        raise SyntaxError
                                    type = input("Enter type of cloth (formal/informal): ")
                                    if type not in ("formal","informal"):
                                        raise SyntaxError
                                    price = float(input("Enter price of cloth : "))
                                    size = input('Enter size of wear ("s","m","l","xl","xxl"): ')
                                    if size not in ("s","m","l","xl","xxl"):
                                        raise SyntaxError
                                except SyntaxError:
                                    print("Check for typos, spelling,missing parenthessis,colons or incorect input")
                                    break
                                quant = int(input("Enter quantity of products : "))

                                e = User(sid,snm,type,price,size,quant)
                                c.addcloth(e)
                                print(f"Item with id {sid} succesfully addet to store")

                            
                              
                            
                                

                #display
                        elif (ch==2):
                            c.displayCloth()

                #search by id
                        elif (ch==30):
                            id = int(input("Enter id to search : "))
                            c.searchClothbyID(id)   
                
                #search by name
                        elif (ch==3):
                            snm = input("Enter Name of cloth to search  : ")
                            c.searchCloth(snm)

                #delete item
                        elif (ch==4):
                            id = int(input("enter id to delete item from store : "))
                            c.delteItem(id)
                        
                #Update by id
                        elif (ch==5):
                            id = int(input("Enter id to update item : "))
                            c.updateItem(id)
                        #we can update price of catogry all at once like catagory hoodie and size is s then update
                
                #display sell records
                        elif (ch==6):
                            c.allBill()

                #Exit
                        elif ch == 10:
                            print("Program Ended")
                            break
                            
                        else:
                            print("Invalid choice")
            else:
                    print("Wrong Credentials try again")


        elif choice == 2:
            print("Enter user id and Password correctly : ")
            userid = int(input("Enter User id a: "))
            passw = input("Enter your Password : ")
            x = 0
        
            if userid == 123 and passw == "userg":
                print("Login succesful")

                n = 0
                while n!=10:
                        print('''
                        2.display
                        3.search
                        4.add to cart by display
                        5.add to cart by search
                        6.display myCart
                        7.buy item
                        8.buy item from cart
                        9.remove from cart
                        10.Exit
                        ''')
                    
                        ch = int(input("Enter your choice  : "))

                #display
                        if ch == 2:
                            u.displayCloth()    

                #search           
                        elif ch == 3:
                            snm = input("Enter Name of cloth to search  : ")
                            u.searchCloth(snm)

                #add to cart by display       
                        elif ch == 4:
                            u.displayCloth()
                            id = int(input("Enter id to add item to cart : "))
                            u.addToCart(id)

                #add to cart by search
                        elif ch == 5:
                            snm = input("Enter Name of cloth to search  : ")
                            u.searchCloth(snm)
                            id = int(input("Enter id to add item to cart : "))
                            u.addToCart(id)

                #display myCart
                        elif ch == 6:
                            u.displayMyCart()

                #buy item
                        elif ch == 7:
                            u.displayCloth()
                            id = int(input("Enter id to buy item : "))
                            u.buyItem(id)

                #buy item from cart         
                        elif (ch==8):
                            u.displayMyCart()
                            id = int(input("Enter id to buy item : "))
                            u.buyItem(id)
                            

                #remove from cart
                        elif (ch==9):
                            u.displayMyCart()
                            id = int(input("Enter id to remove item : "))
                            u.removeItem(id)

                #Exit
                        elif ch == 10:
                            print("Program Ended")
                            break
            
            else:
                print("Wrong Credentials Try again")

        else:
            print("Invalid choice")  

    except ValueError:
        print("Please Enter Number")
    
    except FileNotFoundError:
        print("The file you requested not found. Kindly try again. Please check name, spelling,extention.")
    
    except TypeError:
        print("Operation applied on inapropriate type.")
    
    except NameError:
        print("local variable not found")
    
    except ModuleNotFoundError:
        print('Specified module not found')
    
    except:
        print("something went wrong")
        
                            
                           
                       

                
  
            