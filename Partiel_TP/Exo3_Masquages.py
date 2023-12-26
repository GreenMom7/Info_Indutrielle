# -*- coding:Latin-1 -*-


def AnalyseRegister(valRegistre):
    bit7 = (valRegistre & 0x80) >> 7
    bit56 = (valRegistre & 0x60) >> 5
    bit4 = (valRegistre & 0x10) >> 4
    bit3 = (valRegistre & 0x08) >> 3
    bit2 = (valRegistre & 0x04) >> 2
    bit1 = (valRegistre & 0x02) >> 1
    bit0 = (valRegistre & 0x01) 
    
    if bit7 == 1:
        print(f'- coluer')
    else :
        print(f'- noir et blanc')
        
    if bit56 == 0:
        print(f'- 480*640')
    elif bit56 == 1:
        print(f'- 1920*1080')
    elif bit56 == 2:
        print(f'- 3840*2160')
    elif bit56 == 3:
        print(f'- 7680*4320')
     
    if bit4 == 1:
        print(f'- infrarouge active')
    else:
        print(f'- infrarouge desactive')
        
    frequence = bit3*2+bit2*10+bit1*50
    print(f'- frequence = {frequence} Hz')
    
    if bit0 == 1 :
        print(f'- version 1')
    else :
        print(f'- version 0')
        
def ConfigResolution(val, valRegister):
    newValregistre = valRegister
    if val == 1 :
        newValregistre = valRegister & 0x9F
    elif val == 2 :
        newValregistre = (valRegister & 0xBF)|0x20
    elif val == 3 :
        newValregistre = (valRegister & 0xDF)|0x40
    elif val == 2 :
        newValregistre = valRegister |0x60
     
    return newValregistre

VAL = 0xE3   
AnalyseRegister(VAL)
newConfig = ConfigResolution(2,VAL)
print(f'nouvelle configuration : ')
AnalyseRegister(newConfig)

