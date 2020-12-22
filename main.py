import pyttsx3
import time
import PySimpleGUI as sg
import threading

global start_time
start_time = time.time()

def counter_thread(window):

    start_time = time.time()
    scout_min = int(values["-scout_in-"])
    scout_sec = scout_min * 60
    smd_start_min = int(values["-smd_start_in-"])
    smd_start_sec = smd_start_min * 60
    smd_warning_min = int(values["-smd_warning_in-"])
    smd_warning_sec = smd_warning_min * 60
    engine.say("Nuclear Umbrella started...")
    engine.runAndWait()

    #first wait: Scouting
    time.sleep(scout_sec)
    elapsed_time_min = int((time.time() - start_time) / 60)
    engine.say(str(elapsed_time_min) + " minutes have passed: Don't be blind, make sure you scout!")
    engine.runAndWait()

    #second wait: start build SMD
    elapsed_time_min = int((time.time() - start_time) / 60)
    time.sleep((smd_start_min - elapsed_time_min)*60 )
    elapsed_time_min = int((time.time()-start_time)/60)
    engine.say(str(elapsed_time_min) + " minutes elapsed, reminder: Start building the nuclear missile defense!")
    engine.runAndWait()

    #third wait: SMD must be ready
    time.sleep((smd_warning_min - elapsed_time_min)*60)
    elapsed_time_min = int((time.time() - start_time) / 60)
    engine.say(str(elapsed_time_min) + " minutes passed, WARNING: Must have SMD ready, with missile built! There is a high risk of rain!")
    engine.runAndWait()

if __name__ == '__main__':

    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[2].id)


    sg.theme('BluePurple')

    layout = [[sg.Text('Scout warning after (mins):'), sg.Text(size=(4,1), key='-scout-')], [sg.Input(size=(4,1),key='-scout_in-',default_text="10")],
              [sg.Text('Start building SMD (mins):'), sg.Text(size=(4,1), key='-smd_start-')], [sg.Input(size=(4,1),key='-smd_start_in-',default_text="20")],
              [sg.Text('SMD be ready warning (mins):'), sg.Text(size=(4, 1), key='-smd_warning-')],[sg.Input(size=(4, 1), key='-smd_warning_in-',default_text="25")],
              [sg.Text('Time elapsed:'), sg.Text(size=(10, 1), key='-timer-')],
              [sg.Button('Start'), sg.Button('Exit')]]

    sg.Input()

    window = sg.Window('FAF Nuclear Umbrella Timer',layout, size=(400,300))

    while True:  # Event Loop
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Start':
            # Update the "output" text element to be the value of "input" element

            counter_thread_instance = threading.Thread(target=counter_thread, args=(window,), daemon=True)
            counter_thread_instance.start()
        time_elapsed = int(time.time() - start_time)
        window['-timer-'].update('{:02d}:{:02d}.{:02d}'.format((time_elapsed // 60) // 60, (time_elapsed // 60) % 60, time_elapsed % 60))

        #window['-timer-'].update(str(time_elapsed / 60 /60) +":"+str(time_elapsed / 60)+":"+str(time_elapsed))
    window.close()