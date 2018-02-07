import sqlite3

#Creating a connection object with sightind.db
conn = sqlite3.connect('sightings.db')
c = conn.cursor()

#creating a table; storing statements strings

strsql = """
        CREATE TABLE if not exists sightings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city text,
            comments text,
            country text, 
            shape text, 
            state text
            );
        """

strsql2 = """
        Insert into sightings (city,country,shape, state)
        Values('Chicago','United Stage','Square','Texas');
        """
   
#Executing statments    
c.execute(strsql)
c.execute(strsql2)

#Commiting to change
conn.commit()
conn.close()

    
