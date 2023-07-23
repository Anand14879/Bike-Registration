import datetime

#welcome message function
def interface_message():
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("    Welcome to Bike Management System   ")
    print("++++++++++++++++++++++++++++++++++++++++++")

#printing choices for the user to make
def choices():
    print("1.Sell Bikes")
    print("2.Order Bikes")
    print("3.Exit")

#printing invalid option prompt
def input_invalid():
    print("INVALID INPUT. Please enter a valid option number.")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

#Exit message shown
def exit_message():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("   Thank you for using Bike Management System   ")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")

#printing the bikes available in the bikes.txt file
def display_bikes_details():
    print("-------------------------------------------------------------------------------")
    print("Bike ID        Bike-Name        Company        Color    Stock   Price($)")
    print("-------------------------------------------------------------------------------")
    opened_file = open("bikes.txt", "r") #opening bikes.txt file to read
    bike_ID = 1

    for line in opened_file: #going through each line of the text file
        print(" ", bike_ID, "\t\t" + line.replace(",", "\t")) # printing each row of data with bike ID at the start
        bike_ID += 1 # increment bike_ID by one
    print("--------------------------------------------------------------------------------")
    opened_file.close() #closing file

#getting a 2D list by storing details of bikes in it
def returning_2D_list():
    opened_file = open("bikes.txt")
    listNew = []
    for line in opened_file:
        line = line.replace("\n", "")  # for replacing \n with ""
        line = line.split(",")#convert string into list by spliting with given parameter
        listNew.append(line) #adding the string into the list
    opened_file.close()
    return listNew

#using try except when getting bike ID input from user
def try_bike_ID():
    check = True
    while check == True:
        try:
            bike_ID = int(input("Enter the value of bike ID: "))
            check = False
        except:
            #prints invalid when anything other than number is pressed
            print("Invalid entry. Please enter a number for ID of bike: ")
            check = True
    return bike_ID

#checks if the bike ID is valid or not
def validate_bike_ID():
    bike_ID = try_bike_ID()
    while bike_ID <= 0 or bike_ID > len(returning_2D_list()):
        print("Please enter the valid ID!!!")
        print(display_bikes_details())
        bike_ID = try_bike_ID()
    return bike_ID
#used try except to see if quantity is invalid
def tot_quantity():
    check = True
    while check == True:
        try:
            new_total_quantity = int(input("Please enter the quantity: "))
            check = False
        except:
            print("Invalid entry. Please enter an integer value!")
            check = True
    return new_total_quantity

#checking validity of quantity when bike is being sold
def validate_quantity(bike_ID):
    in_stock = returning_2D_list()[bike_ID - 1][3]
    total_quantity = tot_quantity()
    while total_quantity <= 0 or total_quantity > int(in_stock) :
        print("Out of bounds. Please enter the valid quantity you want to purchase")
        print(display_bikes_details())
        total_quantity = tot_quantity()
    
    return total_quantity

#checking validity of quantity when bike is being added
def validate_quantity_stocking(bike_ID):
    total_quantity = tot_quantity()
    while total_quantity <= 0:
        print("Out of bounds. Please enter valid quantity")
        total_quantity = tot_quantity()
    return total_quantity

#updates the stock when bike is sold or added
def update_stock(listNew):
    file = open("bikes.txt", "w")  
    for list_1D in listNew:
        file.write((str(list_1D[0])).strip() + ", " + (str(list_1D[1])).strip() + ", " + (str(list_1D[2])).strip() + ", " + (str(list_1D[3])).strip() + ", " + (str(list_1D[4])).strip())
        file.write("\n")
    file.close()
    display_bikes_details()
    
    
    
#to make update on stock when bike is sold
def selling_bikes(bikeID, quantity):
    bikes = returning_2D_list()
    bikes[bikeID - 1][3] = int(bikes[bikeID - 1][3]) - quantity
    update_stock(bikes)
    print("\n\n")
    
#to make the update on stock when bike is added
def ordering_bikes(bikeID,quantity):
    bikes = returning_2D_list()
    bikes[bikeID - 1][3] = int(bikes[bikeID - 1][3]) + quantity
    update_stock(bikes)
    print("\n\n")
    


