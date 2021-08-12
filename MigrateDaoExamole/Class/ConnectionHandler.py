import pyodbc
class ConnectionHandler:
    def __init__(self,host,database,user,passwd):
        self.host=host
        self.database=database
        self.user=user
        self.passwd=passwd
        self.conn=None

    def connect(self):
        try:
            self.conn=pyodbc.connect('Driver={SQL Server};SERVER='+self.host+';DATABASE='+self.database+';UID='+self.user+';PWD='+self.passwd)
            return self.conn
        except:
            print("no hay conexion")
            return None
    
    def executeQuery(self,query):
        self.connect()
        cursor=self.conn.cursor()
        result=cursor.execute(query)
        self.conn.commit()
        self.conn.close()
        return result

    def executeSelect(self,query):
        self.connect()
        cursor=self.conn.cursor()
        result=cursor.execute(query).fetchall()
        self.conn.close()
        return result
