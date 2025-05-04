
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


readLogCollection()
print(fileDict["00"])