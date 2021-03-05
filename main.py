#create phone which will
#accept user input to create ,
# existing contact class can delete contact, modify name and number of existing contact, 
# search number based on name
# create command line interface and then connect it with pysimple gui with frontend based

import sqlite3
import os
class new_contact():

    def __init__(self):
        print('New contact class used to make a new contact to the database')
        self.conn = sqlite3.connect('info.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS phonebook(
            name text NOT NULL,
            number integer NOT NULL)''')
        
    def asking_stuff(self):
        self.__ask_name()
        self.__ask_contact()
        self.__surity()
        self.storing_in_db()

    def __ask_name(self):
        name = input("Enter name:")
        self.__name = name
        
    def __ask_contact(self):
        contact = int(input("Enter contact:"))
        self.__contact = contact

    def just_printing(self):
        print(self.name)
        print(self.contact)

    def __surity(self):
        print('Do you want to save this in phonebook?(Y/N)')
        print('Name:'+self.__name)
        print('contact:'+str(self.__contact))
        c = input()
        if c == 'Y':
            self.storing_in_db()
        elif c == 'N':
            self.asking_stuff()
        else:
            print('Invalid choice')
            self.__surity()

    def storing_in_db(self):
        self.conn.execute(f"insert into phonebook values('{self.__name}',{self.__contact})")
        self.conn.commit()


class edit_contact(new_contact):
    
    def __init__(self):
        if os.path.isfile('info.db'):
            pass
        else:
            print('No data found')
        
    def search(self):
        try:
            self.conn = sqlite3.connect('info.db')
            c = self.conn.cursor()
            c.execute(f'SELECT * FROM phonebook where ')
        except:
            print('No such record')
        
    def __edit_name(self):
        pass

    def __edit_number(self):        
        pass
            
   

if __name__ == '__main__':
    a = edit_contact()
  