import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import pyjokes
import pyautogui
import time
import wolframalpha
import winshell
import os, sys, subprocess ,datetime
import cv2
import pyzbar.pyzbar as pyz 
import requests
import json
from json import *
from urllib.request import urlopen
from PIL.ImageChops import screen
import smtplib
from email.message import EmailMessage
app = wolframalpha.Client(" XG354P-EAGP2X6822")
#Text To Speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[-1].id)

def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()

def wish():# wishes us based on time
    hour = int(datetime.datetime.now().hour)
    tt = datetime.datetime.now().strftime ("%I:%M:%p")
    if hour >= 0 and hour<12:
        speak("good morning boss , its")
        print(tt)
        speak(tt)
    elif hour>=12 and hour<16:
        speak("good afternoon sir , its")
        print(tt)
        speak(tt)
    elif hour>=16 and hour<20:
        speak("good afternoon sir , its ") 
        print(tt)
        speak(tt)
    else:
        speak(f"good night sir , its") 
        print(tt) 
        speak(tt)
    speak("how can i help you")


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ullhasykumar007@gmail.com', 'ullhas1947')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def get_email_info():
    speak('To Whom you want to send email')
    name = input()
    receiver = [name]
    print(receiver)
    speak('What is the subject of your email?')
    subject = takecom()
    speak('Tell me the text in your email')
    message = takecom()
    send_email(receiver, subject, message)
    speak('your email has been send boss')

 
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}")
    except Exception:                #For Error handling
        print("Unable to Recognize your voice.") 
        return "none"
    return text


