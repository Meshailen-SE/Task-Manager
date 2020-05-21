#Task 20
#Compulsory Task 1
#Capstone project 3
#Meshailen Chetty
#start: 26/02/2020
#end: 20/03/2020

text_file = open("user.txt","r+")
#variables that will print objects for a user friendly matter.
spacer = ("=" * 50)
spacer1 = ("-" * 50)
#initialised my boolean variables to true in the beginning of the program
login_success = True
repeat = True
#asked the user to input their name and password
name = input("What is your username?").lower()
password = input("What is your password?").lower()

#created a while loop and initialised it to True
while login_success:
    #used a for loop that will read each line in the textfile    
    for line in text_file:
        #i then split the name and password with a comma in the textfile
        valid_user = line.split(", ")
        #created a new variable that stores the first index
        other_name = valid_user[0]
        #created a new variable that stores the second index and replaces a new line with a space
        other_password = valid_user[1].replace("\n","")
        #created an if statement if the variables are equal to the text to the textfile then the boolean is set to false and i stopped the loop with a break function
        if name == other_name and password == other_password:
            login_success = False
            break
#created another if statement with a condition if its not equal to the textfile then it loops through by asking the user to input their name and password again 
#i then closed the textfile and re-opened the textfile
#and set the boolean variable to true
    if name != other_name and password != other_password:
        print("Your login process is incorrect please try again! ")
        name = input("What is your username?")
        password = input("What is your password?")
        text_file.close()
        text_file = open("user.txt","r+")
        login_success = True

