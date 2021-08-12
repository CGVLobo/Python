from Class.Migratition import Migration
#from Class.ConnectionHandler import ConnectionHandler
migration=Migration()
print(migration.getPath())
migration.getListPath()
migration.makeMigration()

#handle=ConnectionHandler("LAPTOP-IU8SOAQU\SQLEXPRESS","pythonBD","loboCGV","detonador")

#print(handle.connect())
#print(handle.executeQuery("select * from table1").fetchall())
