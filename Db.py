import sqlite3

class Database:
    def __init__(self,db:str):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur = self.con.execute('''CREATE TABLE IF NOT EXISTS contacts 
                                    (Id INTEGER PRIMARY KEY , Name TEXT , Lastname TEXT , Address TEXT , Phone TEXT)''')
        self.con.commit()

    def insert(self,name:str,lname:str,add:str,tel:str):
        self.cur.execute('INSERT INTO contacts VALUES (NULL,?,?,?,?)',
                         (name,lname,add,tel))
        self.con.commit()

    def select(self):
        self.cur.execute('SELECT * FROM contacts ORDER BY Id ASC')
        records = self.cur.fetchall()
        return records

    def delete(self,id):
        self.cur.execute('DELETE FROM contacts WHERE Id = ?',(id,))
        self.con.commit()

    def update(self,id,name,lname,add,tel):
        self.cur.execute('''UPDATE contacts SET 
                         Name = ? , Lastname = ? , Address = ? , Phone = ? 
                         WHERE Id = ?''',(name,lname,add,tel,id))    
        self.con.commit()

    def exit(self):
        self.con.close()    

    def search(self,name:str):
        self.cur.execute('''SELECT * FROM contacts WHERE 
                         Id=? or Name=? or Lastname=? or Address=? or Phone=? ''',
                         (name,name,name,name,name))
        records = self.cur.fetchall()
        return records
       