# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect("chinook.db")
def selectOperasyonlari():
    # cursor = connection.execute("""select FirstName, LastName 
    #                             from customers 
    #                             where city='Prague' or city='Berlin' 
    #                             order by FirstName, LastName desc""")
    #descending=azalan, ascending=yukselen
    # for row in cursor:
    #     print("First Name:" + row[0])
    #     print("Last Name:" + row[1])
    #     print("******")
    
    # cursor = connection.execute("""select city, count(*) 
    #                             from customers 
    #                             group by city
    #                             having  count(*) > 1
    #                             order by count(*)""")
                                
    # for row in cursor:
    #     print("City:" + row[0])
    #     print("Count:" + str(row[1]))
    #     print("******")
    
    cursor = connection.execute("""select FirstName, LastName 
                                from customers 
                                where FirstName like 'a%' """)
    
    for row in cursor:
        print("First Name:" + row[0])
        print("Last Name:" + row[1])
        print("******")
        
    connection.close()

selectOperasyonlari()

def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" insert into customers 
                       (firstName, lastName, city, email)
                       values ('Erman', 'Sezer', 'Kirklareli', 
                               'erman@gmail.com')""")
    connection.commit()
    connection.close()
                       
#insertCustomer()
                       
def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" update customers set city='Edirne'
                       where city='Kirklareli' """)
    connection.commit()
    connection.close()                   


#updateCustomer()

def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" delete from customers 
                       where customerid=60 """)
    connection.commit()
    connection.close() 
    
#deleteCustomer()

def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""SELECT albums.Title, artists.name 
                                FROM artists INNER JOIN albums
                                on artists.ArtistId=albums.ArtistId
                                """)
    for row in cursor:
        print("Title: " + row[0] + " Name: " + row[1])

        
    connection.close()
    
joinOperasyonlari()



