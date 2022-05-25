import mysql.connector

ThisRoom = 'Room1'
Hour = '2022051810'

mydb1 = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')
mycursor1 = mydb1.cursor(buffered=True)

fields = ['Tmestamp', 'Message', 'Rain', 'MsgName', ThisRoom]

values = ', '.join(fields)
statement = 'SELECT '+values+" FROM Messages WHERE Tmestamp LIKE '%"+Hour+"%'"
print(statement)
MessageFinder = mycursor1.execute(statement)


Messages = mycursor1.fetchall()

for row in Messages:
    print(row)
