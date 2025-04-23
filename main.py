dict = {}
tempDict = {}

transaction = False

def printMenu():
    print("1. Begin Transaction")
    print("2. Create/Update Key")
    print("3. Retreive Value")
    print("4. Save Transaction")
    print("5. Abort Transaction")
    print("6. Exit Program")

def begin_transaction():
    global transaction
    if (transaction):
        print("Error! A transaction is already in place!")
        return
    transaction = True
    print("Transaction has begun!")

def put(key, value):
    global tempDict
    tempDict[key] = value
    print("Key-Value pair has been created/updated!")

def get(key):
    global dict
    if (not key in dict):
        return None
    else:
        return dict[key]


def commit():
    global transaction
    global dict
    global tempDict
    if(not transaction):
        print("Error! There needs to be a transaction going on!")
        return
    dict.update(tempDict)
    transaction = False
    print("Transaction has been saved!")


def rollback():
    global transaction
    global tempDict
    if(not transaction):
        print("Error! There needs to be a transaction going on!")
        return
    tempDict.clear()
    transaction = False
    print("Transaction has been canceled!")



def main():
    print("Welcome to Joshua's Data Processing and Storage system! (DPaS)")

    while True:
        printMenu()
        option = input("Enter menu option:")
        
        if (option == "1"):
            begin_transaction()
        elif (option == "2"):
            global transaction
            if (not transaction):
                print("Error! There needs to be a transaction going on!")
            else:
                key = input("Enter the key you want to create/update")
                value = input("Enter the value for your key")
                put(key, value)
        elif (option == "3"):
            key = input("Enter the key")
            print("The value for your key is ", get(key))
        elif (option == "4"):
            commit()
        elif (option == "5"):
            rollback()
        elif (option == "6"):
            print("Thank you for using the DPaS system!")
            break
        else:
            print("Please enter an integer in the range 1-5")


if __name__=="__main__":
    main()
