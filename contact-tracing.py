# Write a python program for contact tracing:

# - Display a menu of options
#     Menu:
#          1 -> Add an item
#          2 -> Search
#          3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
#         - Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
#                    Use dictionary to store the info
#                    Use the full name as key
#                    The value is another dictionary of personal information
#         - Option 2: Search, ask full name then display the record
#         - Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# Example Output:

# Menu:
#  1 -> Add an item
#  2 -> Search
#  3 -> Exit (y/n)

# What do you want to do? (1-3): 1
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# Saved!
# What do you want to do? (1-3): 2
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890 What do you want to do? (1-3): 3
# Exit? n

d = {}
while True:
    menu_list = input('''

\033[36;3m
MENU
1. Add an Information
2. Search 
3. Exit (y/n) \033[0m
\033[33;1m\n\nWhat do you want to do? (1-3) \033[0m\n
\033[1m>>>\033[0m ''')


    #add information menu
    if menu_list == "1":
        print("ADD AN INFORMATION MENU")
        n = int(input("How many times do you want to enter data?: "))
        for i in range(n):
        
            dict_name = input("\nEnter your Full Name: ")

            d[dict_name] = {}
            print("\n\nTAGUIG CITY CONTACT TRACING")
            Name = input("Enter your Full Name (For Verification): ")
            Age = input("Enter Age: ")
            Address = input("Enter Address: ")
            PhoneNumber = (input("Enter Phone Number: "))
            Nationality = input("Enter Nationality: ")
            Birthday = input("Enter Birthday: ")
            d[dict_name]["Name"] = Name
            d[dict_name]["Age"] = Age
            d[dict_name]["Address"] = Address
            d[dict_name]["PhoneNumber"] = PhoneNumber
            d[dict_name]["Nationality"] = Nationality
            d[dict_name]["Birthday"] = Birthday

            print("----------------------------------------------------------------")
            print("\n\nYou Entered your FULL NAME: " + d[dict_name]["Name"])
            print("You Entered your AGE: " + d[dict_name]["Age"])
            print("You Entered your ADDRESS: " + d[dict_name]["Address"])
            print("You Entered your PHONE NUMBER: " + d[dict_name]["PhoneNumber"])
            print("You Entered your NATIONALITY: " + d[dict_name]["Nationality"])
            print("You Entered your BIRTHDAY: " + d[dict_name]["Birthday"])
            print("----------------------------------------------------------------")
            print("\n\nYour Data has been Saved!\n\n")
            print(d)
                

    #finder of information
    elif menu_list == "2":
            print("SEARCH FOR SAVED INFORMATION MENU")
            print("\n===========================================================")
            key_finder = input("Please enter your full name: ")
            print("Your Age is "+ d[key_finder]["Age"] + ".")
            print("Your Address is "+ d[key_finder]["Address"] + ".")
            print("Your Phone Number is "+ d[key_finder]["PhoneNumber"] + ".")
            print("Your Nationality is "+ d[key_finder]["Nationality"] + ".")
            print("Your Birthday is "+ d[key_finder]["Birthday"] + ".")
            print("===========================================================")

    #continue or not?
    elif menu_list == "3":
        cnt_again = input("Do you still want to continue? (y/n): ")
        if cnt_again == "y":
            continue
        elif cnt_again == "n":
            print("\n\n<<< Thank you for using the program! Have a great day! :) >>> ")
            break



            










