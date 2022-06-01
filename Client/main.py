import time
import schedule
import mysql.connector
import urllib.request
import vlc


from datetime import datetime
from os.path import exists

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
        #Lockdown row found, checking if its Active
       
        LockdownRows = mycursor.fetchall() 
        
        for x in LockdownRows:
            if x[1] == bytearray(b'1'):
                #Lockdown is active
                print('Lockdown Active, checking if test?')
                
                if x[2] == bytearray(b'1'):
                    #This is a test
                    print('This is a test')
                    
                else:
                    #Not a test, Lockdown is active
                    
                    #uncomment in production
                    #lockdownplayer = vlc.MediaPlayer('lockdown.mp3')
                    #lockdownplayer.play()
                    print('Lockdown found, played sound')
                    
                    
                    
                    
                    #------------------------------ Lockdown functions complete, onto messages ---------------------------------
                    
                    
                    
                    
            else:
                #No Active Lockdown, Check if there are any messages pending for download
                print('No active lockdown, Checking for pending downloads')
                
                now = datetime.now()
                Hour = now.strftime("%Y%m%d%H")
                mycursor1 = mydb1.cursor(buffered=True)
                fields = ['Tmestamp', 'Message', 'Rain', 'MsgName', ThisRoom]
                values = ', '.join(fields)
                statement = 'SELECT '+values+" FROM Messages WHERE Tmestamp LIKE '%"+Hour+"%'"

                #Check SQL Db for Messages to be played this hour
                MessageFinder = mycursor1.execute(statement)
                MessageCount = mycursor1.rowcount

                if MessageCount != 0:
                    #At least one message has been found
                    print('--------------------------------------------------------------------------')
                    print('At least one message has been found (From downloading function)')
                    MessageRows = mycursor1.fetchall()
                    
                    for row in MessageRows:
                        #Check if message applies to this room
                        if row[4] == bytearray(b'1'):
                            #Message applies to this room, check if it needes to be downloaded
                            print('Message Applies to this room')

                            FileName = row[3]
                            FileName1 = FileName.replace('/', '')
                            isFile = exists(FileName1)
                            if isFile == False:
                                #File not found, Download
                                print('File not found, downloading')
                                FileAddress = 'https://webtunnel-harryocon.pitunnel.com'+FileName
                                urllib.request.urlretrieve(FileAddress, FileName1)
                            else:
                                #File has been downloaded already
                                print('File previously downloaded, passing')
                                pass
                        else:
                            #Message does not apply to this room
                            print('Message does not apply to this room')
                            pass
                else:
                    #No message found
                    print('No message found (From downloading function)')
                    print(statement)
                    pass
                
                #--------------- Downloading function complete ----------------------------------------------

                #----------------- Beginning To check is messsage needs to be played now ---------------
def pollPlay():
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
        print('--------------------------------------------------')
        print('At least one message has been found (From play messages function')
        NowMessages = mycursor2.fetchall()

        for row in NowMessages:
            if row[4] == bytearray(b'1'):
                print('Message applies to this room')
                #Message applies to this room:

                if row[1] == bytearray(b'1'):
                    print('Send message tickbox checked')
                    #Check if sending a message

                    #Get message name and play
                    AudioFile = row[3]
                    AudioFile1 = AudioFile.replace('/', '')
                    #Uncomment The following in production, causing issue in docker testing
                    MsgFile = vlc.MediaPlayer(AudioFile1)
                    MsgFile.play()
                    print('Lockdown Found, Played sound')
                if row[2] == bytearray(b'1'):
                    #Check if rain indicator is enables
                    print('overwrite rain')
                    #Light Led


            else:
                #Message does not apply to this room
                print('Message does not apply to this room (From Play message function')
                pass










schedule.every(15).seconds.do(poll)
schedule.every(60).seconds.do(poll)

while True:
    schedule.run_pending()
    mydb.commit()
    mydb1.commit()
    mydb2.commit()
    time.sleep(1)
