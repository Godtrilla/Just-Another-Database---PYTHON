import sys, os, time

import Database

'''
This is the main function file
And should be ran as the main file. 
    '''

#RESOURCE FILES
parksFile = 'Parks2.csv'
parksDB = 'ParksDatabase.data'

#MAIN FUNCTION, CONTROLLED BY MENU OPTIONS
def go():
    print('''
      [01] Create New Database
      [02] Enter Parks Database
      [03] Open Database
      [00] Exit
    ''')
    while True:
        menu = input(' Menu OPTION >>')
        if menu == '01' or menu == '1':
            os.system("clear")
            print('FUNCTION TEMPORARILY UNAVAILABLE')
        elif menu == '02' or menu == '2':
            print("ENTERING DATABASE")
            enterDatabase()
        elif menu == '03' or menu == '3':
            print('FUNCTION TEMPORARILY UNAVAILABLE')
        elif menu == '00' or menu == '0':
            os.system("clear")
            print('EXITING DATABASE')
            Database.getData()
            sys.exit(2)
        else:
            print(' INPUT ERROR %s' % (menu))

'''
Function takes user into the Parks database 
which is controlled by a menu.
		'''

def enterDatabase():
    import CSVcontroller
    CSVcontroller.formatter(parksFile)


    while True:
        prompt()
        menu = input(' Menu OPTION >>')

        #UPDATE RECORD
        if menu == '01' or menu == '1':
            os.system("clear")
            recordNum = input("ENTER ID NUMBER >>")
            if not Database.idChecker(recordNum):
                print("INPUT ERROR, RECORD DOES NOT EXIST")
            else:
                Database.updateRecord(parksDB, recordNum)

        #DISPLAY RECORD
        elif menu == '02' or menu == '2':
            os.system("clear")
            recordNum = input("ENTER ID NUMBER >>")
            if not Database.idChecker(recordNum):
                print("INPUT ERROR, RECORD DOES NOT EXIST")
            else:
                print(Database.displayRecord(parksDB, recordNum))

        #CREATE/ADD RECORD
        elif menu == '03' or menu == '3':
            os.system("clear")
            Database.createRecord()

        #DELETE RECORD
        elif menu == '04' or menu == '4':
            os.system("clear")
            recordNum = input("ENTER ID NUMBER >>")
            if not Database.idChecker(recordNum):
                print("INPUT ERROR, RECORD DOES NOT EXIST")
            else:
                Database.deleteReocrd(parksDB, recordNum)

        #EXITING DATABASE
        elif menu == '05' or menu == '5':
            os.system("clear")
            print('EXITING DATABASE')
            Database.getData()
            sys.exit(2)


        #INPUT ERROR
        else:
            print(' INPUT ERROR %s' % (menu))

#MENU PROMPT
def prompt():
    print('''
    %s[+]----U.S. NATIONAL PARKS DATABASE----[+]
      [01] Update record
      [02] Display record
      [03] Add record
      [04] Delete record
      [05] Exit Database
    		''')


#MAIN FUNCTION BEING CALLED
go()


#EXIT HANDLER
if __name__ == '__main__':
    time.sleep(3)
    os.system("clear")
