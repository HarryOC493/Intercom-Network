import time
import schedule
import mysql.connector
import pygame
import urllib.request


from datetime import datetime
from os.path import exists

#Uncomment in production, caused issues in Docker
#pygame.mixer.init()

ThisRoom = 'Room1' #Enter Room Name Here, See user manual for more info

mydb = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')
mydb1 = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')
mydb2 = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')

mycursor = mydb.cursor(buffered=True)

def poll():
    myresult = mycursor.execute("SELECT * FROM Lockdowns")
    LockdownCount = mycursor.rowcount
    
    if LockdownCount != 0:
        #Lockdown Found
        LockdownRows = mycursor.fetchall() 
        for x in LockdownRows:
            if x[2] == bytearray(b'1'):
                #Do Lockdown Test Things
                print('This is a test')
            else:
                #Do Lockdown Things

                #Uncomment in production, caused issues in Docker
                #pygame.mixer.music.load("lockdown.mp3")
                #pygame.mixer.music.play()
                #pygame.mixer.music.unload()
    else:
        #No Lockdown found. Contine
        now = datetime.now()
        Hour = now.strftime("%Y%m%d%H")
        mycursor1 = mydb1.cursor(buffered=True)

        fields = ['Tmestamp', 'Message', 'Rain', 'MsgName', ThisRoom]
        values = ', '.join(fields)
        statement = 'SELECT '+values+" FROM Messages WHERE Tmestamp LIKE '%"+Hour+"%'"

        MessageFinder = mycursor1.execute(statement)
        MessageCount = mycursor1.rowcount

        if MessageCount != 0:
            #At least one message has been found
            MessageRows = mycursor1.fetchall()
            for row in MessageRows:
                if row[4] != '':
                    #If message applies to this room:

                    #Check if file has been downloaded
                    FileName = row[3]
                    isFile = exists(FileName)
                    if isFile == False:
                        #File not found, Download
                        FileAddress = 'https://cetsstunnel-harryocon.pitunnel.com/'+FileName
                        urllib.request.urlretrieve(FileAddress, FileName)
                    else:
                        #File has been downloaded already
                        pass
                else:
                    pass
        else:
            pass

        now = datetime.now()
        Minute = now.strftime("%Y%m%d%H%M")
        mycursor2 = mydb2.cursor(buffered=True)

        fields = ['Tmestamp', 'Message', 'Rain', 'MsgName', ThisRoom]
        values = ', '.join(fields)
        statement1 = 'SELECT '+values+" FROM Messages WHERE Tmestamp LIKE '%"+Minute+"%'"

        MessageTime = mycursor2.execute(statement1)
        IsMessage = mycursor2.rowcount

        if IsMessage != 0:
            #At least one message has been found
            NowMessages = mycursor2.fetchall()

            for row in NowMessages:
                if row[4] != '':
                    #Message applies to this room:

                    if row[1] == '1':
                        #Check if sending a message

                        #Get message name and play
                        AudioFile = row[3]
                        #Uncomment The following in production, causing issue in docker testing
                        #pygame.mixer.music.load(AudioFile)
                        #pygame.mixer.music.play()
                        #pygame.mixer.music.unload()
                    if row[2] == '1':
                        #Check if rain indicator is enables
                        print('overwrite rain')
                        #Light Led


                else:
                    #Message does not apply to this room
                    pass










schedule.every(15).seconds.do(poll)

while True:
    schedule.run_pending()
    time.sleep(1)
