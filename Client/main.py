import time
import schedule
import mysql.connector
import urllib.request
import vlc


from datetime import datetime
from os.path import exists

#Uncomment in production, caused issues in Docker
lockdownplayer = vlc.MediaPlayer('Lockdown.mp3')

ThisRoom = 'Room1' #Enter Room Name Here, See user manual for more info

File = open('../../creds.txt', 'r')
Filelines = File.readlines()


DbUser = Filelines[0].strip()
DbPass = Filelines[1].strip()
DbHost = Filelines[2].strip()
DbName = Filelines[3].strip()

mydb = mysql.connector.connect(user=DbUser, password=DbPass, host=DbHost, database=DbName)
mydb1 = mysql.connector.connect(user=DbUser, password=DbPass, host=DbHost, database=DbName)
mydb2 = mysql.connector.connect(user=DbUser, password=DbPass, host=DbHost, database=DbName)

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
                lockdownplayer.play()
                print('Lockdown found, played sound')
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
                        MsgFile = vlc.MediaPlayer(AudioFile)
                        MsgFile.play()
                        print('Lockdown Found, Played sound')
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
