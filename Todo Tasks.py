import os.path
import time
import tkinter as tk
import tkinter.messagebox as tkmb
from os import path

#Check if the file exists and loop until the user exits.
while(True):
    #If the file exists returns true
    if path.exists("tasks.txt"):
        True
    #If the file does not exists creates a new file    
    else:
        myFile = open("tasks.txt", "w")
        myFile.write("To-Do Tasks:\n")           
        myFile.close()

    #Prints out different texts options for user selection
    print("\nChoose any options:")
    print("1: Add Task/s")
    print("2: View  Task/s")
    print("3: Edit  Task/s")
    print("4: Delete  Task/s")
    print("5: Set a Task Reminder")
    print("6: Exit Program")

    #Takes user's input for selecting specific choices from above
    option = int(input() + "\n")
    if option == 1:
        #Checks and reads the file and takes user's input and writes into the file
        if path.exists("tasks.txt"):    
            with open("tasks.txt", "r") as add:
                try:
                    lines = add.readline()
                    while lines:
                        #Allows to modify the file by adding user's input 'x' amount of times
                        with open("tasks.txt", "a") as index:
                            index.write(input() + "\n")
                            line = add.readline()

                #Allows user to exit the program with a message        
                except KeyboardInterrupt:
                    print('Exiting...')
                    time.sleep(0.5)
        #In case the file does not exists the next statement will create the file    
        else:
            myFile = open("tasks.txt", "w")
            myFile.write("To-Do Tasks:\n")
            myFile.close()

    #Prints out the data from the file
    elif option == 2:
        print("\n")
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            #Check if the second line at index 1 from the file is empty
            if len(lines) < 2 or not (lines[1].strip()):
                print("\nThere are no tasks to view!")
        
            else:
                for line in lines:
                    line = line.rstrip('\n')
                    print(line)

    elif option == 3:
        print("\n")
        with open("tasks.txt", "r") as f:
            try:
                lines = f.readlines()
                #Check if the second line at index 1 from the file is empty
                if len(lines) < 2 or not (lines[1].strip()):
                    print("\nThere are no tasks to edit!")
            
                else:
                    #Prints out the data from the file
                    for line in lines:
                        line = line.rstrip('\n')
                        print(line) 

                    #Asks user for input and edits the corresponding line of string (index)
                    print("\nChoose which task to edit by order of number starting from '1':")
                    edit = int(input())
                    
                    with open("tasks.txt", "w") as f:
                        lines[edit] = input() + "\n"
                        print("\n")
                        f.writelines(lines)
                        for line in lines:
                            line = line.rstrip('\n')
                            print(line)             
            except KeyboardInterrupt:
                    print('Exiting...')
                    time.sleep(0.5)
                        
    #Prints out the data from the file
    elif option == 4:
        myFile = open("tasks.txt")
        readLines = myFile.readlines()
        print("\n")
        
        #Check if the second line at index 1 from the file is empty
        if len(readLines) < 2 or not (readLines[1].strip()):
            print("\nThere are no tasks to delete!")

        #Only continue with the statement if the user's input is not 0
        #This is only to avoid deleting the first line inside the file
        else:
            try:    
                #Reads the data inside the file
                myFile = open("tasks.txt", "r")
                readLines = myFile.readlines()
                myFile.close()
                for line in readLines:
                    line = line.rstrip('\n')
                    print(line)

                #Asks the user for input and deletes the index of the submitted number
                print("\nChoose which task to remove by order of number starting with '1': ")
                delete = int(input() + "\n")  
                
                if delete != 0:
                    readLines.pop(delete)
                    with open("tasks.txt", "r") as f:
                        lines = f.readlines()
                    with open("tasks.txt", "w") as f:
                        print("\n")
                        for line in readLines:
                            if line.strip("\n") != readLines:
                                f.write(line)
                                line = line.rstrip('\n')
                                print(line)

                #If the user enters "0" the program prints and error message                
                else:
                    print ("Enter a number greater or equal to '1':")
            except KeyboardInterrupt:
                    print('Exiting...')
                    time.sleep(0.5)                  

    #Prints out the data from the file
    elif option == 5:
        with open("tasks.txt", "r") as f:
            lines = f.readlines()

            try:
                #Check if the second line at index 1 from the file is empty
                if len(lines) < 2 or not (lines[1].strip()):
                    print("\nThere are no tasks to set reminder!")

                else:
                    myFile = open("tasks.txt", "r")
                    readLines = myFile.readlines()
                    myFile.close()
                    print("\n")
                    for line in readLines:
                        line = line.rstrip('\n')
                        print(line)

                    #Asks the user for input to select the index of the submitted number
                    print("\nChoose which task to set a reminder by order of number starting with '1': ")
                    remind = int(input() + "\n")

                    #Only continue with the statement if the user's input is not 0
                    #This is only to avoid selecting the first line inside the file
                    if remind != 0:
                        print("\nFor how many minutes? ")
                        Rtime = float(input())
                        Rtime = Rtime * 60
                        with open("tasks.txt", "r") as f:

                            #This will loop through the file to find the user's input (index)
                            #It will print the line and asks the user to set a time/reminder
                            #A message pops up reminding about the task
                            for i, line in enumerate(f):
                                if i == remind:
                                    time.sleep(Rtime)
                                    line = line.rstrip('\n')
                                    master = tk.Tk()
                                    msg = tk.Label(master, text='Remember To: \n\n' + line)
                                    msg.grid(row=2, column=1, padx= 80,  pady=60)       
            except KeyboardInterrupt:
                    print('Exiting...')
                    time.sleep(0.5)                                            
        f.close()

    #Allows the user to exit the program   
    elif option == 6:
        quit()