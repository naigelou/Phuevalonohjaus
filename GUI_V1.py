import PySimpleGUI as sg
from guiTest import *

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Bridgen IP:'), sg.InputText('')],
            [sg.Text('Valon ID (Mitä valoa haluat ohjata?)'), sg.InputText('')],
            [sg.Text('Valitse nappuloista toiminto.(Muista lisätä sana morsetukseen)')],
            [sg.Text('Anna sana morsetukseen'), sg.InputText('',key='morsetussana'),sg.Button('MORSE')],
            [sg.Button('ON'), sg.Button('OFF'),sg.Button('SATEENKAARI'), sg.Button('DISKO'),sg.Button('Peruuta')
            ,sg.Button('HELP')] ]

# Create the Window
window = sg.Window('Philips hue ohjaus', layout)
event, values = window.Read()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Peruuta': # if user closes window or clicks cancel
        break
    if event == 'ON':
        kaikkiPaalle()
    if event == 'OFF':
        kaikkiPois()
    if event == 'HELP':
        sg.Popup("Bridgen IP (xxx.xxx.x.xx), Valon ID:löytyy valoista.Nappien toiminnot: ON = valo päälle(kirkkaimmalle), OFF = Valo himmeimmälle mahdolliselle,DISKO = Satunnaisessa järjestyksessä eri värit, SATEENKAARI = Sateenkaaren värit läpi, MORSE = Valo morsettaa annetun sanan",keep_on_top=True)
    if event == 'MORSE':
        laatikonsana = values['morsetussana']
        morsetus(laatikonsana)

    

window.close()