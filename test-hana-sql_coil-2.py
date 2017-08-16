import sys
import getopt
import dbapi

def testhana():
  try:
    # Assume HANA host id is pstyoc141 and instance no is 00.
    # Using SYSTEM user with the password defined at HANA install
    conn = dbapi.connect('pstyoc141', 30015, 'SYSTEM', 'P@ssw0rd') 
  
    # Check if database connection was successful or not 
    print 'Connected:',conn.isconnected() 
  
    # Create a schema and table 
    c = conn.cursor() 
    stmnt = 'create schema TEST_SCHEMA'
    c.execute(stmnt)
    stmnt = 'create column table TEST_SCHEMA.TABLE1 (ID integer, NAME varchar(10))'
    c.execute(stmnt) 
    print 'Schema and table created' 
  
    # Insert some data into table
    stmnt = 'insert into TEST_SCHEMA.TABLE1 values (?,?)'
    c.execute(stmnt, (1,'A'))
    c.execute(stmnt, (2,'B'))
    c.execute(stmnt, (3,'C'))
    print '3 records inserted into table'
  
    # Disconnect from database 
    conn.commit()
    conn.close()
  
    # Check if database connection was successful or not 
    print 'Connected:',conn.isconnected() 
  
    # Assume HANA host id is pstyoc141 and instance no is 00.
    # Using SYSTEM user with the password defined at HANA install
    conn = dbapi.connect('pstyoc141', 30015, 'SYSTEM', 'P@ssw0rd')
  
    # Check if database connection was successful or not 
    print 'Connected:',conn.isconnected()
  
    # Count the number of rows in the table 
    c = conn.cursor() 
    stmnt = 'SELECT Count(*) FROM TEST_SCHEMA.TABLE1'
    c.execute(stmnt)
    result = c.fetchall()
    for row in result:
    	reccount = row[0]
    	print reccount,'records are in the table' 
  
    # Delete the schema and table 
    stmnt = 'drop schema TEST_SCHEMA CASCADE'
    c.execute(stmnt)
    print 'Schema and table deleted' 
    return;
  except KeyboardInterrupt:
    print "Bye"
    sys.exit()

def cleanhana():
  try:
    # Assume HANA host id is pstyoc141 and instance no is 00.
    # Using SYSTEM user with the password defined at HANA install
    conn = dbapi.connect('pstyoc141', 30015, 'SYSTEM', 'P@ssw0rd') 
  
    # Check if database connection was successful or not 
    print 'Connected:',conn.isconnected() 

    # Delete the schema and table 
    c = conn.cursor() 
    stmnt = 'drop schema TEST_SCHEMA CASCADE'
    c.execute(stmnt)
    print 'Schema and table deleted' 
  
    # Disconnect from database 
    conn.commit()
    conn.close()

    return;
  except Exception, e:
    print ""

def usage():
  print 'test-hana-sql.py [OPTION]'
  print '  -h, --help			help'
  print '  -1, --once			run one test'
  print '  -c COUNT, --count=COUNT	run COUNT number of tests'
  print '  -f, --forever			do not stop running tests'

def main(argv):
  count = 1
  countto = ''

  try:
    opts, args = getopt.getopt(argv,"h1c:f",["help", "once", "count=", "forever"])
  except getopt.error:
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt in ("-1", "--once"):
      testhana()
    elif opt in ("-c", "--count"):
      countto = int(arg)
      while count <= countto:
        testhana()
        print 'The count is:', count
        print
        count = count + 1
    elif opt in ("-f", "--forever"):
      while True:
        cleanhana()
        testhana()
        print 'The count is:', count
        print
        count = count + 1

if __name__ == "__main__":
   main(sys.argv[1:])
