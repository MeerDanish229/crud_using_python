import sqlite3

conn = sqlite3.connect('database.db')
cursor =conn.cursor()
def create_tbl():
    cursor.execute('''CREATE TABLE IF NOT EXISTS STD_TBL(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT, 
    CONTACT_NO INTEGER
    )
    
   ''')
    
def insert(data):
    sql ="INSERT INTO STD_TBL (NAME,CONTACT_NO) VALUES(?,?)"
    cursor.execute(sql,data)
    conn.commit()

def fetch():
    sql="SELECT * FROM  STD_TBL"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def delete_record(id):
    sql="DELETE FROM STD_TBL WHERE ID=?"
    cursor.execute(sql,(id,))
    conn.commit()


def update_record(new_record,record_id):
    sql="UPDATE STD_TBL SET NAME=? ,CONTACT_NO=? WHERE ID=?"
    cursor.execute(sql,(*new_record,record_id))
    conn.commit()


#create_tbl()
# student_data = ("Meer Danish", 3350202707)
# insert(student_data)
result=fetch()
print(result)
# delete_record(4)
update_data = ("Meer Danish Nagori", 3350202707)
update_record(update_data,6)
