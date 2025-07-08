import time
#names of base variables initialized to begin with
passwordInput = 0
passwordBase = "1234"
name = ""
logEntry = 0
logReading = ""
passwordAttempts = 3
passwordBaseCorrect = False
fileDict = {}


def passwordDemand():
    '''This function handles the password inputs and reacts accordingly'''
    userInput = (input("Enter Password: "))
    global passwordAttempts
    while userInput != passwordBase:
        passwordAttempts = passwordAttempts-1
        if passwordAttempts == 0:
            print("System Locked Down || Too Many Failed Attempts")
            return False
        print("Error: Wrong Password ", passwordAttempts, " Remaining")
        userInput = (input("Enter Password: "))
    print("System Password Entered Correctly: Releasing Logs Now")
    return True


def readLogCollection():
    '''This function reads the file World_Logs.txt and gathers the information from it to place into a dictionary'''
    file = open("World_Logs.txt", "r")
    lineCount = sum(1 for _ in file)
    file.seek(0)
    fileInfo = []
    global fileDict
    for i in range(0, lineCount):
        fileInfo.append(file.readline().strip())
    for i in range (0, lineCount, 2):
        key = fileInfo[i]
        value = fileInfo[i+1]
        fileDict[key] = value
    file.close()

def availableLogs():
    '''This function takes the information gathered from the file to determine what logs are available and print them
    This is done by converting the keys of the dictionary into their own list'''
    global fileDict
    logs = list(fileDict.keys())
    print("Logs Available:")
    for i in range(len(logs)):
        print(f"Log {logs[i]}")

def printOldMachineText(text):
    '''Prints the text for the old machine, slowed for dramatic effect'''
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print("")

def oldPasswordDemand():
    '''This function handles the password inputs and reacts accordingly. 
    Same code as previous version but updated for the old machine'''
    userInput = (input(">Password: "))
    oldPasswordAttempts = 3
    while userInput != "secret":
        oldPasswordAttempts = oldPasswordAttempts-1
        if oldPasswordAttempts == 0:
            printOldMachineText(">System Locked")
            return False
        print("Error: Wrong Password ", oldPasswordAttempts, " Remaining")
        userInput = (input(">Password: "))
    print(">Accessing ")
    return True

def oldMachine():
    '''Similar to main function, runs all the code relating to the old machine'''
    result = oldPasswordDemand()
    if not (result):
        return
    print('I Can No Longer Help Beyond This Point. Goodbye For Now')
    time.sleep(0.5)
    printOldMachineText(">What Information Do You Seek: ")
    LogChoice = input()
    #while LogChoice != -1:
        #This will need to wait until the old world machine logs are made
    return
    

def main(): #You don't need a main function but I'm so used to c++ that I decided to do it this way
    '''Function to run the main part of the code and implement the functions'''
    past_name = False
    if not passwordDemand():
        return
    readLogCollection()
    global name 
    name = input("Hello! What Is Your Name? : ")
    file = open("PastNames.txt", "r")
    file_name = file.readline()
    while (file_name != ""):
        if file_name == name:
            past_name = True
        file_name = file.readline()
    if (past_name):
        print("Welcome Back" + name + " Here Are The Logs Available To You")
    else:
        print("Hello " + name + ", Here Are The Logs Available To You")
    availableLogs()
    LogChoice = (input("Which Log Would You Like To Read? (Enter The Number Only): "))
    while LogChoice != -1:
        if (LogChoice == "258"):
            print("I would recommend avoiding this topic")
            time.sleep(0.5)
            printOldMachineText(">Loading")
            time.sleep(5)
            oldMachine()
            return
        elif (LogChoice == "-1"):
            break
        elif (not fileDict.__contains__(LogChoice)):
            print("Invalid Log Selection")
        else:
            Log = fileDict[LogChoice]
            print("\nNow Printing Log: ")
            print(Log)
        LogChoice = input("Would You Like To Read Another Log? (-1 to exit): ")
    print("Goodbye " + name + ", I Hope You Learned All You Wanted, I Wish To See You Soon :)")
    file.close()
    if (not past_name):
        file = open("PastNames.txt", "a")
        file.write(name + "\n")
        file.close()
    return



main()