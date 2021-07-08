import psycopg2
from django.conf import settings


class FormDb():
    conn = None
    
    def __init__(self):
        try:
            dbInfo = settings.DATABASES['default']
            print(dbInfo['NAME'])
            self.conn = psycopg2.connect(database = dbInfo['NAME'], user = dbInfo['USER'], password = dbInfo['PASSWORD'], host = dbInfo['HOST'], port = dbInfo['PORT'])
        except:
            print("Cannot connect to the database") 
    
    def TableGenerator(self,name):
        cursor = self.conn.cursor()
        sql ='''CREATE TABLE tesForm_''' +name +'''(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT
                )'''
        
        cursor.execute(sql)
        print("Table created successfully........")
        self.conn.commit()
        self.conn.close()   
        
         
    def TableLists(self):
        tableList=[]
        cursor = self.conn.cursor()
        sql ="""SELECT table_name FROM information_schema.tables
                WHERE table_schema = 'public'"""
        
        cursor.execute(sql)
        for table in cursor.fetchall():
            # print(table[0].startswith('tesform_'))
            if table[0].startswith('tesform_'):
                print(table[0])
                tableList.append(table[0])
            
        self.conn.close()
        return tableList