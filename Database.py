import os
import sys
import CSVcontroller

'''
This class contains the functions that 
are used to manipulate the database.
    '''

#VARIABLES THAT KEEPS TRACK OF FILE SIZE AND RECORDS
num_records = 748
record_size = 168

#UNUSED FUNCTION THAT WAS TO BE USED TO OPEN DIFFERENT DATABASES
fileNames = {}
data = [6]


#UNFINISHED FUNCTIONALITY
def createDatabase():
    fileName = ""
    fileNames.update(fileName)

#UNFINISHED FUNCTIONALITY
def openDatabase(file):

    if file not in fileNames:
        return print("FILENAME DOES NOT EXIST")
    else:
        return print("open the file")

#UNFINISHED FUNCTIONALITY
def closeDatabase():
    return 0

#FUNCTION DISPLAYS RECORD TO CONSOLE
def displayRecord(f, recordNum):
        record = ""
        recordNum = CSVcontroller.idMap.get(recordNum)
        Success = False

        if recordNum >= 0 and recordNum < num_records:
            with open(f, "r") as f:
                f.seek(0, 0)
                f.seek(record_size * (recordNum - 1))  # offset from the beginning of the file
                record = f.readline()
                Success = True
                f.close()
        return " ".join(record.split()), Success

#FUNCTION UPDATES RECORD IN PLACE
def updateRecord(file, recordNum):
    data = getData()
    line = (data[0] + "     " + data[1] + "    "  + data[2] + "  " + "    " + data[3])
    line2 = ("    " + data[4] + "    " + data[5] + "  " + data[6])
    recordNum = CSVcontroller.idMap.get(recordNum)

    with open(file, "r") as f:
            record = f.readlines()
            record[recordNum - 1] = (line + line2 + "\n")
    with open(file, "w") as f:
            f.writelines(record)
            f.close()
    return print("RECORD UPDATED")



#UNFINISHED FUNCTIONALITY
def createRecord():
    data = getData()
    line = (data[0] + "     " + data[1] + "    "  + data[2] + "  " + "    " + data[3])
    line2 = ("    " + data[4] + "    " + data[5] + "  " + data[6])


#FUNCTION DELETES RECORD IN PLACE
def deleteReocrd(file,recordNum):
    record = ""
    recordNum = CSVcontroller.idMap.get(recordNum)

    with open(file, "r") as f:
            record = f.readlines()
            record[recordNum - 1] = "\n"
    with open(file, "w") as f:
            f.writelines(record)
            f.close()

    return print("RECORD DELETED")

#FUNCTION TAKES USER INPUT TO FORM A COMPLETE RECORD AND
#RETURNS INFORMATION IN AN ARRAY
def getData():
    data = []
    id = ""
    region = ""
    state = ""
    code = ""
    name = ""
    type = ""
    visitors = ""

    while True:
        id = input('''
            ENTER ID NUMBER>>>>
              		''')
        if idChecker(id):
                print("INPUT ERROR, ID ALREADY EXIST OR INCORRECT FORMAT")
        else:
            data.append(id)
            break



    region = input('''
    ENTER REGION ABBREVIATION>>>>
      		''')
    os.system("clear")
    data.append(region)

    state = input('''
    ENTER STATE ABBREVIATION>>>>
      		''')
    os.system("clear")
    data.append(state)

    code = input('''
    ENTER CODE IDDNTIFIER>>>>
      		''')
    os.system("clear")
    data.append(code)

    name = input('''
    ENTER PARK NAME>>>>
      		''')
    os.system("clear")
    data.append(name)

    type = input('''
    ENTER PARK TYPE>>>>
      		''')
    os.system("clear")
    data.append(type)

    visitors = input('''
    ENTER NUMBER OF VISITORS>>>>
      		''')
    os.system("clear")
    data.append(visitors)

    return data


#FUNCTION CHECKS TO ENSURE ID DOES NOT ALREADY EXIST
def idChecker(id):
    import CSVcontroller

    if id in CSVcontroller.idMap:
        return True