# function to get the current time
def get_datetime_integer():
    import datetime
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    microsecond = str(datetime.datetime.now().microsecond)
    return microsecond+second+minute+hour+day+month+year


#checking transaction  and writing data accordingly
def generate_bill(typeOfTransaction,customerOrShipping_name, todaysDate, empty_bikes_list,location,contact_information,total_price) :
    filename = customerOrShipping_name + "_" + get_datetime_integer()
    opened_file = open(filename + ".txt", "w")
    opened_file.write("---------------------------------------------------------------------------------------------------------------------------------------\n")

    if typeOfTransaction=="sale":
        opened_file.write("________________________Sale Details________________________________________________________________________________________________\n")
        opened_file.write("------------------------------------------------------------------------------------------------------------------------------------\n")
        opened_file.write("Name of Customer:"+str(customerOrShipping_name) +"\n" )
        opened_file.write("Location of customer: "+ str(location)+"\n")
        opened_file.write("The contact information of the customer: " +str(contact_information)+"\n")
        opened_file.write("------------------------------------------------------------------------------------------------------------------------------------\n")

        
    elif typeOfTransaction=="order":
        opened_file.write("_______________________Order Details______________________________ _________________________________________________________________\n")
        opened_file.write("------------------------------------------------------------------------------------------------------------------------------------\n")
        opened_file.write("Name of Shipping Company:"+str(customerOrShipping_name) +"\n" )
        opened_file.write("Location of shipping company: "+ str(location)+"\n")
        opened_file.write("The contact information of the shipping company: " +str(contact_information)+"\n")
        opened_file.write("------------------------------------------------------------------------------------------------------------------------------------\n")
            
    opened_file.write("Date and time: " + str(todaysDate) + "\n")
    opened_file.write("\n")
    opened_file.write(f'{"Bike Name":<25}{"Company":<30}{"Color":<15}{"Unit Price($)":<15}{"Quantity":<30}{"Total Price($)":<20}\n')
    

    for bike_data in empty_bikes_list:
        opened_file.write(f'{bike_data[0]:<25}{bike_data[1]:<30}{bike_data[2]:<15}{bike_data[3]:<15}{bike_data[4]:<30}{bike_data[5]:<20}\n')
        
        opened_file.write("\n")
    opened_file.write("----------------------------------------------------------------------------------------------------------------------------------------\n")
    opened_file.write("Total Price of the order: ($) "+str(total_price) +"\n")
    opened_file.close()
    
#once determining the transaction, printing accordingly
def bike_details_print(typeOfTransaction,customerOrShipping_name, todaysDate, empty_bikes_list,location,contact_information,total_price):
    print("----------------------------------------------------------------------------------------------------------------------------------------------------\n")
    #Checking if the transation is sale or order then printing accordingly
    if typeOfTransaction=="sale":
        print("________________________Sale Details____________________________________________________________________________________________________________\n")
        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print("Name of Customer:"+str(customerOrShipping_name) +"\n" )
        print("The location of the customer: "+str(location)+"\n")
        print("The contact information of the customer: "+str(contact_information)+ "\n")
        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")

        
    elif typeOfTransaction=="order":
        print("_______________________Order Details____________________________________________________________________________________________________________\n")
        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
        print("Name of Shipping Company:"+str(customerOrShipping_name) +"\n" )
        print("Location of shipping company: "+ str(location)+"\n")
        print("The contact information of the shipping company: " +str(contact_information)+"\n")
        print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
            
    print("Date and time: " + str(todaysDate) + "\n")
    print("\n")
    
    print(f'{"Bike Name":<25}{"Company":<30}{"Color":<15}{"Unit Price($)":<15}{"Quantity":<30}{"Total Price($)":<20}\n')

    for bike_data in empty_bikes_list:
        print(f'{bike_data[0]:<25}{bike_data[1]:<30}{bike_data[2]:<15}{bike_data[3]:<15}{bike_data[4]:<30}{bike_data[5]:<20}\n')
        print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("Total Price of the order:($) "+str(total_price) +"\n" )
    

    