#created a new boolean variable and initialised it to true
repeat_admin = True
#created a counting variable and made it equal to 0
i = 0  
#created a while loop and made it equal to True
while True:
    

    #using an if statement that has conditions
    if name == "admin" and password == "adm1n":
        if repeat_admin:
            print(spacer)
        
        #asked the user to select the following using an input
        options = input(f"\nPlease select one of the following options:\ns  - Statistics \nr  - Register user \na  - Add task \nva - View all tasks \nvm - View my tasks \ne  - Exit \n {spacer}\n").lower()

        #used an if statement if a user entered a certain option
        #opened a textfile and read it and split with a new line
        if options == "s":
            stats = open("tasks.txt","r")
            stats1 = stats.read().split("\n")
            #created my counting variable and initialised it to 0
            co = 0
            #used a for loop to read the split textfile and to work with the range from the length of the textfile using the len() function
            for i in range(len(stats1)):
                co += 1   
            #printed the total amount of tasks
            #closed the textfile
            print(f"The total number of tasks entered are {co}")   
            stats.close()

            #done the same as above
            stats_users = open("user.txt","r")
            stats_us = stats_users.read().split("\n")
            user = 0
            for i in range(len(stats_us)):
                user += 1   
            print(f"The total number of users entered are {user}")   
            stats_users.close()

            #opened the textfile
            #asked the user if they wanted to continue or exit the program and made their answer into lowercase letters
            text_file4 = open("user.txt","a")
            options_dash_ad = input(f"{spacer1}\nIf you would to :\nc - continue\nor\ne - exit\n{spacer}\n").lower()

            #if the user chose exit then the program with stop by using the break function
            if options_dash_ad == "e":
                break

            #if they chose to continue then the boolean value is equal to False to display the menu
            #closed the textfile
            if options_dash_ad == "c":
                repeat_admin == False
                text_file4.close() 


        if options == "r":
            #opened a textfile
            textfile = open("user.txt","r")
            #asked the user to input their name they are going to register
            reg_name = input("What is the name of the user? ")

            #created a boolean and initialised it to true
            correct = True
            #used a for loop to read the textfile and split it
            for line in textfile:
                line1 = line.split(", ")
                
            #created a while loop
            while correct:

                #if the name is already in the textfile then it should print a statement and with the boolean it will return it to the main menu
                #used a break function so it doesnt loop infintely
                if reg_name == line1[0]:
                    print("The name you have entered already exists in our database.")
                    correct = True
                    break

                #used an elif statement for a different condition
                #if the passwords do not match then the user can enter it again
                #set the boolean to false
                elif reg_name != line1[0]:
                    reg_password = input("Please enter a password. ")
                    confirm_reg_password = input(f"Please confirm your password.")
                    correct = False

                    # if the passwords do not match then the following will be executed
                    #new inputs are placed 
                    if reg_password != confirm_reg_password:
                        print()
                        print("Your name and password do not match please try again.")
                        reg_name = input("What is the name of the user? ")
                        reg_password = input("Please enter a password. ")
                        confirm_reg_password = input(f"Please confirm {reg_name} password.")

                        #once the passwords match then a print statement states it has been added to the textfiles
                        #then a textfile will be opened and by using the writelines function it is able to write all the information to the textfile
                        if reg_password == confirm_reg_password:
                            print(f"\nThank you {reg_name} has been added to our database. ")
                            textfile = open("user.txt","a")
                            textfile.writelines(f"\n{reg_name}, {confirm_reg_password}")
                    
                    #once the passwords match then a print statement states it has been added to the textfiles
                    #then a textfile will be opened and by using the writelines function it is able to write all the information to the textfile
                    elif reg_password == confirm_reg_password:
                        print(f"\nThank you {reg_name} has been added to our database. ")
                        textfile = open("user.txt","a")
                        textfile.writelines(f"\n{reg_name}, {confirm_reg_password}")
                        text_file4 = open("user.txt","a")
                        options_dash_ad = input(f"\nIf you would to :\nc - continue\nor\ne - exit\n{spacer}\n").lower()
                        if options_dash_ad == "e":
                            break
                        if options_dash_ad == "c":
                            repeat_admin == False
                        text_file4.close()        

                #if statement for a different option
                #asked the user a series of questions usinf inputs that store in variables that will be used for descriptions of tasks
        if options == "a":
            add_name = input("To whom is the task being assigned to? ")
            task = input(f"What is the name of the task given to {add_name}? ")
            task_descrip = input("What is the description of the task? ")
            date_ass = input(f"At which date was the task assigned to {add_name}? ")
            due_date = input(f"When is the due date of the task? ")
            completion = input("Has the task been completed? (Yes or No) ").lower().capitalize()

            #opened a textfile
            #using the write function i am able to update all the information from the inputs to the textfile 
            #closed the textfile
            text_file21 = open("tasks.txt","a")
            text_file21.writelines(f"\n{add_name}, {task}, {task_descrip}, {date_ass}, {due_date}, {completion}")
            print("Thank you the task has been added to the system.")
            text_file21.close()

            #continue or exit menu
            options_dash_ad = input(f"\nWould you like to :\nc - continue\nor\ne - exit\n{spacer}\n").lower()
            text_file21 = open("tasks.txt","a")
            if options_dash_ad == "c":
                repeat_admin = False
            if options_dash_ad == "e":
                break
            text_file21.close()
            
            
        if options == "va":
            #opened a textfile
            #read a textfile and split it with a new line
            text_file2 = open("tasks.txt","r+")
            text_file3 = text_file2.read().split("\n")
            x = 0
            #used a for loop that has a range from 0 to the len of the textfile
            #used indexing of and created a counter that will add 1 to each of them which makes it possible to view all the tasks
            for x in range(len(text_file3)):
                admin_task = text_file3[x].split(",")
                #used a print statement that will print all the tasks in a user friendly view
                print(f"Task\t\t: {admin_task[0]} \nAssigned to\t:{admin_task[1]}\nTask description:{admin_task[2]}\nDate assigned\t:{admin_task[3]}\nDue date\t:{admin_task[4]}\nTask Completion\t:{admin_task[5]}\n\n{spacer1}")
                x += 1
            #closed a textfile
            text_file2.close()
            
            #continue or exit menu
            options2_dash1 = input(f"Would you like to :\nc - continue\nor\ne - exit\n{spacer}\n").lower()
            text_file4 = open("tasks.txt","r+")
            if options2_dash1 == "e":
                break
            if options2_dash1 == "c":
                repeat_admin = False
                text_file2.close()

        #if statement for a different option view mine
        if options == "vm":
            #opened a textfile
            #read the textfile and split it with a new line
            view_task = open("tasks.txt","r")
            view_task2 = view_task.read().split("\n")
            #created a counting variable and intialised it to 0
            z = 0

            #used a for loop that has a range from 0 to the length of the textfile
            #used a condition if the name is equal the tasks textfile then it will print all the tasks that are assigned with the person that is logged in

            for z in range(len(view_task2)):
                task1 = view_task2[z].split(",")
                if name == task1[0]:
                    print(f"Task:\t{task1[0]} \nAssigned to :\t{task1[1]}\nTask description:\t{task1[2]}\nDate assigned:\t{task1[3]}\nDue date:\t{task1[4]}\nTask Complete?\t{task1[5]}\n{spacer1}")
                    #incremented my counting variable by 1
                    z += 1
            #closed the textfile
            view_task.close()

            #continue or exit menu
            options2_dash1 = input(f"If you would to :\nc - continue\nor\ne - exit\n{spacer}\n").lower()
            text_file22 = open("tasks.txt","r+")
            if options2_dash1 == "e":
                break
            if options2_dash1 == "c":
                repeat = False
                text_file22.close()

        #exit option 
        #usinf the break function i am able to exit the loop
        if options == "e":
            break

        #used an else statement if the user entered a input that doesnt occur to the if statements
        #set the boolean to True so that it displays a new menu    
        else: 
            login_success = True


    #using an elif statemnet i wasable to make a login for the other members
    #using the and function i able to create more than one condition
    elif name == other_name and password == other_password:
        #opening statement of the program for the other members
        if repeat:
            print("Welcome User.\n")
            print("Your password is correct.")
        options2 = input(f"{spacer}\nPlease select one of the following options:\na  - add task \nva - view all tasks \nvm - view my tasks \ne  - exit \n {spacer}\n").lower()

        if options2 == "a":
            print(spacer1)
            print("Sorry only admin is able to add tasks. ")
            print(spacer1)
            options2_dash1 = input("Please select one of the following options :\nc - continue\ne - exit\n").lower()
            print(spacer)
            if options2_dash1 == "e":
                break
            if options2_dash1 == "c":
                repeat = False
                text_file.close()
            
                
        if options2 == "va":

            #opened a textfile
            #read a textfile and split it with a new line
            text_file2 = open("tasks.txt","r+")
            text_file3 = text_file2.read().split("\n")
            x = 0
            #used a for loop that has a range from 0 to the len of the textfile
            #used indexing of and created a counter that will add 1 to each of them which makes it possible to view all the tasks
            for x in range(len(text_file3)):
                admin_task = text_file3[x].split(",")
                #used a print statement that will print all the tasks in a user friendly view
                print(f"Task\t\t: {admin_task[0]} \nAssigned to\t:{admin_task[1]}\nTask description:{admin_task[2]}\nDate assigned\t:{admin_task[3]}\nDue date\t:{admin_task[4]}\nTask Completion\t:{admin_task[5]}\n\n{spacer1}")
                x += 1
            #closed a textfile
            text_file2.close()

            #continue or exit menu 
            options2_dash1 = input(f"If you would to :\nc - continue\nor\ne - exit\n{spacer}\n").lower()
            text_file2 = open("tasks.txt","r+")
            if options2_dash1 == "e":
                break
            if options2_dash1 == "c":
                repeat = False
                text_file2.close()

        if options2 == "vm":
            #opened a textfile
            #read the textfile and split it with anew line and stored it in a new varable
            text_file22 = open("tasks.txt","r+")
            text_file33 = text_file22.read().split("\n")
            #created my counting varibale and initialised it to 0
            x = 0
            
            #using a for loop i am able to read the textfile and split it
            #used a for loop that has a range from 0 to the length of the textfile
            #used a condition if the name is equal the tasks textfile then it will print all the tasks that are assigned with the person that is logged in
            for x in range(len(text_file33)):
                task = text_file33[x].split(",")
                if name == task[0]:
                    print(f"Task:\t{task[0]} \nAssigned to :\t{task[1]}\nTask description:\t{task[2]}\nDate assigned:\t{task[3]}\nDue date:\t{task[4]}\nTask Complete?\t{task[5]}\n{spacer1}")
                    x += 1#incremented my counting variable

                #using an else statement if the user does not have any tasks then a print statement will be printed out    
                else:
                    print("You currently do not have any available tasks at hand.")
                    break
            #closed textfile
            text_file22.close()

            #continue or exit menu
            options2_dash1 = input(f"If you would to :\nc - continue\nor\ne - exit\n{spacer}\n").lower()
            text_file22 = open("tasks.txt","r+")
            if options2_dash1 == "e":
                break
            if options2_dash1 == "c":
                repeat = False
                text_file22.close()
        #exit option using break to terminate the program
        if options2 == "e":
            break



#The end :)