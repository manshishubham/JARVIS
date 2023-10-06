import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter.filedialog import *
import pyautogui
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as w
import smtplib
from random import randint
from pytube import YouTube

print("Intializing Your Jarvis AI Desktop Assistant")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Hello, Good Morning !")
    
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
    
    else:
        speak("Hello, Good Evening")
    
    speak("I am Jarvis, How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def game():
    l = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]
    computer = l[randint(0,5)]
    player = False

    while player == False:
        speak("Type - Rock, Paper or Scissors?")
        player = input("Choose - Rock, Paper, Scissors? ")
        speak(f"\nYou chose {player}, computer chose {computer}.\n")
        print(f"\nYou chose {player}, computer chose {computer}.\n")
        if player == computer:
            speak("Tie!")
            print("Tie!")
        elif player == "Rock" or player == "rock":
            if computer == "Paper" or computer == "paper":
                speak(f"You lose! {computer}, covers {player}")
                print("You lose!", computer, "covers", player)
            else:
                speak(f"You win!, {player}, smashes {computer}")
                print("You win!", player, "smashes", computer)

        elif player == "Paper" or player == "paper":
            if computer == "Scissors" or computer == "scissors":
                speak(f"You lose! {computer}, cut {player}")
                print("You lose!", computer, "cut", player)
            else:
                speak(f"You win! {player}, covers {computer}")
                print("You win!", player, "covers", computer)

        elif player == "Scissors" or player == "scissors":
            if computer == "Rock" or computer == "rock":
                speak(f"You lose..., {computer}, smashes, {player}")
                print("You lose...", computer, "smashes", player)
            else:
                speak(f"You win! {player}, cut {computer}")
                print("You win!", player, "cut", computer)
        else:
            speak("Check your spelling!\n")
            print("Check your spelling!\n")
        
        speak("Want to play again? Type Yes or No")
        again = input("\nWant to play again? ")

        #if want to play again
        if again == "Yes" or again == "yes":
            player = False
            computer = l[randint(0,2)]

        #if wants to quit
        else:
            player = True

def recorder():
    # background
    root = Tk()
    root.geometry("400x400+400+80")
    root.resizable(False, False)
    root.title("My Voice Recorder")
    root.configure(background="#F5F5F5")

    # record function
    def Record():
        freq = 44100
        dur = int(duration.get())
        recording = sound.rec(dur*freq,
                            samplerate = freq, channels = 2)
        try:
            temp = int(duration.get())
        except:
            print("Please enter the right value")

        while temp>0:
            root.update()
            time.sleep(1)
            temp=temp-1

            if(temp==0):
                messagebox.showinfo("Time Countdown","Time's up")
            Label(text=f"{str(temp)}", font = "perpetua 25", width = 4, background = "#F5F5F5").place(x=160, y=320) 
        
        sound.wait
        write("Recording.wav",freq,recording)

    #icon
    image_icon = PhotoImage(file = "image.png")
    root.iconphoto(False, image_icon)

    #logo
    photo = PhotoImage(file= "image.png")
    myimage = Label(image=photo)
    myimage.pack(padx=5,pady=25)

    #defining labels
    Label(text="Voice Recorder", font = "forte 28 bold", background = "#F5F5F5", fg = "navy").pack()

    duration = StringVar()

    Label(text = "Enter time in seconds ", font = "perpetua 18 italic", background = "#F5F5F5", fg= "navy").pack()
    entry = Entry(root, textvariable = duration, font = "Times 15 bold", width = 20).pack()

    record = Button(root, font="perpetua 18 bold", text = "Record", bg = "#0A1172", fg = "white", border = 0, command= Record).pack(pady = 25)

    #running mainloop
    root.mainloop()

def yt_down():
    speak("Copy link here...")
    link = input("Link = ")
    yt_1 = YouTube(link)

    print(yt_1.title)
    print(yt_1.thumbnail_url)
    videos = yt_1.streams.all()
    vid = list(enumerate(videos))
    for i in vid:
        print(i)

    strm = int(input("Enter: "))
    videos[strm].download()
    speak("Successfully downloaded")
    print("Successfully")      

def ss():
    root = Tk()
    canvas1 = tk.Canvas(root, width = 200, height = 200)
    canvas1.pack()

    def takeSs():
        mySs = pyautogui.screenshot()
        s_path = asksaveasfilename()
        mySs.save(s_path+"_screenshot.png")
    myButton = tk.Button(text = "Take Screenshot", command = takeSs, font=10)
    canvas1.create_window(100,100,window=myButton)
    root.mainloop()

def sendEmail(to, content):
    server  = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manshishubham09@gmail.com', 'password')

    '''in order to do so we have to go on google nd allow less secure app section "On"
    To help keep your account secure, from May 30, 2022,Google no longer supports
    the use of third-party apps or devices which ask you to sign in to your Google
    Account using only your username and password.'''

    server.sendmail('manshishubham09@gmail.com',to, content)
    server.close()

if __name__ == "__main__":
    #speak("I am a good boy..!!")
    speak("Intializing Your Jarvis A I Desktop Assistent....")
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "open my ide" in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif "email to me" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "manshishubham@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry, email can't be sent")
        
        elif "game" in query:
            game()

        elif "record sound" in query:
            recorder()

        elif "download" in query:
            yt_down()
        
        elif "screenshot" in query:
            ss()
                    
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif "stop" in query:
            speak("Ok see you soon. Have a great time")
            exit()
