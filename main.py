#create phone which will
#accept user input to create ,
# existing contact class can delete contact, modify name and number of existing contact, 
# search number based on name
# adding a comment to test github
# create command line interface and then connect it with pysimple gui with frontend based

import sqlite3
import os
class new_contact():

    def __init__(self):
        print('New contact class used to make a new contact to the database')
        self.conn = sqlite3.connect('info.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS phonebook(
            name text NOT NULL,
            number text NOT NULL)''')
        
    def asking_stuff(self):
        self.__ask_name()
        self.__ask_contact()
        self.__surity()
        

    def __ask_name(self):
        name = input("Enter name:")
        self.__name = name
        
    def __ask_contact(self):
        contact = int(input("Enter contact:"))
        self.__contact = str(contact)

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
        self.conn.execute(f"insert into phonebook values('{self.__name}','{self.__contact}')")
        self.conn.commit()


class edit_contact(new_contact):
    
    def __init__(self):
        if os.path.isfile('info.db'):
            c = int(input('''Make a choice:
            search database - 1
            edit name - 2
            edit number - 3
            '''))
            
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
        
    def search(self):
        try:
            self.conn = sqlite3.connect('info.db')
            c = self.conn.cursor()
            i = input("Enter query to search:")
            if(i.isdigit()):
                print("Searching by number")
                query = 'SELECT * FROM phonebook where number="{}"'
            else:
                print('Searching by name')
                query = 'SELECT * FROM phonebook where name="{}"'

            c.execute(query.format(i))
            
            a = c.fetchall()
            for i in a:
                print('Name: '+i[0]+"\nContact :"+i[1])


        except:
            print('No record Found!')
            
        
    def __edit(self,n,cn):
        # try:
        #     self.conn = sqlite3.connect('info.db')
        #     c = self.conn.cursor()
        #     query = input('Enter name:')
        #     if(n == 'name'):
        #         # query = f'select name from phonebook where {n} = "{query}"'
        #         # query = (c.fetchone()[0])
        #         new_name = input("Enter new name:")
        #         c.execute(f"update phonebook set name = '{new_name}' where name = '{query}';")
        #         self.conn.commit()

        #     elif(query.isdigit() and n == 'number'):
        #         pass
        #     elif(n == 'name'):
        #         pass
        #     elif(n == 'name'):
        #         pass
        #     # if(query.isdigit()):
        #     #     new_name = int(input(f'Enter new {n}:'))
        #     #     c.execute(f"UPDATE phonebook SET {n}='{new_name}' where {cn} = '{query}';")
                
        #     # else:
        #     #     c.execute('SELECT number from phonebook where ')
        #     #     new_name = input(f'Enter new {n}:')
        #     #     c.execute(f"UPDATE phonebook SET {n}='{new_name}' where {cn} = '{query}';")
                
            
        # except:
        #     print('No record found!')  
        pass

class delete_contact():
    def __init__(self):
        try:
            self.conn = sqlite3.connect('info.db')
            c = self.conn.cursor()
            name = input("Enter name to delete contact from phonebook:")
            c.execute(f'delete from phonebook where name="{name}"')
            self.conn.commit()
        except:
            print('no database found')


        
if __name__ == '__main__':
    a = delete_contact()
    