if __name__ == "__main __":
    wish()
    while True:
        query = takecom().lower()

        if "wikipedia" in query:
            speak("searching details....Wait")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif"send email" in query:
            speak("just a secound boss")
            get_email_info()

        elif 'open weather' in query or "weather" in query:
            webbrowser.open("https://www.bbc.com/weather/1262321")#opens bbc weather website and tells weather of mysore
            speak("okey sir")
            speak("opening in web boss")

        elif 'open youtube' in query or "open video online" in query:# opens youtube
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
         

        elif 'open google' in query:
            webbrowser.open("https://www.google.com") #opens google
            speak("opening google")
        elif 'close google' in query:#opens github app
            webbrowser.exit("https://www.google.com")

        elif 'open my website' in query or "open my web page" in query :#opens my first website
            webbrowser.open("file:///E:/CSS%20in%20HTML/new.html")
            speak("opening you website sir") 

        elif 'open between us' in query:#opens between us
            webbrowser.open("https://betweenus.in/default.aspx")
            speak("opening between us")
        
        elif 'open gmail' in query:#opens my gmail
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
             
        elif 'open amazon' in query or 'shop online' in query:#opens my amazon account
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'music from pc' in query or "music" in query or "play music" in query:#plays music from the directery
            speak("ok i am playing music")
            music_dir = 'C:\\Users\\ULLHASYKUMAR\\Music\\Playlists'
            musics = os.listdir(music_dir)
            speak("enjoy boss")
            os.startfile(os.path.join(music_dir,musics[0]))
            exit()

        elif 'video from pc' in query or "video" in query:#plays video from the directery
            speak("ok i am playing videos")
            video_dir = 'Videos'
            videos = os.listdir(video_dir)
            speak("enjoy boss")
            os.startfile(os.path.join(video_dir,videos[0])) 
            exit()
        
        elif 'make a document' in query:
            speak("preparing document")
            fh = open('jarvis note.txt','w')
            speak("what should i write in the document")
            ans = takecom()
            fh.write(ans)
            speak("document has been made")

        elif 'continue typing' in query:
           speak("preparing document")
           speak("what should i write in the document")
           ans = takecom()
           fh.write(ans)
           fh.close
           speak("document has been made")
        
        elif 'stop listening' in query:
            speak("for how many seconds do you want me to stop listening your commands")
            ans =int(takecom())

            print(ans)
            time.sleep(ans)
            speak("jarvis is back to work boss ")

        elif 'search in youtube' in query:
            try:
                    speak("What should I search?")
                    search = takecom()
                    speak("searching in youtube")


                    webbrowser.open("https://www.youtube.com/results?search_query="+ search)
            except Exception as e:
                print(e)
                speak("sorry search was incomplete")
            
        elif 'search google' in query:
            try:
                speak(" yes boss What should I search?")
                google = takecom()
                speak("searching google")
                webbrowser.open("https://www.google.com/?#q="+ google)
            except Exception as e:
                print(e)
                speak("sorry search was incomplete")

            
        elif'the time'in query:#tells us the time in 12 hours format
            srttime = datetime.datetime.now().strftime("%I:%M:%p")
            speak(srttime)

        elif 'open zoom' in query:#opens zoom app
            codePath = "C:\\Users\\ULLHASYKUMAR\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)
            speak("opening zoom meeting, boss")
        
        elif 'close zoom' in query:#opens github app
            os.system("taskkill /f /im Zoom.exe")

        elif 'open github' in query:#opens github app
            codePath = "C:\\Users\\ULLHASYKUMAR\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(codePath)

        elif 'close github' in query:#opens github app
            os.system("taskkill /f /im GitHubDesktop.exe")


        elif 'open vs code' in query or "visual studio code" in query or "open code" in query:#opens VS code app
            codePath = "C:\\Users\\ULLHASYKUMAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'close vs coce' in query:#opens github app
            os.system("taskkill /f /im Code.exe")

        elif 'open WhatsApp' in query or "WhatsApp" in query:#opens whatsapp app
            codePath = "C:\\Users\\ULLHASYKUMAR\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)
        elif 'close whatsapp' in query:#opens github app
            os.system("taskkill /f /im WhatsApp.exe")


        elif 'open t launcher' in query or "minecraft" in query:#opens tlancher app
            codePath = "C:\\Users\\ULLHASYKUMAR\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(codePath)
        

        elif 'open notepad++' in query or "notepad++" in query:#opens notepad++
            codePath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(codePath)
        
        elif 'open reader' in query or "adobe reader" in query:#opens Adobe Acrobat Reader DC
            codePath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(codePath)
        
        elif 'open open office' in query or "open office" in query:#opens open office 4
            codePath = "C:\\Program Files (x86)\\OpenOffice 4\\program\\soffice.exe"
            os.startfile(codePath)
       

        elif 'open school time table' in query or "school time table" in query:#opens school timetable
            codePath = "Downloads\\Msg_11_77923_d846f36f-8025-4f38-946d-1642d36b1fd3_Nov 2 to Nov 6"
            os.startfile(codePath)


        elif 'good bye' in query:# code to exit
            good_bye=("good bye boss")
            speak(good_bye)
            exit()
        
        elif 'tell me a joke'in query:#code to tell a joke
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            
        elif 'password' in query:
	        speak("Ok Master")
	        speak("Here is Your Saved Connected Wifi Password")
	        Collect_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
	        Collect_profiles = [i.split(":")[1][1:-1] for i in Collect_data if "All User Profile" in i]
	        for i in Collect_profiles:
		        results=subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
		        results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
	        try:
		        print("Wifi name: {:<20}|  Password: {:<}".format(i, results[0]))
	        except:
		        print("Wifi name: {:<20}|  Password:  {:<}".format(i, ""))

        elif "what\'s up" in query or 'how are you' in query:#code to chat with us
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takecom()
            speak("what about you boss")
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  

        elif 'made you' in query or 'created you' in query or 'develop you' in query:#code to tell who made this
            ans_m = " For your information Ullhas Y Kumar Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)

        elif 'who is jarvis' in query :#code to tell who is jarvis
            ans_m = "My name is jarvis boss and i am your personal assistant "
            print(ans_m)
            speak(ans_m)
            ans = takecom()
            if 'okey' in ans:
                speak('okey..')
        
        elif 'calculate' in query:
            print("what should i do")
            Y = input()
            print("enter your 1st number")
            var1 = input()
            print("enter your 2nd number")
            var2 = input()
            if Y == '+':
                print("your answer =", int(var1) + int(var2))
            elif Y == '-':
                print("your answer =", int(var1) - int(var2))
                print("your other answer =", int(var2) - int(var1))
            elif Y == '/':
                print("your answer =", int(var1) / int(var2))
                print("your reminder =",int(var1)% int(var2))
            elif Y =='*':
                print("your answer =", int(var1) * int(var2))
            
        elif 'news' in query: 
              
            try:  
                jsonObj = urlopen('''http://newsapi.org/v2/everything?q=bitcoin&from=2020-11-27&sortBy=publishedAt&apiKey=3d14b78290054e3399821803104335b0''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the times of india') 
                print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e))

        elif 'what task do i have today' in query or 'my time today' in query or 'what work do i have' in query:#code to tell me my task of the day
            ans_m = "Today you have online class from 9:30 am to 12 o'clock and then your time table in shown here sir "
            speak('okey sir')
            print(ans_m)
            speak(ans_m)
            ans_from_user = takecom()
            speak('should i open anything boss')
            speak('should i open zoom or anything')

        elif "who are you" in query or "about you" in query or "your details" in query:#tells us what is this program about
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello Jarvis" in query:#code to chat
            hel = "Hello ULLHAS Boss ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:#tells us the assistant nane
            na_me = "Thanks for Asking my name my self ! Jarvis"  
            print(na_me)
            speak(na_me)
        elif "my name" in query or "MY NAME" in query:#tells you your name
            na = "Your name is ULLHAS,my boss"  
            print(na)
            speak(na)
    
        
        elif "you feeling" in query:#tells us the feeling os the assistant after meeting me
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 
        elif query == 'none':
            continue 
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :#code to make the program stop running
            ex_exit = 'Ok boss as you wish'
            speak(ex_exit)
            exit()    
        
