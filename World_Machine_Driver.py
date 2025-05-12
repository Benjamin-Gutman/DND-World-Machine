
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

def main(): #You don't need a main function but I'm so used to c++ that I decided to do it this way
    if not passwordDemand():
        return
    readLogCollection()
    availableLogs()
    LogChoice = input("Which Log Would You Like To Read (Enter The Number Only): ")
    Log = fileDict[LogChoice]
    print("\nNow Printing Log: ")
    print(Log)


main()