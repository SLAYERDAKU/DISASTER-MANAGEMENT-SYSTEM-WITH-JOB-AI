import solutions as sol
import helpline
from tkinter import messagebox
import tkinter as tk
import pyttsx3

nat_dis = ['E : Earthquake', 'F : Flood',
           'L : Landslide', 'E : Errosion', 'U : Unemployment']


# GUI
tk.Tk().withdraw()
messagebox.showinfo('Welcome', 'Welcome to the Disaster Management System')


# -----------------------------------------initialize the engine--------------------------------------------
engine = pyttsx3.init()     # initialise the engine

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   # set the voice

newVoiceRate = 140
engine.setProperty('rate', newVoiceRate)    # set the speed rate

# text to speech


def speak(text):
    # save_logs('Jarvis : {}'.format(text), 'info')
    engine.say(text)
    engine.runAndWait()


speak("Do you want to get a job? ")
choice = input('Do you want to get a job? : ')

# -------------------------------------------------------------------------------------------------------


def print_results(inp):
    for i in range(1, 3):
        print(inp[i])
        speak(text=inp[i])
    speak('Do you want to see more? ')
    user_inp = input('Do you want to see more? (y/n) : ')
    if user_inp == 'y':
        for j in range(3, len(inp)+1):
            print(inp[j])
            speak(text=inp[j])


for i in nat_dis:
    print(i)
speak('Choose what happened with you?')
user_inp = (input('Choose what happened with you? (enter initials): ')).upper()
helpline.helpline_number_acc_to_state()

if user_inp == 'E':
    print_results(sol.earthquake())
elif user_inp == 'F':
    print_results(sol.flood())
elif user_inp == 'L':
    print_results(sol.landside())
elif user_inp == 'U':
    print_results(sol.unemployment())
    choice = input(speak('Do you want to get a job? (y/n) : '))
    if choice == 'y':
        exec(open("Swarnim_unemployment.py").read())
    else:
        print('Thank you for using our service')

else:
    print('Invalid input')


print('\n Hold tight, we will provide help ASAP')
