import sqlite3

conn = sqlite3.connect('sightings.db')
c = conn.cursor()

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
        Values('Chicago','United Stage','Square','Texas');"""
   
c.execute(strsql)
c.execute(strsql2)
conn.commit()
conn.close()

    
