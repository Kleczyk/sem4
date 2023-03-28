import time
import numpy as np
def k3Init():
    import serial
    s = serial.Serial("COM3", 115200)
    # time.sleep(2)

    print(s.name)
    return s
def k3GetBateryState(s):
 s.write(b'V,5\r')
 serialString = s.readline()
 _ = s.read(1) #necessary to empty serial port
 serialString = serialString.decode("Ascii")
 serialString = serialString.strip() #remove the newline character from a string
 _ , bateryState, _ = serialString.split(",") #splits a string into a list
 print(f'Batery state: {bateryState}%\n')
 return bateryState
def k3ReadProximitySensors(s):
 MaxProximitiSignal = 4096
 res = False
 while not res:
    s.write(b'N\r')
    serialString = s.readline()
    _ = s.read(1) #necessary to empty serial port
    serialString = serialString.decode("Ascii")
    serialString = serialString.strip() #remove the newline character from a string
    proxSens = serialString.split(",") #splits a string into a list
    ProximitySensors = proxSens[1:-1] #remove first and last element
    ProximitySensors = np.array(list(map(int, ProximitySensors))) #convert string list to int list
    if len(ProximitySensors)==11:
        res = True
        # # some sensors need correction
        # # 1 - min val = 340, 4 - min val = 110, 7 - min val = 220 and 8 - min val = 120
        ProximitySensors[1] = (ProximitySensors[1]-2000)*(MaxProximitiSignal-0)/(MaxProximitiSignal2000)+0
        ProximitySensors[4] = (ProximitySensors[4]-1100)*(MaxProximitiSignal-0)/(MaxProximitiSignal1100)+0
        ProximitySensors[7] = (ProximitySensors[7]-100)*(MaxProximitiSignal-0)/(MaxProximitiSignal-100)+0
        ProximitySensors[8] = (ProximitySensors[8]-1000)*(MaxProximitiSignal-0)/(MaxProximitiSignal1000)+0
 return ProximitySensors
def k3ReadAmbientSensors(s):
 res = False
 while not res:
 s.write(b'O\r')
 serialString = s.readline()
 _ = s.read(1) #necessary to empty serial port
 serialString = serialString.decode("Ascii")
 serialString = serialString.strip() #remove the newline character from a string
 ambSens = serialString.split(",") #splits a string into a list
 AmbientSensors = ambSens[1:-1] #remove first and last element
 AmbientSensors = np.array(list(map(int, AmbientSensors))) #convert string list to int list
 if len(AmbientSensors)==11:
     res = True
 return AmbientSensors
def k3ReadSpeed(s):
 s.write(b'E\r')
 serialString = s.readline()
 _ = s.read(1) #necessary to empty serial port
 serialString = serialString.decode("Ascii")
 serialString = serialString.strip() #remove the newline character from a string
 Speed = serialString.split(",") #splits a string into a list
 Speed = Speed[1:] #remove first element
 Speed = list(map(int, Speed)) #convert string list to int list
 # print(f'Proximity sensors: {AmbientSensors}\n')
 return Speed
def k3ReadSoftwareVersion(s):
 s.write(b'B\r')
 serialString = s.readline()
 _ = s.read(1) #necessary to empty serial port
 serialString = serialString.decode("Ascii")
 serialString = serialString.strip() #remove the newline character from a string
 SV = serialString.split(",") #splits a string into a list
 SV = SV[1:-1] #remove first and last element
 SV = list(map(int, SV)) #convert string list to int list
 print(f'Software version stored in the robot\'s EEPROM is: {SV}\n')
 return SV
def k3SetSpeed(s,speed_motor_left,speed_motor_right):
 command=f'D,l{speed_motor_left},l{speed_motor_right}\r'
 s.write(str.encode(command))
 serialString = s.readline()
 _ = s.read(1) #necessary to empty serial port
 serialString = serialString.decode("Ascii")
 serialString = serialString.strip() #remove the newline character from a string
 # return serialString
def k3Stop(s):
 k3SetSpeed(s,0,0)

def k3ConfigureSpeedProfileController(s,max_speed,acceleration):
 # At the reset, these parameters aree set to standard values:
 # max_speed to MaxSpeed, acc to 64
 command=f'J,d{max_speed},{acceleration}\r'
 s.write(str.encode(command))
 _ = s.readline()
 _ = s.read(1) #necessary to empty serial port

def k3SetPosition(s,position_motor_left,position_motor_right):
 # Set the 32 bit position counter of the two motors. The unit is the pulse
 # each one corresponds to 0,047mm
 command=f'I,l{position_motor_left},l{position_motor_right}\r'
 s.write(str.encode(command))
 serialString = s.readline()
 _ = s.read(1) #necessary to empty serial port
 serialString = serialString.decode("Ascii")
 serialString = serialString.strip() #remove the newline character from a string
 # return serialString

def k3SetTargetPosition(s,target_position_motor_left,target_position_motor_right,acceleration):
 positioning_accuracy = 0.01
 if acceleration:
    # Set a position to be reached. The move will be performed
    # with three phase, a acceleration to reach the maximum
    # speed, a constant speed and a deceleration phase before the
    # finish position. The unit is the pulse, each one corresponds
    # to 0,047 mm with old firmware, 0.031 mm with new firmware
    command=f'F,l{target_position_motor_left},l{target_position_motor_right}\r'
 else:
    # Set a position to be reached. The move will be performed
    # without acceleration and deceleration. The unit is the pulse,
    # each one corresponds to 0,047 mm with old firmware, 0.031
    # mm with new firmware
    command=f'P,l{target_position_motor_left},l{target_position_motor_right}\r'
    s.write(str.encode(command))
    Position = k3ReadPosition(s)
 if target_position_motor_left==0:
    tpl = 1 # to avoid divide by 0
 else:
    tpl = target_position_motor_left
 if target_position_motor_right==0:
      tpr = 1
 else:
    tpr = target_position_motor_right
 while ( (abs((Position[0]-tpl)/tpl)) > positioning_accuracy) & ( (abs((Position[1]-tpr)/tpr)) > positioning_accuracy):
    Position = k3ReadPosition(s) # read position until target one is reached
    time.sleep(0.02)
    k3Stop(s)
 return Position
def k3ReadPosition(s):
 res = False
 while not res:
    s.write(b'R\r')
    serialString = s.readline()
    _ = s.read(1) #necessary to empty serial port
    serialString = serialString.decode("Ascii")
    serialString = serialString.strip() #remove the newline character from a string
    Position = serialString.split(",") #splits a string into a list
    Position = Position[1:] #remove first element
    Position = list(map(int, Position)) #convert string list to int list
    if len(Position)==2:
        res = True
 return Position
def k3Braitenberg(s,mode):
 #mode==0 - Infrared sensors
 #mode==1 - Ultrasonic sensors
 #mode==2 - Stop Braitenberg mode
 command=f'A,{mode}\r'
 s.write(str.encode(command))
 _ = s.readline()
 _ = s.read(1) #necessary to empty serial port

def k3ReadProximitySensorsLoop(s):
 res = False
 iter = 0
 while not res:
    sens = k3ReadProximitySensors(s)
    print(sens)
    iter += 1
    if iter==1000:
        res = True

def k3SetProgrammableLed(s,LED,State):
 command=f'K,{LED},{State}\r'
 s.write(str.encode(command))
 _ = s.readline()
 _ = s.read(1) #necessary to empty serial port