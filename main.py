import pyttsx3
import time
import PySimpleGUI as sg
import threading

global start_time
start_time = time.time()

def counter_thread(window):

    start_time = time.time()
    scout = int(values["-scout_in-"])
    smd_start = int(values["-smd_start_in-"])
    smd_warning = int(values["-smd_warning_in-"])
    engine.say("Nuclear Umbrella started...")
    engine.runAndWait()
    time.sleep(scout * 60)
    print(time.time() - start_time)
    engine.say(str(scout) + " minutes passed: Don't be blind, scout!")
    engine.runAndWait()
    time.sleep(smd_start * 60)
    engine.say(str(smd_start) + " minutes elapsed, reminder: Start to build nuke defense!")
    engine.runAndWait()
    time.sleep(smd_start * 60)
    engine.say(str(smd_start) + " minutes elapsed, reminder: Start to build nuke defense!")
    engine.runAndWait()

if __name__ == '__main__':

    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[0].id)


    sg.theme('BluePurple')

    layout = [[sg.Text('Scout warning after (mins):'), sg.Text(size=(4,1), key='-scout-')], [sg.Input(size=(4,1),key='-scout_in-',default_text="10")],
              [sg.Text('Start building SMD (mins):'), sg.Text(size=(4,1), key='-smd_start-')], [sg.Input(size=(4,1),key='-smd_start_in-',default_text="20")],
              [sg.Text('SMD be ready warning (mins):'), sg.Text(size=(4, 1), key='-smd_warning-')],[sg.Input(size=(4, 1), key='-smd_warning_in-',default_text="25")],
              [sg.Text('Time elapsed:'), sg.Text(size=(4, 1), key='-timer-')],
              [sg.Button('Start'), sg.Button('Exit')]]

    sg.Input()

    window = sg.Window('FAF Nuclear Umbrella Clicker',layout, size=(400,300))

    while True:  # Event Loop
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Start':
            # Update the "output" text element to be the value of "input" element

            counter_thread_instance = threading.Thread(target=counter_thread, args=(window,), daemon=True)
            counter_thread_instance.start()
            time.sleep(1)
        time_elapsed = int(time.time() - start_time)
        window['-timer-'].update('{:02d}:{:02d}.{:02d}'.format((time_elapsed // 100) // 60,
                                                        (time_elapsed // 100) % 60,
                                                        time_elapsed % 100))

    window.close()