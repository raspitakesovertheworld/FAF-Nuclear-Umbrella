import pyttsx3
import time
import PySimpleGUI as sg
import tkinter



if __name__ == '__main__':

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    sg.theme('BluePurple')

    layout = [[sg.Text('Scout warning after (mins):'), sg.Text(size=(4,1), key='-scout-')], [sg.Input(size=(4,1),key='-scout_in-',default_text="10")],
              [sg.Text('Start building SMD (mins):'), sg.Text(size=(4,1), key='-smd_start-')], [sg.Input(size=(4,1),key='-smd_start_in-',default_text="20")],
              [sg.Text('SMD be ready warning (mins):'), sg.Text(size=(4, 1), key='-smd_warning-')],[sg.Input(size=(4, 1), key='-smd_warning_in-',default_text="25")],
              [sg.Button('Start'), sg.Button('Exit')]]

    sg.Input()

    window = sg.Window('FAF Nuclear Umbrella Clicker',layout, size=(400,300))

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        scout = int(values["-scout_in-"])
        smd_start = int(values["-smd_start_in-"])
        smd_warning = int(values["-smd_warning_in-"])

        print(scout)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Start':
            # Update the "output" text element to be the value of "input" element
            #window['-OUTPUT-'].update(values['-IN-'])

            start_time =time.time()

            engine.say("Nuclear Umbrella started...")
            engine.runAndWait()
            time.sleep(scout*60)
            print(time.time()-start_time)
            engine.say(str(scout)+" minutes passed: Don't be blind, scout!")
            engine.runAndWait()
            time.sleep(smd_start*60)
            engine.say(str(smd_start)+" minutes elapsed, reminder: Start to build nuke defense!")
            engine.runAndWait()
            time.sleep(smd_start * 60)
            engine.say(str(smd_start) + " minutes elapsed, reminder: Start to build nuke defense!")
            engine.runAndWait()

    window.close()