import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
'''for voice in voices:
 # to get the info. about various voices in our PC
 print("Voice:")
 print("ID: %s" %voice.id)
 print("Name: %s" %voice.name)
 print("Age: %s" %voice.age
 print("Gender: %s" %voice.gender)
 print("Languages Known: %s" %voice.languages)
voice_id = 
"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ENUS_ZIRA_11.0"
'''
engine.setProperty('voice', voices[1].id)
def wishMe():
 hour = int(datetime.datetime.now().hour)
 if hour>=0 and hour<12:
 talk("Good Morning!")
 elif hour>=12 and hour<18:
 talk("Good Afternoon!")
 else:
 talk("Good Evening!")
 talk("I am Alexa. Please tell me how may I help you")
def talk(text):
 engine.say(text)
 engine.runAndWait()
def take_command():
 command = ''
 try:
 with sr.Microphone() as source:
 print("calibrating...")
 listener.adjust_for_ambient_noise(source, 5)
 talk('Listening...')
 print('Listening...')
 voice = listener.listen(source)
 command = listener.recognize_google(voice)
 command = command.lower()
 if 'alexa' in command:
 command = command.replace('alexa','')
 print('Command:' + command)
 except:
 pass
 return command
def run_alexa():
 command = take_command()
 try:
 if 'play' in command:
 song = command.replace('play','')
 talk('Playing' + song)
 print('Playing' + song)
 pywhatkit.playonyt(song)
 elif 'time' in command:
 time = datetime.datetime.now().strftime('%I:%M %p')
 talk('Current time is '+time)
 print('Current time is '+time)
 elif 'who the heck is' or 'who' in command:
 person = command.replace('who the heck is','')
 info = wikipedia.summary(person,1)
 talk(info)
 print(info)
 elif 'joke' in command:
 joke = pyjokes.get_joke()
 talk(joke)
 print(joke)
 else:
 talk('Didnt get ya, Can you repeat?')
 print('Didnt get you, Can you repeat?')
 except:
 talk('Sorry, ConnectionError. Can you repeat?')
 print('Sorry, ConnectionError. Can you repeat?')
wishMe()
while(True):
 run_alexa()
 print('------------------------------------------------------------------------------------------------------------------------')

