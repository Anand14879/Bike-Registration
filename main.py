import datetime
import functions

#calling functions below
functions.interface_message()
looping = True
functions.choices()
# creating a loop
while looping:
    the_choice = int(input("Enter the value of option: "))
    if the_choice == 1: #selling of bikes
        print("\n")
        print("Selling bikes.")
        print("++++++++++++++++++++++++++++++++++++++++++\n")
        #printing the bikes that are available   
        functions.display_bikes_details()
        total_price = 0
        morePurchase = "yes"
        empty_bikes_list = []
        check = True
        
        print("Enter the customer details below: ")
        customer_name =input("Enter customer name: ")
        location = input("Enter location of customer: ")
        #using try except
        while check == True:
            try:
                contact_information = int(input("Enter the contact details:"))
                check = False
            except:
                print("The phone number is invalid, please enter digits only!")
                check = True
        #if user chose to buy bikes the following code runs 
        while morePurchase.upper() == "YES":
            
            bikeID = functions.validate_bike_ID() #get bikeID
            quantity = functions.validate_quantity(bikeID) #get quantity
            functions.selling_bikes(bikeID, quantity) #update stock
            bikes = functions.returning_2D_list() #get 2D list of bikes
            bikeName = bikes[bikeID - 1][0] #get bikeName and so on
            companyName = bikes[bikeID - 1][1]
            bikeColor = bikes[bikeID - 1][2]
            bikePrice = bikes[bikeID - 1][4]
            today_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") #get today's date
            price = int(bikes[bikeID-1][4]) * quantity #calculate price of certain bikes
            total_price += price # sum up the total cost of the order
            empty_bikes_list.append([bikeName, companyName, bikeColor, bikePrice, quantity, price]) # append all the bike info into a list

            print("\n")
            print("Order another bike?")#checking if user wants to buy more bikes
            morePurchase = input("Enter yes if you wish to buy more bikes:")
       
        #if buying bikes done, generate bill and bring choices option
        functions.generate_bill("sale",customer_name, today_date,empty_bikes_list,location, contact_information,total_price)
        functions.bike_details_print("sale",customer_name, today_date,empty_bikes_list,location, contact_information,total_price)
        functions.choices()

        
    elif the_choice == 2:
        print("\n")
        print("Ordering bikes.")
        print("++++++++++++++++++++++++++++++++++++++++++\n")
        #print details of bikes available in bikes.txt
        functions.display_bikes_details()
        
        total_price = 0
        moreOrder = "yes"
        order_new = "no"
        empty_bikes_list = []
        #get shippers details        
        check = True
        print("Enter the shipping company's details below: ")
        shipping_name = input("Enter the shipping company name: ")
        location = input("Enter the location of the company: ")
        #use try except to get correct phone number
        while check == True:
            try:
                contact_information = int(input("Enter the contact details: "))
                check = False
            except:
                print("Please enter a valid phone number!")
                check = True
        #keep looping if moreOrder is yes
        while moreOrder.upper() == "YES":
            #print bikes in the bikes.txt file
            functions.display_bikes_details()
            #check if order is new
            order_new = input("Is the order new or not no/yes?")
            if order_new.upper() =="NO":
                bikeID = functions.validate_bike_ID() #get bikeID
                quantity = functions.validate_quantity_stocking(bikeID) #get quantity
                functions.ordering_bikes(bikeID, quantity) #make update of the stock
                bikes = functions.returning_2D_list() # get 2D list
                bikeName = bikes[bikeID - 1][0] #get the bike details
                companyName = bikes[bikeID - 1][1]
                bikeColor = bikes[bikeID - 1][2]
                bikePrice = bikes[bikeID - 1][4]
                bikeStock = bikes[bikeID - 1][3]
                today_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") #get today's date
                price = int(bikes[bikeID-1][4]) * quantity #calculate the price
                total_price += price #sum all the price of bikes
                #append the bike details and cost into a list
                empty_bikes_list.append([bikeName, companyName, bikeColor, bikePrice, quantity, price])
            else:
                #take input of bike details
                bikeName = input("Enter the name of the bike: ")
                companyName = input("Enter the bike company name: ")
                bikeColor = input("Enter color of the bike: ")
                bikePrice = input("Enter price of the bike: ")
                bikeStock = input("Enter the amount you'd like to stock: ")
                print("\n")
                
                bikes = functions.returning_2D_list() #get 2D list of bikes
                #append the new bike info into the 2D list
                bikes.append([bikeName, companyName, bikeColor, bikeStock, bikePrice])              
                #also update the stock
                functions.update_stock(bikes)
                #get today's date
                today_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                price = int(bikeStock)*int(bikePrice) #calculate the price of the bike added
                total_price += price #sum up the price of all bikes added
                #append bike information and cost into a list
                empty_bikes_list.append([bikeName, companyName, bikeColor, bikePrice, bikeStock, price])

            #Check if user wants to stock more bikes    
            print("Ordering another bike?")
            moreOrder = input("Enter yes if you wish to stock more bikes:")
        #print the invoice and generate a file with the invoice in it and print the choices        
        functions.generate_bill("order",shipping_name, today_date,empty_bikes_list,location, contact_information,total_price)
        functions.bike_details_print("order",shipping_name, today_date,empty_bikes_list,location, contact_information,total_price)
        functions.choices()

    #exit the system if choice is 3
    elif the_choice == 3:
        print("\n\n")
        looping = False
        functions.exit_message()
    else:
        #ivalid choice
        functions.input_invalid()
        functions.choices()

