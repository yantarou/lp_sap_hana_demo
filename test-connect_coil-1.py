import dbapi 

conn = dbapi.connect('pstyoc140', 30015, 'SYSTEM', 'P@ssw0rd')

print conn.isconnected() 
