# -*- coding:Latin-1 -*-
import serial
import serial.tools.list_ports
from  tkinter import *
from tkinter import ttk

def OpenPort():
    #fonction eventmentielle lie au clic OpenPort
    global ser
    global LClose
    portName = selected_port.get()
    ser = serial.Serial(portName[0:5])
    LClose.configure(bg = "yellow",text = 'Port Opened'+portName )

def ListPort():
    global Cport
    global LInfo
    listePorts = serial.tools.list_ports.comports()
    CPort['values'] = listePorts
    
def ClosePort():
    global LClose
    ser.close()
    LClose.configure(bg = "red",text = 'Port Closed' )

def ReadDataPort():
    global LData,LDataStr,LDataHexa, data, hexdata
    #le document'https://pyserial.readthedocs.io/en/latest/shortintro.html?highlight=readline#readline'
    data = ser.readline();#lit data du port srie, c'est une ligne y compris le '\n'
    bindata = []
    hexdata = []
    for i in range(len(data)):
        bindata.append(data[i])
        hexdata.append(hex(data[i]))
    LData.configure(text = str(bindata))
    LDataStr.configure(text=str(data))
    LDataHexa.configure(text=str(hexdata))

def WriteData():
    ser.write(str(value).encode('utf-8'))
   
#affichage
def ReadMto():
    
    

    ser.timeout= 0.8

    #print(datetime.datetime.utcnow())

    input_data = ''
    input_data = ser.readline()
    LongeurTrame=len(input_data)

    print('')
    print(f"Trame reu: {input_data}")
    print('')

    if LongeurTrame!=0 :
        #Une tram a t reu
        if input_data[1]==0x23 :
            #Caractre '#' reu
            #Question 3.1 : ajouter un label qui permet d'afficher le numero de trame reu 
            LDataFirmware.configure(text='Trame'+str(input_data[2]-0x30))   
            
            if input_data[2] == 0x31:
                #Trame 1 - Firmware
                print(f"Trame 1: Firmware")
                print(f"{input_data[3:len(input_data)-1]}")
                LDataFirmware.configure(text='Trame'+str(input_data[2]-0x30)) 

            elif input_data[2] == 0x32:
                #Trame 2 - Date
                num_jour=input_data[3] - 0x30
            
                Jours_semaine=['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
                jour=Jours_semaine[num_jour-1]
           
                if(input_data[4]==0x20):  #data 4 (0-3)
                   jour_date=input_data[5] - 0x30
                
                else:
                   jour_date=(input_data[4]-0x30)*10+(input_data[5]-0x30)
            
                Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','aot','septembre','octobre','oovembre','dcembre']  
                if input_data[6]==0x20:
                   mois=Mois[input_data[7]-0x30-1]

                else:
                   mois=Mois[(input_data[6]-0x30)*10+(input_data[7]-0x30)-1]

                anne=input_data[8:12].decode('ascii')

                LDataDate.configure(text='On est le '+   jour  + ' '+ str(jour_date)+' '+ mois+' '+ anne )  

            elif input_data[2] == 0x33:
                #Trame 3 - Heures
                heures = input_data[3:5].decode('ascii')
                minutes = input_data[5:7].decode('ascii')
                secondes = input_data[7:9].decode('ascii')
                dixiemes = input_data[9:11].decode('ascii')
                LDataHeures.configure(text='On est le '+heures+' : '+minutes+' : '+secondes+' : '+ dixiemes )

            elif input_data[2] == 0x34:
                #Trame 4 - Temperatures
                #signe = input_data[3].decode('ascii')
                #partie_entire = input_data[4:6].decode('ascii')
                #point = input_data[6].decode('ascii')
                #dixiemes = input_data[7:9].decode('ascii')
                #LDataTemperature.configure(text='Il fait  '+signe+''+partie_entire+' '+point+' '+ dixiemes+' C' )
                temperature = input_data[3:8].decode('ascii')
                LDataTemperature.configure(text='Il fait  '+temperature+' C' )

            elif input_data[2] == 0x35:
                #Trame 5 - Vent
                vitesse=0
                if data[2]==0x35:
                   i=3
                   vitesse=0
                   Orientation=['N','NE','E','SE','S','SO','O','NO']

                   while(data[i]==0x3C):
                      i=i+1
                      vitesse=vitesse+10

                   vent=Orientation[data[i]-0x30]
          
                   LDataVent.configure(text='Vent de vitesse'+' '+ str(vitesse) +' '+'noeuds'+' '+ vent+ "" )

            
    fen1.after(50,ReadMto)


           
#interface graphique
ser = serial.Serial() #cre un objet de classe Serial

fen1 = Tk() #objet de clas TKinter
fen1.geometry('600x400')
fen1.title("Centrale Mto")

#label 
LPort = Label(fen1,text='Ports:')
LPort.grid(row=2,sticky=E)

#bouton liste port
BListePorts = Button(fen1,text = 'List Ports',command = ListPort)
BListePorts.grid(row=3,sticky=E)

#combo box
selected_port = StringVar()
CPort = ttk.Combobox(fen1, textvariable=selected_port)
CPort['state'] = 'readonly'
CPort.grid(row=4,sticky = E)

#button ouverture
BOpenPort = Button(fen1,text = 'Open Port',command= OpenPort)
BOpenPort.grid(row = 5,sticky = E)


#Label fermeture 
LClose = Label(fen1,text = 'Port Closed',bg = 'red')
LClose.grid(row = 1,column = 2,sticky = E)

#button fermeture
BClosePort = Button(fen1,text='Close Ports',command = ClosePort)
BClosePort.grid(row = 6,sticky=E)

LInfo = Label(fen1,text='',bg = 'white')
LInfo.grid(row = 7,column = 1,columnspan = 3)

#Button receive
BReceive  =Button(fen1,text='read data',command = ReadDataPort)
BReceive.grid(row=8,sticky = E)

#Label Data
LData = Label(fen1,bg = 'yellow')
LData.grid(row = 9,column=1,sticky = W)
LDataStr = Label(fen1,bg = 'gray')
LDataStr.grid(row = 10,column=1,sticky = W)
LDataHexa = Label(fen1,bg = 'cyan')
LDataHexa.grid(row = 11,column=1,sticky = W)

#Button emit
BWrite = Button(fen1,text= 'Write Data',command = WriteData)
BWrite.grid(row = 12,column = 1)

#button mto
BMto = Button(fen1, text ='Mto', command =ReadMto)
BMto.grid(row= 12)

#labelFirmware
LDataFirmware = Label(fen1,bg = 'pink')
LDataFirmware.grid(row = 14,column = 2,columnspan = 1)

#labelDate
LDataDate = Label(fen1,bg = 'light green')
LDataDate.grid(row = 15,column = 2,columnspan = 1)

#LabelHeures
LDataHeures = Label(fen1,bg = 'light blue')
LDataHeures.grid(row = 16,column = 2,columnspan = 1)

#LabelTemperatures
LDataTemperature = Label(fen1,bg = 'light yellow')
LDataTemperature.grid(row = 17,column = 2,columnspan = 1)

#LabelVent
LDataVent = Label(fen1,bg = 'grey')
LDataVent.grid(row = 18,column = 2,columnspan = 1)



#Entre pour le texte  envoyer
value = StringVar() 
value.set("Texte")
entree = Entry(fen1, width=30)
entree.grid(row = 12,column = 2)
fen1.mainloop()



# -*- coding:Latin-1 -*-
#import serial
#import serial.tools.list_ports
#from  tkinter import *
#from tkinter import ttk

#def OpenPort():
#    global ser
#    global LClose
#    portName = selected_port.get()
#    ser = serial.Serial(portName[0:5])
#    LClose.configure(bg = "yellow",text = 'Port Opened'+portName )

#def ListPort():
#    global Cport
#    global LInfo
#    listePorts = serial.tools.list_ports.comports()
#    CPort['values'] = listePorts
    
#def ClosePort():
#    global LClose
#    ser.close()
#    LClose.configure(bg = "red",text = 'Port Closed' )

#def ReadDataPort():
#    global LData,LDataStr
#    data = ser.readline();
#    bindata = []
#    hexdata = []
#    for i in range(len(data)):
#        bindata.append(data[i])
#        hexdata.append(hex(data[i]))
#    LData.configure(text = str(bindata))
#    LDataStr.configure(text=str(data))
#    LDataHexa.configure(text=str(hexdata))


#def WriteData():
#    ser.write(str(value).encode('utf-8'))

#def ReadMeteo():
#    global LData,LDataStr
#    data = ser.readline();
#    #bindata = []
#    #hexdata = []

#    #for i in range(len(data)):
#    #    bindata.append(data[i])
#    #    hexdata.append(hex(data[i]))
#    #LData.configure(text = str(bindata))

#    #LDataStr.configure(text=str(data))
#    #LDataHexa.configure(text=str(hexdata))

#    taille_data=len(data)
#    if taille_data!=0:
#        if data[1]==0x23:
#            LDataTrame.configure(text='Trame'+str(data[2]-0x30))

#        if data[2]==0x31: #affichage trame 1
#            LDataFirmware.configure(text='Firmware:  '+ str(data[3:taille_data-1]))  #ni chaine caractere
       
#        if data[2]==0x32: #affichage trame 2
#            num_jour=data[3]-0x30
            
#            Jours_semaine=['Lundi','Mardi','Mercredi','jeudi','Vendredi','samedi','Dimanche']
#            jour=Jours_semaine[num_jour-1]
           
#            if(data[4]==0x20):  #data 4 (0-3)
#                jour_date=data[5]-0x30
                
#            else:
#                jour_date=(data[4]-0x30)*10+(data[5]-0x30)
            
#            Mois=['Janvier','Fevrier','Mars','avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']  
#            if data[6]==0x20:
#                mois=Mois[data[7]-0x30-1]

#            else:
#                 mois=Mois[(data[6]-0x30)*10+(data[7]-0x30)-1]

#            anne=data[8:12].decode('ascii')

#            LDatadate.configure(text='On est le  '+   jour  + ' '+ str(jour_date)+' '+ mois+' '+ anne )  #mois n anne dh dlm string



#        if data[2]==0x33:  #affichage trame 3
#           heures=data[3:5].decode('ascii') #ou je peux faire data[[3,4]]
#           minutes=data[5:7].decode('ascii')
#           secondes=data[7:9].decode('ascii')
#           dixiemes=data[9:11].decode('ascii')  #9,10 just ecriture je
           
#           LDataheure.configure(text= heures+':'+minutes+':'+secondes+':'+dixiemes)
            
         
           
#        if data[2]==0x34:
            
#            temperature=data[3:8].decode('ascii')
            
#            LDatatemperature.configure(text='il fait'+' '+temperature)
#            if float(temperature)<0.0:
#                  LDatatemperature.configure(bg='cyan')
#            elif float(temperature)>20.0:
#                LDatatemperature.configure(bg='yellow')
#            else :
#                 LDatatemperature.configure(bg='white')
        
       
#        vitesse=0
#        if data[2]==0x35:
#            i=3
#            vitesse=0
#            Orientation=['N','NE','E','SE','S','SO','O','NO']

#            while(data[i]==0x3C):
#               i=i+1
#               vitesse=vitesse+10

#            vent=Orientation[data[i]-0x30]
          
#            LDatavent.configure(text='vent de vitesse'+' '+ str(vitesse) +' '+'noeuds'+' '+ vent+ "" )
            

#    fen1.after(1,ReadMeteo)


##interface graphique
#ser = serial.Serial()

#fen1 = Tk()
#fen1.geometry('600x400')
#fen1.title("Centrale Mto")
##label 
#LPort = Label(fen1,text='Ports:')
#LPort.grid(row=2,sticky=E)

##bouton liste port
#BListePorts = Button(fen1,text = 'List Ports',command = ListPort)
#BListePorts.grid(row=3,sticky=E)

##combo box
#selected_port = StringVar()
#CPort = ttk.Combobox(fen1, textvariable=selected_port)
#CPort['state'] = 'readonly'
#CPort.grid(row=4,sticky = E)


##button ouverture
#BOpenPort = Button(fen1,text = 'Open Port',command= OpenPort)
#BOpenPort.grid(row = 5,sticky = E)

##Label fermeture 
#LClose = Label(fen1,text = 'Port Closed',bg = 'red')
#LClose.grid(row = 1,column = 2,sticky = E)

##button fermeture
#BClosePort = Button(fen1,text='Close Ports',command = ClosePort)
#BClosePort.grid(row = 6,sticky=E)

#LInfo = Label(fen1,text='',bg = 'white')
#LInfo.grid(row = 7,column = 1,columnspan = 3)

##Button receive
#BReceive  =Button(fen1,text='read data',command = ReadDataPort)
#BReceive.grid(row=8,sticky = E)

##Label Data
#LData = Label(fen1,bg = 'yellow')
#LData.grid(row = 9,column=1,sticky = W)
#LDataStr = Label(fen1,bg = 'gray')
#LDataStr.grid(row = 10,column=1,sticky = W)
#LDataHexa = Label(fen1,bg = 'cyan')
#LDataHexa.grid(row = 11,column=1,sticky = W)

##Button emit
#BWrite = Button(fen1,text= 'Write Data',command = WriteData)
#BWrite.grid(row = 12,column = 1)

##Entre pour le texte  envoyer
#value = StringVar() 
#value.set("Texte")
#entree = Entry(fen1, width=30)
#entree.grid(row = 12,column = 2)

##bouton Meteo
#BMeteo=Button(fen1, text ='Mteo',command=ReadMeteo)
#BMeteo.grid(row = 1,sticky= E)

##labeltrame
#LDataTrame = Label(fen1,bg = 'grey')
#LDataTrame.grid(row = 13,column = 2,columnspan = 1)

##labelFirmware
#LDataFirmware = Label(fen1,bg = 'pink')
#LDataFirmware.grid(row = 14,column = 2,columnspan = 1)

##labeldate
#LDatadate= Label(fen1,bg = 'blue')
#LDatadate.grid(row = 15,column = 2,columnspan = 1)

##labelheure
#LDataheure= Label(fen1,bg = 'green')
#LDataheure.grid(row = 16,column = 2,columnspan = 1)

##labeltemperature
#LDatatemperature= Label(fen1,bg = 'orange')
#LDatatemperature.grid(row = 17,column = 2,columnspan = 2)

##labelVent
#LDatavent= Label(fen1,bg = 'orange')
#LDatavent.grid(row = 18,column = 2,columnspan = 2)

#fen1.mainloop()
