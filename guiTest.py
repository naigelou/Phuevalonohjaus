import random
import time

from phue import Bridge

# VAIHDA OIKEA IP OSOITE
b = Bridge('192.168.1.32')
b.connect()
lights = b.lights

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
# Get the bridge state (This returns the full dictionary that you can explore)
#print(b.get_api())
# Print light names
#for l in lights:
#    print(l.name)

class ValoVarit:
    def __init__(self, name, xy):
        self.name = name
        self.xy = xy

violetti = ValoVarit("violetti", [0.3645,0.2128])
indigo = ValoVarit("indigo", [0.2485,0.0917])
sininen = ValoVarit("sininen", [0.167,0.04])
vihrea = ValoVarit("vihreä", [0.1439, 0.7999])
keltainen = ValoVarit("keltainen", [0.5071, 0.4712])
oranssi = ValoVarit("oranssi", [0.5567,0.4091])
punainen = ValoVarit("punainen", [0.675,0.322])

SATEENKAARI = [
    violetti,
    indigo,
    sininen,
    vihrea,
    keltainen,
    oranssi,
    punainen]

aakkoset = {'A':'.-', 'B':'-...','C': '-.-.', 'D': '-..','E': '.', 'F': '..-.','G': '--.','H': '....','I': '..','J': '.---',
'K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-',
'V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','Å': '.--.-','Ä': '.-.-','Ö': '---.','Ü': '..--'}

# sleep time is in seconds.
# Sleep time is longer than transition time, so we can enjoy
SLEEP_TIME = 2
# transition time is in deca seconds
TRANSITION_TIME = 1
MAX_BRIGHTNESS = 254



def paalle(id):
    print("Asetetaan valo", id, "tilaan", True)
    b.set_light(id,'on', True)
    b.set_light(id, 'bri', 254)

def pois(id):
    print("Asetetaan valon", id, "kirkkaus arvoon", 1)
    b.set_light(id, 'bri', 1)
#    b.set_light(id,'on', False)

def laita_valot_paalle(id):
    b.set_light(id,'on', True)
    b.set_light = TRANSITION_TIME
    b.set_light = MAX_BRIGHTNESS
def disco(id):
    b.set_light(id,'on', True)
    b.set_light(id,'bri',254)
#Muista vaihtaa lights oikeisiin valo arvoihin!
def kaikkiPaalle():
    lights = [1]
    for light in lights:
        paalle(light)
#Muista vaihtaa lights oikeisiin valo arvoihin!
def kaikkiPois():
    lights = [1]
    for light in lights:
        pois(light)
def sateenkaari():
    lights=[1]
    for light in lights:
        laita_valot_paalle(light)

#EI EHKÄ TOIMI NÄIN
#Muista vaihtaa lights oikeisiin valo arvoihin!
def disco_valot():
    lights=[1]
    for light in lights:
        #TÄMÄ PITÄÄ EHKÄ OLLA MYÖHEMMIN NIINKUIN SATEENKAARESSA
        disco(light)

def morsetus(morse):
    for kirjain in morse:
        if kirjain == ' ':
            time.sleep(2)
            continue
        iso = kirjain.upper()
        pilkkukoko = aakkoset[iso]
        for pilkut in pilkkukoko:
            if pilkut == '.':
                kaikkiPaalle()
                time.sleep(0.5)
                kaikkiPois()
                time.sleep(1)

            if pilkut == '-':
                kaikkiPaalle()
                time.sleep(1)
                kaikkiPois()
                time.sleep(1)



komento = " "
if(komento == "ON"):
    kaikkiPaalle()
elif(komento == "SATEENKAARI"):
    while True:
        for color in SATEENKAARI:
            for light in lights:
                light.xy = color.xy
                print ("%s vaihtuu %s") % (light.name, color.name)
            time.sleep(SLEEP_TIME)
        laita_valot_paalle()
elif (komento == "DISKO"):
    for light in lights:
        light.xy=[random.random(),random.random()]
        disco_valot()
elif (komento == "OFF"):
    kaikkiPois()
elif (komento == "MORSE"):
    morseinput = input("Anna morsetettava sana ")
    morsetus(morseinput)

# if __name__ == '__main__':
#     main()