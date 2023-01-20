#!/usr/bin/env pybricks-micropython
import pybricks.tools as pt
from pybricks.ev3devices import ColorSensor, Motor, TouchSensor  # type: ignore
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Direction, Port
from pybricks.robotics import DriveBase

# kostka
ev3 = EV3Brick()    

# motory
levy_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
pravy_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)

# senzory
color_levy = ColorSensor(Port.S2)
color_uprostred = ColorSensor(Port.S3)
color_vpravo = ColorSensor(Port.S1)

color_navigacni = ColorSensor(Port.S4)

# drivebase
robot = DriveBase(levy_motor, pravy_motor, 54, 87)

def sleduj_caru():
    global cilova_hodnota_sledovani_cary, konstanta_p, zakladni_rychlost_pro_PID, cl_navigacni
    # P formula
    cl_navigacni = color_navigacni.reflection()
    error_vuci_chtenemu = cl_navigacni - cilova_hodnota_sledovani_cary
    error_vuci_chtenemu *= -1
    jak_moc_se_otocit = konstanta_p * error_vuci_chtenemu
    # vykonej
    robot.drive(zakladni_rychlost_pro_PID, jak_moc_se_otocit)  # type: ignore
def jsem_v_cili():
    # ev3.speaker.set_volume(100)
    # ev3.speaker.beep(440, 200)
    pt.wait(10)
    exit()

def otoc_uturn():
    print("Uturn")
    ## vylaď
    robot.turn(180)
def otoc_doprava():
    print("right")
    ## vylaď
    robot.straight(20)
    robot.turn(92)
def otoc_doleva():
    print("left")
    ## vylaď
    robot.straight(20)
    robot.turn(-92)
def otoc_dopredu():
    # pro přeskakování rovných křižovatek
    print("strght")
    robot.straight(30)

def precti_senzory_s_posunem():
    global cl_vlevo_vepredu, cl_vpravo_vepredu, cl_vprostred_vepredu
    print("čtu vepředu")
    ## vylaď
    robot.straight(30)

    cl_vlevo_vepredu = color_levy.reflection()
    cl_vprostred_vepredu = color_uprostred.reflection()
    cl_vpravo_vepredu = color_vpravo.reflection()
def je_to_bila(vstupni_hodnota):
    global threshold_pro_bilou, threshold_pro_cernou

    if vstupni_hodnota > threshold_pro_bilou: return True
    elif vstupni_hodnota < threshold_pro_cernou: return False
    else: return None
def precti_senzory_pod_sebou():
    global cl_vlevo
    global cl_vpravo
    global cl_uprostred

    cl_vlevo = color_levy.reflection()
    cl_uprostred = color_uprostred.reflection()
    cl_vpravo = color_vpravo.reflection()



class policko():
    # None - nevíme, -1 - cesta není, 0 cesta je, neprošli, 1 - c je, jednou p, 2 - cesta je, prošli 2 krát
    def __init__(self):
        self.nahoru = None
        self.doprava = None
        self.doleva = None
        self.dolu = None

    def je_prazdny(self):
        if self.nahoru == None and self.doprava == None and self.dolu == None and self.doleva == None:
            return True
        else:
            return False
    
    def nastav_podle_krizovatky(self, krizov):
        global moznosti_krizovatky

        moznosti = moznosti_krizovatky.get(krizov) # type: ignore
        print(moznosti, krizov)

        self.nahoru = moznosti[0]     # type: ignore
        self.doprava = moznosti[1]    # type: ignore
        self.dolu = moznosti[2]     # type: ignore
        self.doleva = moznosti[3]       # type: ignore

        strung = str([self.nahoru, self.doprava, self.dolu, self.doleva]) # type: ignore
        print(strung)

    def prijezd(self, smer):
        if smer == 0: self.dolu += 1          # type: ignore
        if smer == 1: self.doleva += 1        # type: ignore  
        if smer == 2: self.nahoru += 1        # type: ignore
        if smer == 3: self.doprava += 1       # type: ignore
## odřřádkování
    def odjezd(self, smer):
        if smer == 0: self.nahoru += 1      # type: ignore
        if smer == 1: self.doprava += 1     # type: ignore  
        if smer == 2: self.dolu += 1        # type: ignore
        if smer == 3: self.doleva += 1      # type: ignore

    def print_all(self):
        strung = str([self.nahoru, self.doprava, self.dolu, self.doleva]) # type: ignore
        strung = strung.replace("None", ".")
        strung = strung.replace("[", "")
        strung = strung.replace("]", "")
        strung = strung.replace("-1", "X")
        strung = strung.replace(",", "")
        strung = strung.replace(" ", "")
        strung += " "
        return strung

    def get_smer(self):
        print("\n")
        lst = [self.nahoru, self.doprava, self.dolu, self.doleva]
        print(lst)
        for x in range(len(lst)):
            if lst[x] == -1:
                lst[x] = 3
        kam = lst.index(min(lst)) # type: ignore
        print(kam)
        print("\n")
        return kam
        
        
    def gnahoru(self):
        return self.nahoru
    def gdoprava(self):
        return self.doprava
    def gdoleva(self):
        return self.doleva
    def gdolu(self):
        return self.dolu
    

    def nnahoru(self, x):
        self.nahoru = x
    def ndoprava(self, x):
        self.doprava = x
    def ndolu(self, x):
        self.dolu = x
    def ndoleva(self, x):
        self.doleva = x



pozice_x_y = [16,16]
otoceni_vuci_startu = 0

cis = 0
najeto_na_kolech = []
najeto_na_kolech2 = []

konstanta_p = 2.5
zakladni_rychlost_pro_PID = 75

threshold_pro_bilou = 40
threshold_pro_cernou =  20
cilova_hodnota_sledovani_cary = 33

co100_cislo_tisknu_pebug = 0
cl_navigacni = color_navigacni.reflection()

moznosti_krizovatky = {
    "┌" : [-1, 0, 0,-1],
    "┐" : [-1,-1, 0, 0],
    "┘" : [ 0,-1,-1, 0],
    "└" : [ 0, 0,-1,-1],
    "├" : [ 0, 0, 0,-1],
    "┤" : [ 0,-1, 0, 0],
    "┬" : [-1, 0, 0, 0],
    "┴" : [ 0, 0,-1, 0],
    "┼" : [ 0, 0, 0, 0],
    "▫" : [ 0, 0, 0, 0]
}



precti_senzory_pod_sebou()
precti_senzory_s_posunem()

while True:
    precti_senzory_pod_sebou()
    sleduj_caru()
    # if check() == "out":
    #     break


