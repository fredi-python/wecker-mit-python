import PySimpleGUI as sg
import datetime
import playsound

layout = [  [sg.Text("die stunde:")],
            [sg.Input()],
            [sg.Text("die minute:")],
            [sg.Input()],
            [sg.Button('wecker stellen')] ]


window = sg.Window('Wecker', layout)


event, values = window.read()

print('Gut', "der wecker ist auf", values[0],":", values[1], "gestellt")

window.close()

while True:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute


    if hour == int(values[0]) and minute == int(values[1]):
        playsound.playsound('sound.wav')
