# create phone which will
# accept user input to create ,
# existing contact class can delete contact, modify name and number of existing contact, 
# search number based on name
# adding a comment to test github
# create command line interface and then connect it with pysimple gui with frontend based
# No gui becouse i cant understand django and tkinter is .....

import sqlite3
import time
from os import *
import base64

#Create a new entry inside database phonebook
class new_contact():

    def en(self,plain):
        return base64.b64encode(plain.encode('ascii')).decode("ascii")
    def de(self,cipher):
        return base64.b64decode(cipher.encode('ascii')).decode("ascii")

	#create database before entring the database
    def __init__(self):
        print('New contact class used to make a new contact to the database')
        self.conn = sqlite3.connect('info.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS phonebook(
            name text NOT NULL,
            number text NOT NULL)''')
        
    def asking_stuff(self):
        self.ask_name()
        self.ask_contact()
        self.__surity()
        

    def ask_name(self):
        name = input("Enter name:")
        self.__name = name
        return name

    def ask_contact(self):
        contact = int(input("Enter contact no.:"))
        self.__contact = str(contact)
        return contact

    def __surity(self):
        print('Name:'+self.__name)
        print('contact:'+str(self.__contact))
        print('Do you want to save this in phonebook?(Y/N)')
        c = input('# ')
        if c == 'Y' or c == 'y':
            try:
                self.storing_in_db()
                print('\n\tSaved Successfully\n')
            except:
                print('\n\tSaving failed!\n')
        elif c == 'N' or c == 'n':
            self.asking_stuff()
        else:
            print('Invalid choice')
            self.__surity()
#storing in database
    def storing_in_db(self):
        self.conn.execute(f"insert into phonebook values('{self.en(self.__name)}','{self.en(self.__contact)}')")
        self.conn.commit()

#edit contact class to edit or search preexisting record inside database
class edit_contact(new_contact):
    
    def __init__(self):
        if path.isfile('info.db'):
            clear()
            print('''Make a choice:
            search database - 1
            edit name - 2
            edit number - 3
            ''')
            c = int(input('# '))
            
            if c == 1:
                self.search()
            elif c == 2:
                self.__edit('name','number')
            elif c == 3:
                self.__edit('number','name')
            else:
                print('invalid option')
                self.__init__()

        else:
            print('No database found')
#searching within database (standalone function no dependency)        
    def search(self):
        try:
            self.conn = sqlite3.connect('info.db')
            c = self.conn.cursor()
            i = input("Enter query to search:")

            if(i.isdigit()):
                print("Searching by number")
                query = "select * from phonebook where number='{}'"
            else:
                print('Searching by name')
                query = "select * from phonebook where name='{}'"

            c.execute(query.format(self.en(i)))
            
            a = c.fetchall()
            for i in a:
                print('Name: '+str(self.de(i[0]))+"\nContact :"+str(self.de(i[1])))


        except:
             print('No record Found!')
            
#edit function passed on to edit name or number depending on query
    def __edit(self,n,cn):
        try:
            self.conn = sqlite3.connect('info.db')
            c = self.conn.cursor()
            if(n == 'name'):
                name = new_contact.ask_name(self)
                c.execute(f'select number from phonebook where name="{self.en(name)}"')
                number = c.fetchone()[0]
                name = input('Enter new name:')
                c.execute(f'update phonebook set name="{self.en(name)}" where number="{self.en(number)}";')
                
            else:
                name = new_contact.ask_name(self)
                number = input('Enter new number:')
                c.execute(f'update phonebook set number="{self.en(number)}" where name="{self.en(name)}";')
                
            self.conn.commit()
        except:
            print('No data found')

        
#delect contact class to delete contact from info db
class delete_contact(new_contact):
    def cls(self):
    # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def __init__(self):
        try:
            a = []
            self.conn = sqlite3.connect('info.db')
            c = self.conn.cursor()
            name = input("Enter name to delete contact from phonebook:")
            for i in c.execute(f'select * from phonebook'):
                a.append(i[0])

            if self.en(name) in a:
                c.execute(f'delete from phonebook where name="{self.en(name)}"')
                self.cls()
                print('\n\n\tContact Deleted Successfully')
                time.sleep(2.5)
                self.cls()
            else:
                print('Not found inside database')
            self.conn.commit()
        except:
            print('no database found')



# Clears screen
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# default menu option to ask user
def menu():

	print('''Welcome to the commandline phonebook app
    Enter your option:
			1.Create a contact
			2.Delete a contact
			3.Edit contact:''')

	choice = int(input('# '))
	if(choice == 1):
		a = new_contact()	
		a.asking_stuff()
	elif(choice == 3):
		a = edit_contact()
	elif(choice == 2):
		a = delete_contact()


#main event to run application
if __name__ == '__main__':
    clear()
    menu()