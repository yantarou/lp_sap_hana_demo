import dbapi 

conn = dbapi.connect('pstyoc141', 30015, 'SYSTEM', 'P@ssw0rd')

print conn.isconnected() 
